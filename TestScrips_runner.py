from robot.libraries.DateTime import get_current_date

from Modules.Admin_Panel import Bookmakers
from Modules.Admin_Panel import setup

#validation meassage

url_msg="Url is required!"
Title_msg="Title is required!"
Successfully_message= ""
Updated_message="Bookmaker updated successfully"
Invalid_title_message=""
Invalid_URl_message=""

Title_name= "Automation"+get_current_date()
Title_name=Title_name.split(" ",1)

Url_name="http://"+Title_name[0]+"/test.com"

#<<<<<<<<<<   Test Cases    >>>>>>>>>

#verify the create bookmakers
def verify_create_bookmakers():
    driver=setup.login_adminAccount()
    print("create bookmakers")
    data = ["True", "wizzy", "http://wizzy.com",Successfully_message]
    Bookmakers.create_bookmakers(data,driver)
    print("logout driver")
    setup.logout_adminaccount(driver)

#verify the mandatory filed for create bookmakers
def verify_create_bookmakers_Allmandatory_filed():
    driver=setup.login_adminAccount()
    print("create bookmakers")
    data = ["True","", "",url_msg,Title_msg]
    Bookmakers.create_bookmakers(data,driver)
    print("logout driver")
    setup.logout_adminaccount(driver)

def verify_create_bookmakers_Titlemandatory_filed():
    driver=setup.login_adminAccount()
    print("create bookmakers")
    data = ["True", "",Url_name,url_msg,Title_msg]
    Bookmakers.create_bookmakers(data,driver)
    print("logout driver")
    setup.logout_adminaccount(driver)

def verify_create_bookmakers_URLmandatory_filed():
    driver=setup.login_adminAccount()
    print("create bookmakers")
    data = ["True",Title_name,"",url_msg,Title_msg]
    Bookmakers.create_bookmakers(data,driver)
    print("logout driver")
    setup.logout_adminaccount(driver)

#verify changing title and url of bookmakers
def verify_Edit_Bookmakers():
    driver = setup.login_adminAccount()
    print("create bookmakers")
    print(Title_name)
    data = ["True",Title_name[0], Url_name,Updated_message]
    Bookmakers.edit_bookmakers(data,driver)
    print("logout driver")
    setup.logout_adminaccount(driver)

def verify_Edit_statusOf_Bookmakers():
    driver = setup.login_adminAccount()
    print("create bookmakers")
    print(Title_name)
    data = ["False","","",Updated_message]
    Bookmakers.edit_bookmakers(data,driver)
    print("logout driver")
    setup.logout_adminaccount(driver)


#verify_create_bookmakers_mandatory_filed()
verify_Edit_Bookmakers()

