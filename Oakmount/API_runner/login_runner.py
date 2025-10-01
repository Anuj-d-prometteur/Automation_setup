import sys
import traceback

from Oakmount.User.Login import Login
import pytest

class TestLogin:


    def test_login_with_vaild_inputs(self):
        login = Login()
        # url = self.ParlayPro_base_url +"/user/login"
        url = login.Oakmount_base_url+"api/users/login"
        Username = "anujdesai21@yopmail.com"
        Password = "Pass@123"
        userId_And_code = login.login_with_user(url,Username,Password)

        if userId_And_code.json()['status_code'] == 200:
            data = login.login_with_2FA(userId_And_code.json()['data'])
            bearer =data.get('access_token')
            userdetails= data.json()['data'].get('user_data')
            print(userdetails)

            # assert userdetails['first_name'] == "test", f"Expected first_name={userdetails['first_name']}, but got {userdetails}"
            # assert userdetails["last_name"] == "test", f"Expected last_name={userdetails["last_name"]}, but got {userdetails}"
            # assert userdetails["username"] == "test", f"Expected username={userdetails["username"]}, but got {userdetails}"
            # assert userdetails["email"] == "<EMAIL>", f"Expected email={userdetails["email"]}, but got {userdetails}"
            # assert userdetails["dob"] == "", f"Expected dob={userdetails["dob"]}, but got {userdetails}"
            # assert userdetails["contact_number"] == "", f"Expected contact_number={userdetails["contact_number"]}, but got {userdetails}"
            # assert userdetails["affiliate_code"] == "", f"Expected affiliate_code={userdetails["affiliate_code"]}, but got {userdetails}"
            # assert userdetails["affiliate_referral_code"] == "", f"Expected affiliate_referral_code={userdetails["affiliate_referral_code"]}, but got {userdetails}"
            # assert userdetails["user_id"] == "", f"Expected user_id={userdetails["user_id"]}, but got {userdetails}"
            return bearer
        else:
            print("Test failed")
            traceback.print_exception(*sys.exc_info())

    def test_login_with_invaild_inputs(self):
        login = Login()
        data = login.login_with_user("anujdesai21@yopmail.com", "Pass@122")
        megs = data.json()['message']
        assert data.json()['status_code'] == 403 , f"Expected status_code= 403, but got {data.json()['status_code']}"
        assert megs == "Invalid credentials", f"Expected error message= 'Invalid credentials', but got {megs}"
        print("Test Case Passed")

    def test_Top_fails(self):
        login = Login()
        data = login.login_with_user("anujdesai21@yopmail.com", "Pass@123")
        if data.json()['status_code'] == 200:
            data = login.login_with_2FA(data.json()['data'])
            if data.json()['status_code'] == 400:
                print("Login failed")

                if data.json()['message'] == "Incorrect code." or data.json()['message'] == "Code expired or invalid.":
                    print("Incorrect text message")
        else:
            traceback.print_exception(*sys.exc_info())

