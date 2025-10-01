from Oakmount.User.Login import Login
import pytest
import sys
import json

from Oakmount.User.Regester_user_parlaypro import regestration


class Test_parlay_pro:

    def test_create_user(self):
        login = Login()
        base_url =login.ParlayPro_base_url
        url = base_url+"user/register"
        reg = regestration()

        with open(r"C:\Users\Anuj d\Desktop\Testdata.json", "r") as f:
            data = json.load(f)

        print(data)  # whole dictionary
        print(data[0])# access a field

        # Vaild_cred: deside the test case have vaild data or not / True it meance test case is positive.
        # filed: if the test data is invaild then mention the name of filed.
        msg = reg.create_user(url,data[0],True,"")
        print(msg)



    def test_login_with_vaild_cred(self):
        print("Login OTP")
        login = Login()
        base_url= login.ParlayPro_base_url
        url = base_url+"users/login"
        user="anujtesting555@yopmail.com"
        password = "Pp@12345"
        responce = login.login_with_user(url,user,password)
        print(responce)

