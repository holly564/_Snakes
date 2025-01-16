from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def navigation_rodeo_on_website():
    driver = webdriver.Firefox()
    driver.get('https://some_site.com/careers/opportunities/')
    assert "Careers opportunities | SOMESITE" in driver.title
    element = driver.find_element(By.ID, "video-2")
    element.click()
    driver.close()


def get_screenshot_jobs_website():
    from datetime import date

    driver = webdriver.Firefox()
    driver.get('https://some_site.com/careers/opportunities/')
    assert "Careers opportunities | SOMESITE" in driver.title

    try:
        element2 = driver.find_elements(By.CLASS_NAME, "jv-job-list-name")
        filename = "cbnco_careers_page_" + str(date.today())+ ".png"
        driver.get_screenshot_as_file("test.png")
    except NoSuchElementException as myexception:
        print(myexception)

    driver.quit()