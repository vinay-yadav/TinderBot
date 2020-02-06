from selenium import webdriver
from time import sleep
from secrets import *


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('/home/carlmark/PycharmProjects/TinderBot/chromedriver_79')

    def login(self):
        date = '15'
        month = '8'
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

        contbtn = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        contbtn.click()
        sleep(2)
        radio_btn = self.driver.find_element_by_xpath('//*[@id="u_3_9"]/div[2]/label[1]/span')
        radio_btn.click()

        self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]').click()
        sleep(3)
        date_field = self.driver.find_element_by_xpath('//*[@id="u_5_9"]/span[1]')
        date_field.click()
        sleep(1)
        date_in = self.driver.find_element_by_xpath(f'//*[@id="js_m"]/div/div/ul/li[{date}]/a/span/span')
        date_in.click()

        month_f = self.driver.find_element_by_xpath('//*[@id="u_5_c"]/span[1]')
        month_f.click()
        sleep(1)
        month_in = self.driver.find_element_by_xpath('//*[@id="js_x"]/div/div/ul/li[8]/a/span/span')
        month_in.click()

        year_f = self.driver.find_element_by_xpath('//*[@id="u_5_f"]/span[1]')
        year_f.click()
        sleep(2)
        year_in = self.driver.find_element_by_xpath('//*[@id="js_18"]/div/div/ul/li[10]/a/span/span')
        year_in.click()

        ctnbtn1 = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        ctnbtn1.click()
        sleep(4)
        ctnbtn2 = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        ctnbtn2.click()
        sleep(6)
        self.driver.switch_to.window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(2)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        btn.click()

    def dislike(self):
        btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        btn.click()

    def autoswipe(self):
        try:
            n = 0
            while True:
                sleep(0.5)
                self.like()
                n +=1
        except Exception:
            print(n)
            self.driver.close()


bot = TinderBot()
bot.login()
bot.autoswipe()

