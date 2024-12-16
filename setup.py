
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep

global driver

def login_useraccount():
    try:
        print("inter in code")
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        driver.get("https://wizzy-web-app.vercel.app/auth/login")
        driver.maximize_window()
        sleep(1)
        print("Script executed successfully")
        driver.find_element(By.XPATH,"//input[@id=':r0:']").send_keys("anujsubcription2@yopmail.com")
        driver.find_element(By.XPATH,"//input[@id=':r1:']").send_keys("Pass@123")
        sleep(3)
        driver.find_element(By.XPATH,"//button[contains(text(),'Sign In')]").click()
        print("wait for a min")
        sleep(10)
        username = driver.find_element(By.XPATH, "(//button[@type='button']/div/span)[3]").text
        if username== "Wizzy_QA Tester":
            print("Test case pass")
        else:
            print("expected : 'Wizzy_QA Tester' , Actual : {}".format(username))
        e=""
        return e

    except Exception as e:
        print("closed exception ",{e})

def logout_userAccount():
    try:
        global  driver
        login_useraccount()
        sleep(3)
        driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
        sleep(1)
        driver.find_element(By.XPATH,"//div[@id='dropdown-user']//li/button").click()
        sleep(3)
        driver.find_element(By.XPATH,"//div[2]/div[1]//div[2]/button[2]").click()
        sleep(2)

    except Exception as e:
        print({e})

def login_adminAccount():
    try:
        print("inter in code")
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        driver.get("https://wizzy-admin.vercel.app/auth-pages/login")
        driver.maximize_window()
        sleep(1)
        print("Script executed successfully")
        driver.find_element(By.XPATH,"//input[@id='loginUsername']").send_keys("wizzyadmin@yopmail.com")
        driver.find_element(By.XPATH,"//input[@id='loginPassword']").send_keys("Pass@123")
        sleep(3)
        driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
        print("wait for a min")
        sleep(4)
        login_toster = driver.find_element(By.XPATH, "//div[@class='header-left col-md']/b").text
        print(login_toster)
        if login_toster== "Login successful":
            print("Test case pass")
        else:
            print("expected : 'Login successful' , Actual : {}".format(login_toster))
        e=""
        return e

    except Exception as e:
        print("closed exception ",{e})


def logout_adminaccount():
    try:
        global  driver
        login_adminAccount()
        sleep(3)
        driver.find_element(By.XPATH,"//button[@type='button']//b[contains(text(),'Logout')]").click()
        sleep(3)
        driver.find_element(By.XPATH,"//div[2]/div[1]//div[2]/button[2]").click()
        sleep(2)
        logout_toster= driver.find_element(By.XPATH,"//div[@role='alert']/div[2]").text()
        if logout_toster== "Logout Successfully":
            print("Test case pass")
        else:
            print("expected : 'Logout Successfully' , Actual : {}".format(logout_toster))
        e=""
        return e

    except Exception as e:
        print("Error: ",{e})

logout_userAccount()
logout_userAccount()
logout_adminaccount()
logout_adminaccount()