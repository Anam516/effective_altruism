# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:18:10 2017

@author: hussaina

Scrapper to get Address, Description, Name, Purpose and Website (if any) from the source http://www.pcnc.com.ph/ngo-list.php
Python version 3.6
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

Name=[]
Address=[]
Purpose=[]
Website=[]
Description=[]

url_temp="http://www.pcnc.com.ph/ngo-list-with-bir.php?page="
for i in range (1,27):
    url=url_temp
    url+=str(i)
    
    try:
        r=requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        x=soup.find_all('span', class_='current')
        for xs in x:
            link=xs.find_all('a')
            for links in link:
                link1='http://www.pcnc.com.ph/'
                link1+=(links.get('href'))
                z=requests.get(link1)
                soup_2 = BeautifulSoup(z.content, "html.parser")
                info=soup_2.find_all('span', class_='ngodetails')
            
            
                description=soup_2.find_all('td')
                
               
            
            
                Name.append(info[0].text)
                Address.append(info[1].text)
                Purpose.append(info[11].text)
                Website.append(info[10].text)
                Description.append(description[12].text)
                
    
    except ConnectionError:
        time.sleep(20)
columns = {'Name': Name, 'Address': Address, 'Website': Website, 'Purpose': Purpose, 'Description':Description}

df=pd.DataFrame(columns)
df.to_excel('NGO.xlsx')
