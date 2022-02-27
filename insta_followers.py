import time
import shutil
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_option)

Download_path = r"C:\Users\dalla\.wdm\drivers\chromedriver\win32"
CHROME_DRIVER = os.environ.get("CHROMEDRIVER")

try:
    service = Service(executable_path=CHROME_DRIVER)
except Exception as r:
    print(r)
    CHROM_VERSION = ChromeDriverManager().driver.get_version()
    service = Service(executable_path=ChromeDriverManager().install())
    shutil.move(os.path.join(Download_path, CHROM_VERSION, "chromedriver.exe"), r"C:\WebDriver\bin")


class InstaFollowers:
    def __init__(self, webdriver_, insta_user, insta_pass, account_name):
        self.driver = webdriver_
        self.insta_user = insta_user
        self.insta_pass = insta_pass
        self.account_name = account_name
        self.insta_website = r"https://www.instagram.com/"

    def insta_login(self):
        self.driver.get(self.insta_website)
        self.driver.implicitly_wait(10)
        insta_user_name = self.driver.find_element(By.NAME, "username")
        insta_user_name.send_keys(self.insta_user)
        self.driver.implicitly_wait(10)
        insta_password = self.driver.find_element(By.NAME, "password")
        insta_password.send_keys(self.insta_pass)
        self.driver.implicitly_wait(10)
        login = self.driver.find_element(By.XPATH, "//*[text()='Log In']")
        login.click()

    def do_not_save_info(self):
        cancel_save = self.driver.find_element(By.XPATH, '//*[text()="Not Now"]')
        self.driver.implicitly_wait(10)
        cancel_save.click()

    def search_for_account(self):
        self.driver.implicitly_wait(10)
        account = self.driver.find_element(By.XPATH, '//*[@aria-label="Search Input"]')
        account.send_keys(self.account_name)
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.XTCLo')))
        select_search_menu = self.driver.find_element(By.CSS_SELECTOR, '.XTCLo')
        time.sleep(2)
        select_search_menu.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        select_search_menu.send_keys(Keys.ENTER)

    def follow(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.visibility_of_element_located((By.XPATH,
                                               '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')))
        select_followers = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        self.driver.implicitly_wait(10)
        select_followers.click()
        time.sleep(2)
        followers = self.driver.find_elements(By.XPATH, '//*[text()="Follow"]')
        followers.pop(0)
        for f in followers:
            try:
                f.click()
                time.sleep(3)
                update_followers = self.driver.find_elements(By.XPATH, '//*[text()="Follow"]')
                update_followers.pop(0)
                for n in update_followers:
                    if n not in followers:
                        followers.append(n)
                f.send_keys(Keys.ARROW_DOWN)
            except Exception as r:
                pass
