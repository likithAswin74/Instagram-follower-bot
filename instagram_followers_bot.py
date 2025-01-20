from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

# keep the chrome even after the chrome finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # entering the email
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys("likithaswin15@gmail.com")

        # entering the password
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys("Instagram@123")

        # clicking the login button
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        # clicking the not now button
        time.sleep(8)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR, ".x78zum5 div")
        not_now_button.click()

        # clicking the not now button on avoid notification
        time.sleep(4)
        notifications_button = self.driver.find_element(By. CSS_SELECTOR, '._ap36')
        notifications_button.click()

    def find_followers(self):
        time.sleep(5)
        # opening the person account
        self.driver.get("https://www.instagram.com/udemy/followers/")

        # clicking the followers on the account. and it will open a popup message which contains followers
        time.sleep(4)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        followers.click()

        # getting the popup message's xpath (popup window xpath) to perform the scroll down operation
        time.sleep(5)
        model_xpath = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div')
        for i in range(10):
            # used to scroll down on the popup window
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model_xpath)
            time.sleep(2)


    def follow(self):
        time.sleep(5)

        # storing all the follow buttons in all_buttons
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".x1nhvcw1 ._ap30")
        print(all_buttons)

        for button in all_buttons:
            # clicking all the buttons one by one
            try:
                time.sleep(4)
                # print(button.text)
                button.click()
                print("success")
            except ElementClickInterceptedException:
                continue


obj = InstaFollower()
obj.login()
obj.find_followers()
obj.follow()