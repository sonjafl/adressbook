# -*- coding: utf-8 -*-
from libs.commands.commandIntrface import commandInterface
from libs.saveload.storage import storage

class commandEdit(commandInterface):
    storage = None#häää??
    def __init__(self):
        self.name = "edit"
        self.storage = storage()#wozu?

    def process(self,username,usernamenumber):
        
        usernamenumber=usernamenumber.split()
        username=usernamenumber[0]
        #usernumber=usernamenumber[1]
        #print ('editing', username)
        
        if username in open('adressbook.txt').read():
            adressbook = open("adressbook.txt","r")
            lines = adressbook.readlines()
            for line in lines:
                if username in line:
                    print line
            newnumber=raw_input("please enter the new number:")
            self.storage.delete(username)
            self.storage.save(username,newnumber)
        
        else: print ('name does not exist yet, you can only create')
       
