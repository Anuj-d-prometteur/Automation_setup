import traceback
from http.client import responses

import requests


class Login:
    # base_url ="https://api.oakmont.prometteur.in/"
    Oakmount_base_url = "https://api.oakmont.prometteur.in/"
    ParlayPro_base_url = "https://api.opticodds.prometteur.in/"

    def __init__(self):
        pass

    def login_with_user(self,url,user,password):
        try:
            print("Logging in...")
            payload = {"email": user, "password": password,"is_test":True}
            respons = requests.post(url, json=payload)

            if respons.status_code != 200:
                message = respons.json()["message"]
                print(f"{message}")
                return respons
            else:
                print("Login successful")
                return respons
        except:
            traceback.print_exc()
            print("Login failed")

    def login_with_2FA(self,base_url,payload):
        try:
            url=f"{base_url}api/users/verify-login"
            respons =requests.post(url, json=payload)
            assert respons.status_code == 200
            print(respons.json())
            return respons
        except:
            traceback.print_exc()
            print("Login OTP failed")
