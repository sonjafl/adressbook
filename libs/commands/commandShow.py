# -*- coding: utf-8 -*-
from libs.commands.commandInterface import commandInterface

class commandShow(commandInterface):
    
    def __init__(self):
        self.name = "show"
        super(commandShow, self).__init__()
        
    def process(self,usercommand,usernamenumber):
        whattoshow = usernamenumber
        #print ('usernamenumber(commandshow)',usernamenumber)
        #print ('whatttoshow',whattoshow)
        adressbook = open("adressbook.txt","r")
        lines = adressbook.readlines()
        
        if whattoshow=='all':
            lines.sort()
            print lines
        else: 
            for line in lines:
                if whattoshow in line:
                    print line
                    
            #TODO: gibt es sowas wie "wenn du keine zeile gefunden hast die zutrifft, dann print "gibts nicht""?
            #im moment wird "name does not exist" jedes mal angezeigt
            else: print ('name does not exist')
            
        adressbook.close()
           
            # else: 
            #    print ('else')#wenn es den namen nicht gibt, print(name esxistiert nicht))