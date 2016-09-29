# -*- coding: utf-8 -*-  
  
from distutils.core import setup   
import py2exe                            
  
includes = ["encodings", "encodings.*"]
data_files = []
options = {"py2exe":   
            {   "compressed": 1,           
                "optimize": 2,   
                "bundle_files": 1,   
                "includes": includes  
                  
            }   
          }   
  
setup(       
    version = "0.1.0",
    description = "fileCheck0.1.0",
    name = "fileCheck0.1.0",
    options = options,   
    zipfile=None,  
	data_files = data_files, 
    console=[{"script": "UI.py"}]
    )  