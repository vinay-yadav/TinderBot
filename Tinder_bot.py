from selenium import webdriver
from time import sleep
from secrets import *


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('/home/carlmark/PycharmProjects/TinderBot/chromedriver_79')

    def login(self):
        try:
            self.driver.get('https://tinder.com')
            sleep(5)
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
            fb_btn.click()

            # switching window
            base_window = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[1])

            email = self.driver.find_element_by_xpath('//*[@id="email"]')
            email.send_keys(username)

            password = self.driver.find_element_by_xpath('//*[@id="pass"]')
            password.send_keys(loginkey)

            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()

            sleep(2)

            self.driver.switch_to.window(base_window)

            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()
            sleep(2)
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()

        except Exception:
            self.driver.close()

    def like(self):
        btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        btn.click()

    def dislike(self):
        btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        btn.click()

    def autoswipe(self):
        try:
            while True:
                sleep(0.5)
                self.like()
        except Exception:
            self.driver.close()


bot = TinderBot()
bot.login()
bot.autoswipe()

