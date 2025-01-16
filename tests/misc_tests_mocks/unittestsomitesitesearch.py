import unittest
import selenium
from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import service
from time import sleep

class researchsomesite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        opts = Options()
        opts.add_argument("-headless")
        self.browser = Firefox(options=opts)
        self.browser.get("https://www.some_site.com/")

    def tearDown(self):
        self.driver.close()

    def get_somesitesreenshot(self):

        self.driver.save_full_page_screenshot("some_site.png")
        assert os.path.exists("some_site.png")


    def careerssearch_via_hyperlink(self):

        workingwithus = self.driver.find_element(By.CLASS_NAME, "ckc-primary-nav__link")
        workingwithus.click()
        sleep(3)

    def careerssearch_in_jobpagetitle(self):
        driver = self.driver
        driver.get("https://www.some_site.ca/en/services/jobs/opportunities.html")
        self.assertIn("Find a job - SomeSite.ca", driver.title)

