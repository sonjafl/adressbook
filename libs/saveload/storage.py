'''
Created on 30.10.2013

@author: sonja
'''

class storage(object):
    
    source = "adressbook.txt"
    
    def save(self,username,number):
        #print ('saving name and number',username,number)
        adressbook = open(self.source,'a')
        newcontact=[str(username),' ', str(number),'\n']
        adressbook.writelines(newcontact)
        
        adressbook.close()
        
    def delete(self,username):
        adressbook = open(self.source,"r")
        lines = adressbook.readlines()
        adressbook.close()
        adressbook = open(self.source,"w")
        for line in lines:
            if not str(username) in line:  
            #if line!=str(username)+'\n':
                adressbook.write(line)
        adressbook.close()
    
    def edit(self):
        pass
    
    def findByName(self, name):
        if name in open('adressbook.txt').read():
            adressbook = open("adressbook.txt","r")
            lines = adressbook.readlines()
            for line in lines:
                if name in line:
                    return line
    
#def load(self):
#    pass
    
