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


#pathToBinary = new File("C:\\user\\Programme\\FirefoxPortable\\App\\Firefox\\firefox.exe");
#ffBinary = new FirefoxBinary(pathToBinary);
#firefoxProfile = new FirefoxProfile();       
#driver = new FirefoxDriver(ffBinary,firefoxProfile);

connection = urllib.urlopen("http://www.data.gov/metrics")
driver = webdriver.Firefox()
driver.get('http://www.data.gov/metrics')

df = pd.read_csv('chosen_numbers.csv')

numbers = list(df['numbers'])
week = len(numbers) - 1

i = 0
number_range = list(range(20,608))

rand_options = [x for x in number_range if x not in numbers]
data = 0

while  data == 0:
    z = rn.choice(rand_options)    
    
    
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
        
    
