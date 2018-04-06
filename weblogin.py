from selenium.webdriver.chrome.options import Options
from selenium import webdriver

    
class WebLogin:
    def __init__(self):
        self._webdriver = None
        self._chromeopt = None
        self._name_input = self._pass_input = self._login_btn = None

    def __del__(self):
        self._webdriver.close()
        del self._webdriver
        del self._chromeopt
    
    def launch(self,
               website='https://accounts.spotify.com/en/login',
               showGUI=True):
        self._chromeopt = Options()
        if not showGUI:
            self._chromeopt.add_argument("--headless")
        # self._chromeopt.add_argument(
        #    '--user-data-dir="~/.config/google-chrome"')
        # self._chromeopt.binary_location = '/usr/bin/google-chrome'
        self._webdriver = webdriver.Chrome(chrome_options=self._chromeopt)
        self._webdriver.get(website)

    # --------------------------------------
    def find_input(self):
        self._name_input = self._webdriver.find_element_by_xpath(
            '//input[@ng-model="form.username"]')
        if self._name_input is None:
            raise Exception("Not find username input")
        #
        self._pass_input = self._webdriver.find_element_by_xpath(
            '//input[@ng-model="form.password"]')
        if self._pass_input is None:
            raise Exception("Not find password input")
        #
        self._login_btn = self._webdriver.find_element_by_xpath(
            '//button')
        if self._login_btn is None:
            raise Exception("Not find login button")

    def send_keys(self, user="default", passwd=""):
        self._name_input.clear()
        self._name_input.send_keys(user)
        self._pass_input.clear()
        self._pass_input.send_keys(passwd)
        self._login_btn.click()


