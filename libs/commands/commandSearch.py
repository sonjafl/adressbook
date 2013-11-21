# -*- coding: utf-8 -*-
from libs.commands.commandInterface import commandInterface

class commandSearch(commandInterface):
    
    def __init__(self):
        self.name = "search"
        super(commandSearch, self).__init__()

    def process(self,username,usernamenumber):
        
        usernamenumber=usernamenumber.split()
        username=usernamenumber[0]
        user = self.storage.search(username)
        
        if user is not None:
            print user
        else: 
            print ('name does not exist yet, you can only create')