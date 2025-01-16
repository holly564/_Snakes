from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup, SoupStrainer
import logging


def diagnose_cbno_careers_page():
    from bs4 import diagnose

    # Set up logging to troubleshoot if anything goes wrong
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # Initialize the WebDriver
    logging.info("Launching Diagnose of some_site page")

    with open("This  Company, Limited Careers.htm") as fp:
        data = fp.read()
    diagnose.diagnose(data)

    logging.info("End of diagnosing")


def parse_only_positions():
    # Set up logging to troubleshoot if anything goes wrong
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize the WebDriver
    logging.info("Initializing WebDriver")
    driver = webdriver.Firefox()
    driver.get("https://jobs.jobvite.com/some_site/?nl=1&fr=false")

    only_a_tags = SoupStrainer("a")
    only_tr_tags = SoupStrainer("tr")

    soup = BeautifulSoup(driver.page_source, "html5lib", recursive=True)
    returned_a_tags = soup.find_all(SoupStrainer("tr"))
    if returned_a_tags:
        for result in returned_a_tags:
            print(result)

    logging.info("Closing WebDriver")
    driver.quit()


def parse(self, response):
    driver = webdriver.Firefox()
    driver.get("https://jobs.jobvite.com/some_site/?nl=1&fr=false")
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.findAll('tr', class_='"job-list-name"')

    for link in links:
        yield {
            'id': link['id'],
            'title': link.find_all('td')[2].a.text,
            'url': link.find_all('td')[2].a['href'],
            'rank': int(link.td.span.text.replace('.', ''))
        }

    driver.quit()


def scraping_titles_with_selenium():
    # Set up logging to troubleshoot if anything goes wrong
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize the WebDriver
    logging.info("Initializing WebDriver")
    driver = webdriver.Firefox()
    driver.get("https://jobs.jobvite.com/some_site/?nl=1&fr=false")
    driver.find_element(By.CLASS_NAME, "h2")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    BeautifulSoup(driver.page_source, "html5lib")

    # Find all titles on the page (class - titleline)
    logging.info("Finding all position text or links on the page")
    section = soup.find_all('h3', string='h2', recursive=True)
    if section:
        logging.info('"Found {len(section}. Printing section:')
        for a_section in section:
            a_section_child = a_section.findNext('table')
            if a_section_child:
                print(a_section.next_siblings)

    # Close the driver
    logging.info("Closing WebDriver")
    driver.quit()


if __name__ == '__main__':
    diagnose_cbno_careers_page()
    scraping_titles_with_selenium()
