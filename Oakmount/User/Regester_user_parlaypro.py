from datetime import datetime

from pyexpat.errors import messages

from Oakmount.User.Login import Login
import pytest
import requests

class regestration:
    def __init__(self):
        pass

    def create_user(self,url,data,vaild_cred,filed):
        try:

            name , email , password , confirmPassword,mobile,dob= data
            if data['fullName']:
                name = data['name']
            if data['email']:
                email= data['email']
            if data['password']:
                password = data['password']
            if data['confirmPassword']:
                confirmPassword = data['confirmPassword']
            if data['phone']:
                mobile = data['phone']
            if data['dob']:
                dob = data['dob']

            payload = {
                        "fullName": f"{name}",
                        "email": f"{email}",
                        "dob": f"{dob}",
                        "phone": f"{mobile}",
                        "password": f"{password}",
                        "confirmPassword": f"{confirmPassword}"
                        }
            responce= requests.post(url= url,json= payload)
            print(responce.json())

            if vaild_cred == True:
                if responce.status_code ==200:
                    if responce.json().get('msg') == "User created successfully":
                        return responce.json()
                    else:
                        print(f"Something went wrong: {str(responce.json().get('message'))}")
            else:
                messages = str(responce.json().get('msg'))
                messages = messages.split(',')

                if filed == "date":
                    if messages[0] == "Date of Birth must be in YYYY-MM-DD format" or messages[0] == "Invalid Date of Birth" or messages[0] == "User must be at least 13 years old":
                        return responce.json()
                elif filed == "email":
                    if messages[0] == "Email already registered" or messages[0] == "Please enter valid email":
                        return responce.json()
                elif filed == "Phone":
                    if messages[0] == "Phone number already registered" or messages[0] == "Phone must be a 10-digit number":
                        return responce.json()
                else:
                    print("pass")
        except Exception as e:
            print(e)


