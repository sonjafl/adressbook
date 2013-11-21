'''
Created on 30.10.2013

@author: sonja
'''

class storage(object):
    
    def save(self,username,number):
        #print ('saving name and number',username,number)
        adressbook = open("adressbook.txt",'a')
        newcontact=[str(username),' ', str(number),'\n']
        adressbook.writelines(newcontact)
        
        adressbook.close()
        
    def delete(self,username):
        adressbook = open("adressbook.txt","r")
        lines = adressbook.readlines()
        adressbook.close()
        adressbook = open("adressbook.txt","w")
        for line in lines:
            if not str(username) in line:  
            #if line!=str(username)+'\n':
                adressbook.write(line)
        adressbook.close()
    
#def load(self):
#    pass
    
