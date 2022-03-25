import re
import json
from modules.registration import isnotValidMail
def logValidation ():
    condition =True
    while condition:
        while condition:
            Email=input("please enter your Email")
            condition=isnotValidMail(Email)
        condition =True
        while condition:
            from getpass import getpass
            password = getpass("please enter your password")
            if len(password)>=8:
                condition=False
        condition =True
        condition = isTheUsernotExistJson(Email,password)
    print ("the user is logged in successfully")
    return Email
    


def isTheUsernotExist(Email :str,password :str): 
    with open("regfile.txt","r") as Rfile:
        usersData=Rfile.readlines()
        for user in usersData:
            userDataList=list(user.strip("\n").split(":"))
        for i in userDataList:
            if i==f"{Email},{password}":
                print (i)
                return False
        print("notfound") 
        return True

def isTheUsernotExistJson(Email :str,password :str): 
    with open("userDB.json","r") as Rfile:
        json_object = json.load(Rfile)
    condition =list(filter (lambda item:( item['email'] == Email and item['password'] == password) ,json_object))
    if condition: 
        return False
    return True 
    

