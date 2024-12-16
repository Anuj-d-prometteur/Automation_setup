from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from Modules import setup
from selenium.webdriver.common.by import By

submit_button= "//button[@type='submit']"

setup.login_useraccount()

def setup_edge():
    try:
        # Automatically download and set up the correct EdgeDriver
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

        # Open the desired URL
        driver.get("https://wizzy-web-app.vercel.app/auth/login")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for a few seconds
        sleep(3)

        print("Edge setup completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def verify_the_login_with_invaild_otp():
    global driver
    # driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-qez9d7']//button").click()
    driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-5gktoq']//button").click()
    driver.find_element(By.XPATH,"//input[@id='mobileNumber']").send_keys("7769925139")
    driver.find_element(By.XPATH,submit_button).click()
    sleep(3)
    for index   in range(6):
        sleep(1)
        #print("//div//input[@id='otp-input-{}']".format(index))
        driver.find_element(By.XPATH,"//div//input[@id='otp-input-{}']".format(index)).send_keys(str(index))

    sleep(1)
    driver.find_element(By.XPATH,"//button[contains(text(),'Enter OTP')]").click()
    sleep(1)
    error_message =driver.find_element(By.XPATH,"//div/p[contains(text(),'User')]").text

    if error_message == "User Not Found or OTP not matched":
        print("Test Cases Pass")
    else:
        print("Test Cases Failed")
    driver.close()


