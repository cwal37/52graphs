# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""

from selenium import webdriver
import time
import urllib
import lxml.html
import random as rn
import pandas as pd


connection = urllib.urlopen("http://www.data.gov/metrics")
driver = webdriver.Firefox()
driver.get('http://www.data.gov/metrics')

df = pd.read_csv('chosen_numbers.csv')

numbers = list(df['numbers'])
week = len(numbers) - 1

i = 0
number_range = list(range(20,608))

rand_options = [x for x in number_range if x not in numbers]

z = rn.randint(rand_options)    


for link in driver.find_elements_by_tag_name('a'): # select the url in href for all a tags(links)

    print i
    print z

    if i == z:
        if link.get_attribute('href') != 'javascript:void(0)':
            complete_link = str(link.get_attribute('href'))
            try:
                if complete_link[48] != '(': 
                    print(link.get_attribute('href'))
                    data = str(link.get_attribute('href'))
                if complete_link[48] == '(':
                    z = z+1
            except AttributeError:
                z = z+1
        if link.get_attribute('href') == 'javascript:void(0)':
            z = z+1

    i = i + 1

driver.close()
driver.quit()


driver = webdriver.Firefox()
driver.get(data)

new_elements =  list(driver.find_elements_by_tag_name('a'))
new_links = [str(x.get_attribute('href')) for x in new_elements ]

driver.close()
driver.quit()

final_link_set = []
#http://catalog.data.gov/dataset/
for link in new_links:
    if link[:32] == 'http://catalog.data.gov/dataset/':
        final_link_set.append([link])
        
choice = rn.randint(0, len(final_link_set))
link_choice = final_link_set[choice]


driver = webdriver.Firefox()
driver.get(link_choice)
        
    

#
##
##fxProfile = new.FirefoxProfile();
##
##fxProfile.setPreference("browser.download.folderList",2);
##fxProfile.setPreference("browser.download.manager.showWhenStarting",false);
##fxProfile.setPreference("browser.download.dir","c:\\mydownloads");
##fxProfile.setPreference("browser.helperApps.neverAsk.saveToDisk","text/csv");
##
##WebDriver driver = new.FirefoxDriver(fxProfile);
#
#browser = webdriver.Firefox(profile)
#page = browser.get("http://cdiac.ornl.gov/ftp/ushcn_daily/")
#
##browser.find_element_by_id('exportpt').click()
##browser.find_element_by_id('exporthlgt').click()
#
##page.click("link=.gz")
#
#browser.close()
#browser.quit()