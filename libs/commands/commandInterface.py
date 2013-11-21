# -*- coding: utf-8 -*-
from libs.saveload.storage import storage

class commandInterface(object):
    """
      Command Interface - provides common interface for command Modules
      @todo: refactor to abstract
    """
   
    name = None
    storage = None
    
    def __init__(self):
        self.storage = storage()
    
    def process(self, userparameter):
        """
           Main process function 
        """
        pass

   
   
    
