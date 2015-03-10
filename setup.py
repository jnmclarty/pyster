import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
        
v = '0.1.0beta'
  
setup(name = "PySter",
      version = v,
      packages = ['pyster'],
      install_requires=['rrsm'],
      description = 'Python *anywhere',
      long_description=(read('README.md')),    
      author = "Jeffrey McLarty",
      author_email = "jeffrey.mclarty@gmail.com",
      url = 'https://github.com/jnmclarty/pyster',
      download_url = 'https://github.com/jnmclarty/pyster/tarball/' + v,    
      keywords = ["pyster"],
      classifiers = ['Development Status :: 4 - Beta',
                     'Operating System :: Microsoft :: Windows :: Windows 7',
                     'Programming Language :: Python :: 2.7'])