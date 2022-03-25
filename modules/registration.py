import re
import json

from pandas import date_range
def regValidation ():
    condition =True
    while condition:
        Fname=input("please enter your first Name")
        condition=validateTextInput(Fname)
    condition =True
    while condition:
        Lname=input("please enter your last Name")
        condition=validateTextInput(Lname)
    condition =True
    while condition:
        Email=input("please enter your Email")
        condition=isnotValidMail(Email)
        condition=isusedMail(Email)
    condition =True
    while condition:
        from getpass import getpass
        password = getpass("please enter your password")
        if len(password)>=8:
            condition=False
    condition =True
    while condition:
        Confirm_password = getpass("please reenter your password")
        if Confirm_password==password:
            condition=False
    condition =True
    while condition:
        phone=input("please enter your phoneNumber")
        condition=isnotValidPhone(phone)
    #------------------------------------------
    #writeToAfile("regfile.txt",Fname,Lname,Email,password,phone)
    #data={"f"{Email}":{password,Fname,Lname,phone}"}
    data ={"email":Email,"password":password,"Fname":Fname,"Lname":Lname,"phone":phone}
    print(type(data))
    write_json(data,"userDB.json")

def validateTextInput (string :str):
    if string.isalpha():
        return False
    else :
        return True

        
def isnotValidMail(email :str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return False
    else:
        return True

def isnotValidPhone(phone :str):
    r=re.fullmatch('01[0-2 5][0-9]{8}',phone) # calling fullmatch function by passing pattern and n
    if r!=None: # checking whether it is none or not 
        return False
    else:
        return True
def isusedMail(mail :str):
    with open('userDB.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    condition =list(filter (lambda Email:Email['email'] == mail,json_object))
    if condition: 
        return True
    return False
def write_json(new_data, filename):
    with open(filename,'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
    file_data.append(new_data)
        # Sets file's current position at offset.
    with open (filename ,"w") as file:
        # convert back to json.
        json.dump(file_data, file, indent = 4)


def writeToAfile(fileName :str,*args):
    data=f"{args[0]}:{args[1]}:{args[2]},{args[3]}:{args[4]}\n"
    try:
        with open(fileName,"a") as wfile:
            wfile.write(data)
        #wfile =open(fileName,"a")
        print("file opened with success")
    except Exception as e:
        print (e)
    else:
        
        #wfile.write(data)
        wfile.close()