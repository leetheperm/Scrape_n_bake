# Scrape n Bake


![Pyhton3.8](https://img.shields.io/badge/Python-3-blue)
![PyPI - Status](https://img.shields.io/pypi/status/wheel)


## Objective

The objective of this project is to create a web scraping application that can be used for the most common use cases 


## Tech stack

Python 3.8
Beautiful Soup
Selenium Webdriver
Geckodriver


## Libraries

install all requirements by typing
```
pip3 -r install requirements.txt
```

options

--help has help menu

### arguments

-u url (pass one url into the command line)
-l list of urls (path to text file of urls)
-f findAll (pass arguments like h1 or p or similar)
-s selector (to be done later)
-r regex (to be done later)
-p preset + preset name (phonenum, email, )
-w write to file (give file path and file name)
-t telephone number
### examples

```
pyhton3 webscrape.py -u site.com -f "h1"
```
or
```
python3 webscrape.py -l /usr/share/listofsites -f "p"
```

