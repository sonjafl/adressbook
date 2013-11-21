# -*- coding: utf-8 -*-
from libs.commands.commandInterface import commandInterface

class commandDelete(commandInterface):
    
    def __init__(self):
        self.name = "delete"
        super(commandDelete, self).__init__()

    def process(self,username,usernamenumber):
        
        usernamenumber=usernamenumber.split()
        username=usernamenumber[0]
        #usernumber=usernamenumber[1]
        #print ('deleting', username)
        self.storage.delete(username)
        