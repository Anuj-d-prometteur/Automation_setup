from http.client import responses

import requests


class Login:
    base_url ="https://api.oakmont.prometteur.in/"

    def __init__(self):
        pass

    def login_with_user(self,user,password):
        print("Logging in...")
        url = f"{self.base_url}api/users/login"
        payload = {"email": user, "password": password,"is_test":True}
        respons = requests.post(url, json=payload)

        if respons.status_code != 200:
            message = respons.json()["message"]
            status_code = respons.json()["status_code"]
            print(f"{message}: {status_code}")
        else:
            userdeatils= respons.json()["data"]
            print(respons.json())
            return(userdeatils)


    def login_with_2FA(self,payload):
        url=f"{self.base_url}api/users/verify-login"
        payload=payload
        respons =requests.post(url, json=payload)
        assert respons.status_code == 200
        print(respons.json())
        return (respons)

