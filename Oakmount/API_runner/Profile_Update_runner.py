from Oakmount.User.Login import Login
from Oakmount.User.Profile_update import Profile_update

class TestProfile_update:

    def test_Update_profile(self):
        login = Login()
        user = "anujdesai21@yopmail.com"
        Password = "Pass@123"
        Update = Profile_update()
        # url = self.ParlayPro_base_url +"/user/login"
        url = login.Oakmount_base_url+"api/users/login"

        UserPayload = login.login_with_user(url, user, Password)
        userdetails = login.login_with_2FA(login.Oakmount_base_url, UserPayload.json()['data'])
        print(userdetails.json())
        msg = Update.user_details(login.Oakmount_base_url,userdetails)
        print(msg)
        if msg == "Barrer token is not received.":
            print(f"Test Case Assert failed. {str(msg)}")

        elif msg == "Test Case Assert failed.":
            print(f"Test Case Assert failed. {str(msg)}")
        else:
            print(f"Test Case Assert passed.{str(msg)}")
