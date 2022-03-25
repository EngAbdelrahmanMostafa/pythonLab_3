from textwrap import indent
from modules.registration import validateTextInput
from modules.registration import write_json
from modules.login import logValidation
from datetime import datetime
import re
import json
def addProject(Email :str):
    condition =True
    while condition:
        Title=input("please enter your project title")
        condition=validateTextInput(Title)
    condition =True
    while condition:
        Details=input("please enter your project details")
        condition=validateTextInput(Details)
    condition =True
    while condition:
        Target=input("please enter your total target")
        condition=validateintInput(Target)
    condition =True
    while condition:
        sDate=input("please enter your start Date")
        condition=validateDateInput(sDate)
    condition =True
    while condition:
        eDate=input("please enter your end Date")
        condition=validateDateInput(eDate)
    #------------------------------------------
    #writeToAfile("regfile.txt",Fname,Lname,Email,password,phone)
    #data={"f"{Email}":{password,Fname,Lname,phone}"}
    data ={"Title":Title,"Details":Details,"Target":Target,"sDate":sDate,"eDate":eDate,"owner":Email}
    print(type(data))
    write_json(data,"projectsDB.json")

def validateintInput(target:str):
    if target.isnumeric():
        return False
    return True

def validateDateInput(date :str):
    # initializing format
    DateRegex =r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
    if re.fullmatch(DateRegex, date):
        return False
    else:
        return True
def viewAllProjects():
    with open('projectsDB.json','r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
    print ("-\-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-/-")
    print (file_data)

def EditaProject(Email :str):
    condition =True
    viewAllProjects()
    while condition:
        Title=input("please enter your project title to edit")
        condition=validateTextInput(Title)
        condition=checkProjectOwner(Email,Title)
    #print(list(filter (lambda mail:mail['owner'] == Email and mail['Title'] == Title ,json_object)))
    with open('projectsDB.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    element=dict(next((item for item in json_object if item['owner'] == Email and item['Title'] == Title), None))
    json_object[:] = [d for d in json_object if d.get('Title') != Title and d.get('owner') != Email]
    with open ('projectsDB.json' ,"w") as file:
    # convert back to json.
        json.dump(json_object, file, indent = 4)
    condition =True
    while condition:
        Title=input("please enter your project title old Title is : "+element.get('Title'))
        condition=validateTextInput(Title)
    condition =True
    while condition:
        Details=input("please enter your project details old details is : "+element.get('Details'))
        condition=validateTextInput(Details)
    condition =True
    while condition:
        Target=input("please enter your total target old total target is : "+element.get('Target'))
        condition=validateintInput(Target)
    condition =True
    while condition:
        sDate=input("please enter your start Date old start date is "+element.get('sDate'))
        condition=validateDateInput(sDate)
    condition =True
    while condition:
        eDate=input("please enter your end Date old end date is "+element.get('eDate'))
        condition=validateDateInput(eDate)
    #------------------------------------------
    #writeToAfile("regfile.txt",Fname,Lname,Email,password,phone)
    #data={"f"{Email}":{password,Fname,Lname,phone}"}
    
    data ={"Title":Title,"Details":Details,"Target":Target,"sDate":sDate,"eDate":eDate,"owner":Email}
    print(type(data))
    write_json(data,"projectsDB.json")

def checkProjectOwner(Email,Title):
    with open('projectsDB.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    condition =list(filter (lambda mail:mail['owner'] == Email and mail['Title'] == Title ,json_object))
    if condition: 
        return False
    return True

def deleteaProject (Email):
    condition =True
    viewAllProjects()
    while condition:
        Title=input("please enter your project title to delete")
        condition=validateTextInput(Title)
        condition=checkProjectOwner(Email,Title)
    condition =True
    while condition:
        Del=input("Are you sure you want to delete this project ? Y/N")
        if Del =="Y":
            condition=False
        elif Del == "N":
            return 0
        else:
            condition=True
    with open('projectsDB.json','r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
    file_data[:] = [d for d in file_data if d.get('Title') != Title and d.get('owner') != Email]
        # Sets file's current position at offset.
    with open ('projectsDB.json' ,"w") as file:
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def searchwithDate():
    condition =True
    while condition:
        sDate=input("please enter the start Date of the project")
        condition=validateDateInput(sDate)
    with open('projectsDB.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    element=dict(next((item for item in json_object if item['sDate'] == sDate ), None))
    print(element)