from logging import exception
from time import sleep
from turtledemo.clock import setup
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from Modules.Admin_Panel import setup


def create_bookmakers(data,driver):
     try:
         print("inter the method")
         driver.find_element(By.XPATH,"//div[@class='aside-body']//a[@href='/bookmakers-Management']").click()
         headers=driver.find_element(By.XPATH,"//b[contains(text(),'Bookmakers Management')]").text
         if headers!="Bookmakers Management":
             print("Expected Name: 'Bookmakers Management' , Actual :",headers )
         else:
             driver.find_element(By.XPATH,"//button[contains(text(),' Add New Bookmakers')]").click()
             sleep(1)
             driver.find_element(By.XPATH,"//input[@name='title']").send_keys(data[1])
             driver.find_element(By.XPATH,"//input[@name='url']").send_keys(data[2])
             driver.find_element(By.XPATH,"//select[@name='status']").click()
             driver.find_element(By.XPATH,f"//select[@name='status']/option[@value='{data[0]}']").click()
             driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
         sleep(3)
         if data[1]!="" and data[2]!="":
             title_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
             url_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
             driver.find_element(By.XPATH, "//div[@class='modal-content']//button[@aria-label='Close']").click()
             print(f"Test Failed: Expected ='{data[3]}',Actual ='{data[4]}'")
         else:
             successfully_msg=driver.find_element(By.XPATH,"//div[contains(text(),'Bookmaker updated successfully')]").text
             print(f"Test Failed: Expected ='{data[3]}',Actual ='{successfully_msg}'")
             print("Test Case Pass.")
         e=None
         return e
     except Exception as e:
         print("closed exception ", {e})
         traceback.print_exc()

def edit_bookmakers(data,driver):
    try:
        Name=None
        Url=None
        print("inter the method")
        driver.find_element(By.XPATH, "//div[@class='aside-body']//a[@href='/bookmakers-Management']").click()
        headers = driver.find_element(By.XPATH, "//b[contains(text(),'Bookmakers Management')]").text
        if headers != "Bookmakers Management":
            print("Expected Name: 'Bookmakers Management' , Actual :", headers)
        else:
            sleep(2)
            search_key=driver.find_element(By.XPATH,"//table//tr[3]/td[3]/div").text
            sleep(2)
            driver.find_element(By.XPATH,"//input[@id='searchInput']").send_keys(search_key)
            sleep(4)
            driver.find_element(By.XPATH,"(//table//tr[1]/td[6]//button)[1]").click()
            sleep(1)
            driver.find_element(By.XPATH, "//input[@name='title']").clear()
            driver.find_element(By.XPATH, "//input[@name='title']").send_keys(data[1])
            driver.find_element(By.XPATH, "//input[@name='url']").clear()
            driver.find_element(By.XPATH, "//input[@name='url']").send_keys(data[2])
            driver.find_element(By.XPATH, "//select[@name='status']").click()
            sleep(1)
            driver.find_element(By.XPATH, f"//select[@name='status']/option[@value='{data[0]}']").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
        sleep(3)
        error_msg=driver.find_element(By.XPATH,"//div[contains(text(),'Bookmaker updated successfully')]").text
        if error_msg!=data[3]:
            exception("successfully message is not displayed")
        else:
            driver.find_element(By.XPATH, "//input[@id='searchInput']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys(data[1])
            sleep(2)
            Name=driver.find_element(By.XPATH, "//table//tr[1]/td[3]").text
            Url=driver.find_element(By.XPATH, "//table//tr[1]/td[4]").text
            sleep(1)
        if Name!=data[1] and Url!=data[2]:
            exception("Updated Name and URl is not match")
        else:
            print("Test cases pass")

    except Exception as e:
        print("closed exception ", {e})
        traceback.print_exc()

