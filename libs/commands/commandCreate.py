# -*- coding: utf-8 -*-
from libs.commands.commandInterface import commandInterface
import re

class commandCreate(commandInterface):
    def __init__(self):
        self.name = "create"
        super(commandCreate, self).__init__()
        
    def process(self, usercommand,usernamenumber):
        usernamenumber=usernamenumber.split()
        username=usernamenumber[0]
        usernumber=usernamenumber[1]
        
        #print ('username,usernumber(create.process)', username,usernumber)
        tel=re.compile("[0-1]+")
        usernumber2 = tel.match(usernumber)
        number=usernumber2.group()
        if number:
            if username in open('adressbook.txt').read():
                print ('name already exists, you can only edit')
            else:
                #print ('Will create entry with name and number:', username, number)
                self.storage.save(username,number)#wieso so umständlich?
            
        else:
            print 'Number seems to be wrong'
        
        #save username und usernumber in file
