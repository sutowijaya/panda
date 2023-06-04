#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#@title ***SELENIUM SOCKS5***
from seleniumwire import webdriver
import time

options = {
        'proxy': {
            #'http': 'socks5://ambon:gaming@143.198.198.4:2408', 
            #'https': 'socks5://ambon:gaming@143.198.198.4:2408',
            'no_proxy': 'localhost,127.0.0.1'
        }  
    }


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome('chromedriver', options=chrome_options,seleniumwire_options=options)
driver.get("https://shifu.mrpandabear.org/mine?wallet=002CA3573BA9FB3CEDB451A4D85E5A7D29DF5D2000DCC9AD27")
print(driver.title)
time.sleep(999999)
