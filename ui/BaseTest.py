from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r"/Users/amityerva/PycharmProjects/SeleniumAPI/Drivers/chromedriver")
        self.webDriverWait = WebDriverWait(self.driver, 10)
        print("----------  Run started at : " + str(datetime.datetime.now()) + "  ----------")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.ndtv.com/")

    def tearDown(self) -> None:
        if self.driver is not None:
            print("----------  Run Completed at : " + str(datetime.datetime.now()) + "  ----------")
            self.driver.close()
            self.driver.quit()
