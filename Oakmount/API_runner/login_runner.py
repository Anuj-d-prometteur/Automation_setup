import sys
import traceback

from Oakmount.User.Login import Login
import pytest

class TestLogin:


    def test_login_with_vaild_inputs(self):
        login = Login()
        userId_And_code = login.login_with_user("anujdesai21@yopmail.com","Pass@124")
        if userId_And_code != None:
            data=login.login_with_2FA(userId_And_code)
            bearer =data['access_token']
            userdetails= data['user_data']
            assert userdetails.first_name == "test", f"Expected first_name={userdetails.first_name}, but got {userdetails}"
            assert userdetails.last_name == "test", f"Expected last_name={userdetails.last_name}, but got {userdetails}"
            assert userdetails.username == "test", f"Expected username={userdetails.username}, but got {userdetails}"
            assert userdetails.email == "<EMAIL>", f"Expected email={userdetails.email}, but got {userdetails}"
            assert userdetails.dob == "", f"Expected dob={userdetails.dob}, but got {userdetails}"
            assert userdetails.contact_number == "", f"Expected contact_number={userdetails.contact_number}, but got {userdetails}"
            assert userdetails.affiliate_code == "", f"Expected affiliate_code={userdetails.affiliate_code}, but got {userdetails}"
            assert userdetails.affiliate_referral_code == "", f"Expected affiliate_referral_code={userdetails.affiliate_referral_code}, but got {userdetails}"
            assert userdetails.user_id == "", f"Expected user_id={userdetails.user_id}, but got {userdetails}"
        else:
            pytest.fail("Unexpected failure")