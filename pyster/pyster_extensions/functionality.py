import hashlib as hl
import pandas as pd
from math import pi
import re

def HardCodedPassword(seed):
    """Returns a hardcoded password"""
    passwords = {'gmail' : 'BadUnsecurePassw0rd', 'facebook' : 'WhoUsesFacebook', 'github' : 'CodeIsPoetry'}
    if seed in passwords.keys():
        return passwords[seed]
    else:
        return "DefaultPassword"

hcp = HardCodedPassword
        
def HashPassword(seed):
    """Returns the Hex Digest of any seed"""
    tmp = hl.sha256(seed).hexdigest()
    print tmp
    return str(tmp) 

hp = HashPassword

def CustomHumanDerivableButRediculouslyHardPassword(seed):
    """Implements a custom approach to building a password dynamically"""
    tmp = seed + 'pyStar'
    
    def infi(l,i):
        """Simulates an indefinitely long, repeated, list, by looping over the elements in a single list."""
        return l[i % len(l)]
        
    return "".join([x + infi(["!","@","#","."],i) + str(i) for i,x in enumerate(tmp)])

cp = CustomHumanDerivableButRediculouslyHardPassword

def AutomatedParagraph(Name,Num,Den):
    #Just an example
    tmp = "Hello " + Name + "\n Your account has grown by " + str(Num) + ".  This represents an increase of " + str(round((Num/Den) * 100,4)) + "% off of your previous balance (" + str(Den) + "), so your new total is " + str(Den+Num) + "."
    
    if Num > 0:
        return tmp + "This is great!"
    else:
        return tmp + "You should try harder."

ap = AutomatedParagraph
        
def CheckGmail():
    #TODO
    return "You have no new messages"

cg = CheckGmail

def SearchGmail():
    #TODO
    return "\n".join([str(i) + "result" * ((i % 3) + 1) for i in range(10)])

sg = SearchGmail
       
def SendEmailToSelf(msg):
    #TODO
    return "Sent"

se = SendEmailToSelf

def PriceOf(symbol):
    #TODO
    return "$193.88"

sq = PriceOf

def CreateClass():
    return """class ClassName(object):
    \"\"\" Information about the class \"\"\"
    def __init__():
       \"\"\" Information about the class \"\"\"
    def __repr__(self):
       return "'{}()'.format(self.__name__)"""

def newlines():
    return """\n\n\n\n"""
    
def nl(n):
    tmp = "\n".join([str(i+1) for i in range(n)])
    return tmp
    
df1 = pd.DataFrame({'one' : pd.Series(pd.np.random.randn(6),index=list('abcdef')),
                    'two' : pd.Series(pd.np.random.randn(6),index=list('abcdef')),
                    'three' : pd.Series(pd.np.random.randn(6),index=list('abcdef'))})

df2 = pd.DataFrame({'animal' : ['cat'] * 3 + ['dog'] * 2 + ['bird'] * 4,
                    'weight' : [2.5,2.6,2.3] + [5.3,5.8] + [0.2,0.2,0.2,0.3],
                    'color' : ['white','black','brown'] + ['brown','black'] + ['black'] * 4})


def p2e(df):
    """First attempt to convert pandas DF to Excel"""
    tmp = str(df)
    tmp = re.sub(' +','\t',tmp)
    return tmp
    
def p2e2(df):
    """Second attempt to convert pandas DF to Excel"""
    #lb = [0x28] + [0x25] * len(df.columns)
    s = "\t".join([""] + list(df.columns)) + "\n\n"
    for row in df.iteritems():
        tmp = [str(v) for v in row[1].values]
        s = "\t".join([str(row[0])] + tmp) + "\n\n"
    return s
   
site = "C:\\WinPython-32bit-2.7.8.2\\python-2.7.8\\Lib\\site-packages"

def em(to=None):
    if to:
        tmp = "+".join(to.split(" ") + ["do","not","spam","please"])
        return "first.last{}@gmail.com".format(tmp)
    else:
        return "first.last@gmail.com"

redditpass = "theresalwaysmoneyinthebananastand"