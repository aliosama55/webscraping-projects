import requests # type: ignore
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
import lxml

job_title = []
company_name = []
location_name = []
skills = []


# The role of this function is to get all the data inside the 
results = requests.get("https://wuzzuf.net/search/jobs/?q=Python&a=hpb")
# The role of this function is to get the text content inside the website
src = results.content
# i need to investigate further more on these three functions as they seems the core of scraping
soup = BeautifulSoup(src,"lxml")
job_titles = soup.find_all("a", {"class":"css-o171kl"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
location_names = soup.find_all("span", {"class":"css-5wys0k"})
job_skills = soup.find_all("a" ,{"class":"css-o171kl","class":"css-5x9pm1"})

# Range tells him to iterate for number of times so it is an iteratable object (an object that you can iterate with ) but if you write 7 only this means a thing like r for ex
# range function (satrt,stop,step)  start optional, step optional but stop is the number that we 


""" for i in range(len(job_titles)):
  
  job_title.append(job_titles[i].text)
  company_name.append(company_names[i].text)
  location_name.append(location_names[i].text)
  skills.append(job_skills[i].text)
    
print(job_title,company_name,location_name,skills)"""

print(company_names)