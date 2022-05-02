import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:

    def __init__(self, e_mail, password, down, up, provider, user_name):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = down
        self.up = up
        self.e_mail = e_mail
        self.password = password
        self.int_provider = provider
        self.user_name = user_name
        self.driver.set_window_position(-10000, 0)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        cookie_button_xpath = '/html/body/div[6]/div[2]/div[1]/div[5]/button[2]'
        cokie_button = self.driver.find_element(by=By.XPATH, value=cookie_button_xpath)
        cokie_button.click()

        go_button_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        go_button = self.driver.find_element(by=By.XPATH, value=go_button_xpath)
        go_button.click()

        print("Down and up speed is being measured..")
        time.sleep(60)

        go_results_button_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[' \
                                  '8]/div/div/div[2]/a '
        go_results_button = self.driver.find_element(by=By.XPATH, value=go_results_button_xpath)
        go_results_button.click()

        up = self.driver.find_element(by=By.CLASS_NAME, value='upload-speed')
        up = up.text
        down = self.driver.find_element(by=By.CLASS_NAME, value='download-speed')
        down = down.text

        return [down, up]

    def tweet_at_provider(self, down_speed, up_speed):
        message = f"Hey {self.int_provider}, why is my internet speed {down_speed}down/{up_speed}up when I pay for {self.down}down/{self.up}up?"
        self.driver.get("https://twitter.com/home")

        print('Logining your twitter account')

        time.sleep(5)

        username_input = self.driver.find_element(by=By.NAME, value='text')
        username_input.send_keys(self.e_mail)
        username_input.send_keys(Keys.ENTER)

        time.sleep(5)

        user_name = self.driver.find_element(by=By.NAME, value='text')
        user_name.send_keys(self.user_name)
        user_name.send_keys(Keys.ENTER)

        time.sleep(5)

        password_input = self.driver.find_element(by=By.NAME, value='password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)

        print('You logged in.')
        time.sleep(5)
        print('Twitting your message..')

        entry = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        entry.send_keys(message)

        time.sleep(5)

        send_button = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        send_button.click()

        print('Your message is Twitted ..')

        self.driver.quit()
