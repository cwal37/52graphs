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

# result from first proper run-through
# http://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-for-u-s-air-carriers-operating-under-14-c-782f8


# To prevent download dialog
#profile = webdriver.FirefoxProfile()
#profile.set_preference('browser.download.folderList', 2) # custom location
#profile.set_preference('browser.download.manager.showWhenStarting', False)
#profile.set_preference('browser.download.dir', 'C:\Users\cwal3\Desktop\Development\wwtw\state_data')
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')


#fp = webdriver.FirefoxProfile('C:/Users/cwal3/AppData/Roaming/Mozilla/Firefox/Profiles/e8hk3z0p.default')
#driver  = webdriver.Firefox()
#
#'c:\users\cwal3\appdata\local\temp\tmpqtszgd'
#print driver.firefox_profile.path
#
#driver.close()

connection = urllib.urlopen("http://www.data.gov/metrics")
driver = webdriver.Firefox()
driver.get('http://www.data.gov/metrics')


#dom =  lxml.html.fromstring(connection.read())
i = 0
z =  581#rn.randint(20, 608)

for link in driver.find_elements_by_tag_name('a'): # select the url in href for all a tags(links)
    #browser = webdriver.Firefox()
    #complete_link = 'http://www.data.gov/metrics' + link
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

    #time.sleep(3)
    #print link.get_attribute('href')
    #time.sleep(5)
    #if i > 6:
        
        #page.click()
       # urllib.urlopen(complete_link)
      #  time.sleep(8)
        #save_me = ActionChains(br).key_down(Keys.CONTROL)\.key_down('s').key_up(Keys.CONTROL).key_up('s')
        #save_me.perform()
        #response = urllib.urlopen(complete_link)
        #with open(link, 'w') as f:
        #    f.write(response.read())
        
        
      #  time.sleep(8)
    i = i + 1
   # print i

    
   # print link
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