# from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import sys
import time
import re
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html, 'lxml')

keys = Keys()
options = Options()

options.headless = True
options.set_preference("browser.privatebrowsing.autostart", True)


class Offer_test:
    def __init__(self):
        self.driver = webdriver.Firefox(
            options=options, executable_path='/Users/lee.davies/Downloads/Geckodriver')
        self.site_list_choice = sys.argv[1]

    def url_grab(self):
        site_list_choice = self.site_list_choice
        driver = self.driver
        if site_list_choice == '-u':
            driver.get('http://www.' + sys.argv[2])
            self.find_all()
        elif site_list_choice == '-l':
            with open(sys.argv[2], 'r') as file1:
                lines = file1.readlines()
                for line in lines:
                    line = line.strip()
                    driver.get('http://' + line)
                    time.sleep(1)
                    # self.find_all()
                    self.directory_grabber()
        elif site_list_choice == '-S':
            self.SEO_checker()
        else:
            print('other options not available')

    def regex_email_grabber(self):
        """ An email parser

        attributes:
        	EMAIL_REGEX: expression to grab common and obscure email cases
        """
        driver = self.driver
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        for re_match in re.finditer(EMAIL_REGEX, driver.page_source):
            print(re_match.group())

    def directory_grabber(self):
    	""" A directory parser

    	Attributes: 
    		URL_REGEX: expression to find common directories
    	"""
        driver = self.driver
        URL_REGEX = r"""(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"""
        for re_match in re.finditer(URL_REGEX, driver.page_source):
            print(re_match.group())

    def phone_grabber(self):
    	""" A phone number parser

    	Attributes:
			PHONE_REGEX: experssion for most common phone numbers
    	"""
        driver = self.driver
        PHONE_REGEX = r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"
        for re_match in re.finditer(URL_REGEX, driver.page_source):
            print(re_match.group())

    def find_all(self):
    	""" A Beautiful Soup scraping function using Findall 

    	Attributes:
    		bs: handles the Beautiful Soup parser and pulls text from Selenium page_source object
    		highlight: lists through iterations of provided html attribute for example ('h2')
    	"""
        driver = self.driver
        find_all_param = sys.argv[3]
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        highlight = bs.findAll("%s" % find_all_param)
        for high in highlight:
            print(high.get_text().strip())

# run = Offer_test()
# run.url_grab()


#greentext = bsObj.findAll("span", {"class": "green"})
# for name in greentext:
# 	print(name.get_text())

# h_find = bs.findAll(id="text")
# for h in h_find:
# 	print(h.get_text())

# red_text = bs.findAll("span", {"class": "red"})
# for red in red_text:
# 	print(red.get_text())
