# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:24:17 2021

@author: VigneshSS
"""


#https://www.synerzip.com/blogs/web-scraping-introduction-applications-and-best-practices/#:~:text=Web%20scraping%20typically%20extracts%20large,show%20data%20from%20a%20website.

##robots.txt

"""
githubapi
swapi
jsonplaceholder

https://www.analyticsvidhya.com/blog/2020/04/5-popular-python-libraries-web-scraping/

5 popular libraries used for Webscraping :
    
1.BeautifulSoup
2. Selenium
3. Scrapy
4. Requests (HTTP for Humans) Library for Web Scraping
5. lxml Library for Web Scraping
"""

# BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

#print(res.text)
#print(soup)
#print(soup.body.contents)
#print(soup.find_all('div'))  #find('a)
#https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
#https://www.w3schools.com/cssref/css_selectors.asp


#print(soup.select('.storylink')[0:4]) #. means its class
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_byvote(hnlist):#whenever sort by dctionary use lambda and give column name
    return sorted(hnlist, key =lambda l:l['votes'], reverse = True)


def create_custom(links,subtext):
    hn=[]
    for dx,item in enumerate(links):
        title = links[dx].getText()
        href = links[dx].get('href', None)
        vote = subtext[dx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',''))
            if points>99:
                hn.append({'title': title, 'link': href,'votes': points})  #hn.append(href)
    return sort_stories_byvote(hn)

pprint.pprint(create_custom(links, subtext))
        

"""
url = 'https://news.ycombinator.com/'
res = requests.get(url)

# print(res)    # Response 200 menas everything is good
# print(res.text)    
# this will have the entire html data in it. Exactly the same thing which we get when we click 'View Page Source'

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)
# this will also have the exact same thing as res.text, but it will keep in html format, and not in string format,
# and it will be easier to manupulate it

# print(soup.body)
# print(soup.body.contents)    # result comes in a 'list' in this case. But not with the previous cases.

# print(soup.find_all('div'))
# print(soup.find_all('a'))    # find all the 'a' tags - all the links
# print(soup.title)
# print(soup.a)     # it finds the first a tag
# print(soup.find('a'))    # it finds the first a tag

# print(soup.find(id="score_24273602"))
# print(soup.select("#score_24273602"))   # outputs in a list
# select grabs the data using a CSS selector, where '.' means 'class', '#' means 'id', etc.

# print(soup.select('a')[0])    
# grabs all the 'a' tags, and print only the first one, as this is a list, and we want the 0th item

# print(soup.select(".score")[0])# grabs all the class="score" tags

link = soup.select(".storylink")
# <a class="storylink" href="https://www.bbc.com/news/world-africa-53887947">Africa declared free of wild polio</a>
 
subtext = soup.select(".subtext")
# <span class="score" id="score_24273602">1061 points</span>

li = []

for i in range(len(link)):
    news_link = link[i].get("href", None)    # if the link is not there, the value will be taken as None
    news_title = link[i].getText()
    votes = subtext[i].select(".score")
    if len(votes):
        score = votes[0].getText().split(' ')[0]
    else:
        score = 0
        
    if int(score) > 100:
        li.append((news_title, news_link, int(score)))

li.sort(key = lambda x:x[2], reverse=True)
# li = sorted(li, key =lambda x:x[2], reverse=True)    # same as that of above

pprint.pprint(li)

"""















