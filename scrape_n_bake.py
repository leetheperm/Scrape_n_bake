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
		self.driver = webdriver.Firefox(options=options, executable_path='/Users/lee.davies/Downloads/Geckodriver')
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
					driver.get('http://'+ line)
					time.sleep(1)
					# self.find_all()
					self.directory_grabber()
		elif site_list_choice == '-S':
			self.SEO_checker()			
		else:
			print('other options not available')

	def email_grabber(self):
		driver = self.driver
		EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
		for re_match in re.finditer(EMAIL_REGEX, driver.page_source):
			print(re_match.group())		

	def directory_grabber(self):
		driver = self.driver
		URL_REGEX = r"""(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"""
		for re_match in re.finditer(URL_REGEX, driver.page_source):
			print(re_match.group())		

	def phone_grabber(self):
		driver = self.driver
		PHONE_REGEX = r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"
		for re_match in re.finditer(URL_REGEX, driver.page_source):
			print(re_match.group())	

	def find_all(self):
		driver= self.driver
		find_all_param = sys.argv[3]
		bs = BeautifulSoup(driver.page_source,'html.parser')
		highlight = bs.findAll("%s" % find_all_param)
		for high in highlight:
			print(high.get_text().strip())

	# def	SEO_checker(self):
	# 	driver = self.driver
	# 	pass
		# try:
  #           page_title = browser.find_element_by_css_selector('meta[name="title"]')
  #           print('Page title: ', end='')
  #           print(page_title.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           meta_des = browser.find_element_by_css_selector(
  #               'meta[name="description"]')
  #           print('meta description: ', end='')
  #           print(meta_des.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           twitter_site = browser.find_element_by_css_selector(
  #               "meta[name='twitter\\:site']")
  #           print('twitter site: ', end='')
  #           print(twitter_site.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           twitter_creator = browser.find_element_by_css_selector(
  #               "meta[name='twitter\\:creator']")
  #           print('twitter creator: ', end='')
  #           print(twitter_creator.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           url_twitter = browser.find_element_by_css_selector(
  #               "meta[name='twitter\\:url']")
  #           print('twitter url: ', end='')
  #           print(url_twitter.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           twitter_title = browser.find_element_by_css_selector(
  #               "meta[name='twitter\\:title']")
  #           print('twitter title: ', end='')
  #           print(twitter_title.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           twitter_description = browser.find_element_by_css_selector(
  #               "meta[name='twitter\\:description']")
  #           print('twitter dexcription: ', end='')
  #           print(twitter_description.get_attribute('content'))
  #       except:
  #           pass
  #       # Facebook meta data
  #       print('-'*20)
  #       print('FACEBOOK')
  #       try:
  #           facebook_site = browser.find_element_by_css_selector(
  #               "meta[property='og:site_name']")
  #           print('Facebook site: ', end='')
  #           print(facebook_site.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           url_facebook = browser.find_element_by_css_selector(
  #               "meta[property='og\\:locale']")
  #           print('facebook language: ', end='')
  #           print(url_facebook.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           facebook_title = browser.find_element_by_css_selector(
  #               "meta[property='og\\:title']")
  #           print('facebook title: ', end='')
  #           print(facebook_title.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           facebook_description = browser.find_element_by_css_selector
  #           ("meta[property='og\\:description']")
  #           print('facebook description: ', end='')
  #           print(facebook_description.get_attribute('content'))
  #       except:
  #           pass
  #           # break between
  #       print('-'*20)
  #       print('OTHER META DATA')
  #       try:
  #           item_prop = browser.find_element_by_css_selector(
  #               "meta[property='og\\:country-name']")
  #           print('country name: ', end='')
  #           print(item_prop.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           item_prop = browser.find_element_by_css_selector(
  #               "meta[itemprop='name']")
  #           print('item prop name: ', end='')
  #           print(item_prop.get_attribute('content'))
  #       except:
  #           pass
  #       try:
  #           canonical_link = browser.find_element_by_css_selector(
  #               'link[rel="canonical"')
  #           print('canonical link: ', end='')
  #           print(canonical_link.get_attribute('href'))
  #       except:
  #           pass
  #       try:
  #           item_prop = browser.find_element_by_css_selector(
  #               "meta[itemprop='keywords']")
  #           print('Keywords: ', end='')
  #           print(item_prop.get_attribute('content'))
  #       except:
  #           pass		



run = Offer_test()
run.url_grab()


#greentext = bsObj.findAll("span", {"class": "green"})
# for name in greentext:
# 	print(name.get_text())

# h_find = bs.findAll(id="text")
# for h in h_find:
# 	print(h.get_text())

# red_text = bs.findAll("span", {"class": "red"})
# for red in red_text:
# 	print(red.get_text())