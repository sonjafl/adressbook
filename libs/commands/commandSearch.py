# -*- coding: utf-8 -*-
from libs.commands.commandIntrface import commandInterface
from libs.saveload.storage import storage

class commandSearch(commandInterface):
    storage = None#häää??
    def __init__(self):
        self.name = "search"
        self.storage = storage()#wozu?

    def process(self,username,usernamenumber):
        
        usernamenumber=usernamenumber.split()
        username=usernamenumber[0]
        #usernumber=usernamenumber[1]
        #print ('searching', username)
        
        if username in open('adressbook.txt').read():
            adressbook = open("adressbook.txt","r")
            lines = adressbook.readlines()
            for line in lines:
                if username in line:
                    print line
        else: print ('name does not exist yet, you can only create')