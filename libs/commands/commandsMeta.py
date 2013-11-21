
'''
Created on 14.01.2013

@author: sonja
'''
from libs.commands.commandCreate import commandCreate
from libs.commands.commandDelete import commandDelete
from libs.commands.commandEdit import commandEdit
from libs.commands.commandSearch import commandSearch
from libs.commands.commandShow import commandShow

class commandsMeta(object):
    
    commands=[]
    
    def __init__(self):
        self.commands.append(commandCreate())
        self.commands.append(commandDelete())
        self.commands.append(commandEdit())
        self.commands.append(commandSearch())
        self.commands.append(commandShow())
        
        
    def validcommand(self,usercommand):
        for cmd in self.commands:
            #print ('cmd(commandsmeta)',cmd.name)
            if cmd.name == usercommand:
                return True
        else:
            return False 
                
    def process(self,usercommand,usernamenumber):
        for cmd in self.commands:
            if cmd.name == usercommand:
                cmd.process(usercommand,usernamenumber)
    
    
    
        