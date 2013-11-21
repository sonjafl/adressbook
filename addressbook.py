# -*- coding: utf-8 -*-

from libs.commands.commandsMeta import commandsMeta
#create sonja 0011
class addressbook(object):
    #TODO:?
    commandsMeta = None
    #TODO:?
    def __init__(self, *args, **kwargs):
        self.commandsMeta = commandsMeta()
    
    def main(self):
        self.welcomeScreen()
        self.printHelp()
        
        while True:
            userinputlist = self.readUI()
            #print ('userinputlist',userinputlist)
                       
            if userinputlist==False:
                #print "Wrong command (addressbook.py)"
                self.printHelp()
            else:
                self.commandsMeta.process(userinputlist[0],userinputlist[1])
                
            # process user input callttr
        
        
    def welcomeScreen(self):
        print "welcome to sonjas addressbook"
        
    def printHelp(self):
        print "create [name and number]"
        print "delete [name]"
        print "edit [name]"
        print "search [name]"
        
        
        
    def readUI(self):
        userinput=raw_input("please enter your command:")
        return  self.inputparser(userinput)
        
        
    def inputparser(self,userinput):
        userinputlist=userinput.split(' ',1)
        usercommand=userinputlist[0]
        usernamenumber=userinputlist[1]
        #print ('usernamenumber(inputparser)',usernamenumber)
        #usernumber=userinputlist[2]
        if self.commandsMeta.validcommand(usercommand) == True:
            return userinputlist   
        else:
            #print ('nix da (addressbook.inputparser)')
            return False
        
    

    
        
    
    
    



if __name__ == '__main__':
    ad = addressbook()
    
    ad.main()