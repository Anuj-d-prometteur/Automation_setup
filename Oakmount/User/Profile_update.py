import traceback

import requests

from Oakmount.User.Login import Login

class Profile_update:

    login = Login()

    def user_details(self,base_url,userdetails):
        try:
            barrer = userdetails.json()['data'].get('access_token')
            user_data= userdetails.json()['data'].get('user_data')

            if barrer != None:
                url = f"{base_url}api/users/update-profile"
                payload = {"username": "Test1","s3_key":"profile_images/1746687639.jpg",
                            "first_name": "Automation",
                           "last_name":"test"}
                headers = {"Authorization": f"Bearer {barrer}"}
                response = requests.put(url,json=payload,headers=headers)

                try:
                    assert response.json()['status_code'] == 200
                    assert response.json()['message'] == "User Profile Updated successfully."
                    assert response.json()['data']['username'] == user_data.get('username') ,f"The Username expected is {user_data.get('username')} but got {response.json()['data']['username']}"
                    assert response.json()['data']['first_name'] == user_data.get('first_name') ,f"The first name expected is {user_data.get('first_name')} but got {response.json()['data']['first_name']}"
                    assert response.json()['data']['last_name'] == user_data.get('last_name') , f"The last name expected is {user_data.get('last_name')} but got {response.json()['data']['last_name']}"
                    return "User Profile Updated successfully."
                except AssertionError as e:
                    print(e)
                    return f"Test Case Assert failed:{str(e)}."
            else:
                return "Barrer token is not received."
        except AssertionError as e:
            traceback.print_exc()
            return f"Something went wrong: {str(e)}"