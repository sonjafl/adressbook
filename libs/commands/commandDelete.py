# -*- coding: utf-8 -*-
from libs.commands.commandIntrface import commandInterface
from libs.saveload.storage import storage

class commandDelete(commandInterface):
    storage = None#häää??
    def __init__(self):
        self.name = "delete"
        self.storage = storage()#wozu?

    def process(self,username,usernamenumber):
        
        usernamenumber=usernamenumber.split()
        username=usernamenumber[0]
        #usernumber=usernamenumber[1]
        #print ('deleting', username)
        self.storage.delete(username)
        