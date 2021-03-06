##############################################################################
#
# Imports not written by Jeffrey McLarty
#
# Caution should be taken when sourcing these.
#
###############################################################################
import pyHook    # Can be sourced on sourceforge
import pythoncom # Comes with PyWin32 at Gohlke's site: 
                 # http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32

##############################################################################
#
# These are part of the standard library.  
#
###############################################################################
import traceback
import datetime as dt

###############################################################################
#
# This code came from a stack overflow question and answer.  
#
###############################################################################
import keyboarder as kb

###############################################################################
#
# RRSM is a module written and maintained by Jeffrey McLarty, it is very easy
# to install and inspect for yourself. It was actually created in order
# to build the first prototype of PySter.  It is installed automatically,
# if you installed PySter via pip.
#
###############################################################################
from rrsm import StateMachine

###############################################################################
#
# PySter will have access to any functions in the standard library and
# anything that gets defined in this file.  You are free to use my examples
# but encouraged to submit pull requests for your own.
#
###############################################################################
from pyster_extensions import *

class PySter(object):    
    def __init__(self,debug=False):
        self.KeysPressed = ""
        self.State = StateMachine(['LISTENING','CAPTURINGCODE','PRINTING'])
        self.Debug = debug
        self.LastRight = dt.datetime.now()
    def right_double(self,event):
        if (dt.datetime.now() - self.LastRight) < dt.timedelta(seconds=1):
            print "Fire!"
        self.LastRight = dt.datetime.now()
        
    def pressed_chars(self,event):
        if self.Debug and (self.State != self.State.PRINTING):

            out = []
            out.append(str(event.KeyID))
            out.append(str(event.ScanCode))
            out.append(str(event.Ascii))
            out.append(str(event.flags)) 
            #out = [str(x) for x in (event.KeyID,event.ScanCode,event.Ascii,event.flags)]
            print "KeyID\tScanCode\tAscii\tflags"
            print "\t".join(out)
            
        if event.Ascii == kb.VK_BACK: #backspace
            self.KeysPressed = self.KeysPressed[:-1:]
        elif event.Ascii == 26: #ctrl-z
            self.KeysPressed = ""
        else:
            if event.Ascii:
                x = chr(event.Ascii)
            
            if self.State == self.State.LISTENING:
                if event.Ascii:
                    if event.Ascii >= 32 and event.Ascii <= 126:
                        if x == '>':
                            self.KeysPressed += x
                            if self.KeysPressed[-3:] == ">>>":
                                if self.Debug:
                                    print "Starting to capture"
                                self.State.switch_to(self.State.CAPTURINGCODE)
                                self.KeysPressed = ""
                        else:
                            self.KeysPressed = ""                            
            elif self.State == self.State.CAPTURINGCODE:
                if event.flags == 1:
                    if self.Debug:
                        print type(event.ScanCode)
                    if event.ScanCode == 77: #up or down arrow
                        code = "ans = " + str(self.KeysPressed)
                        if self.Debug:
                            print list(self.KeysPressed)
                            print "{" + code + "}"
                        try:
                            exec(code)
                            bu = chr(kb.VK_BACK) * (len(self.KeysPressed) + 3)
                            self.State.switch_to(self.State.PRINTING)
                            self.NKeysToPrint = len(str(ans))
                            kb.ghost_write(bu + str(ans))
                        except SyntaxError:
                            print "*" * 10
                            #print traceback.print_exc()
                            print "Syntax Error while trying to execute: {}".format(code)
                        except Exception as e:
                            self.KeysPressed = ""
                            print e.message
                            raise
                        self.State.switch_to(self.State.LISTENING)
                        self.KeysPressed = ""
                elif event.Ascii:
                    if event.Ascii >= 32 and event.Ascii <= 126:
                        self.KeysPressed += x
            elif self.State == self.State.PRINTING:
                self.NKeysToPrint -= 1
                #if self.Debug:
                #    print "Printing" + str(self.NKeysToPrint)
                if self.NKeysToPrint <= 0:
                    self.State.switch_to(self.State.LISTENING)

if __name__ == '__main__':
    MyPySter = PySter(debug=True)
    
    proc = pyHook.HookManager()
    proc.KeyDown = MyPySter.pressed_chars
    proc.HookKeyboard()
    
    pythoncom.PumpMessages()