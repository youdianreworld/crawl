#coding:utf-8
import urllib2
import urllib
import requests
from bs4 import BeautifulSoup

url = "https://bbs.hupu.com"
proxy = {'http':'http://10.22.98.21:8080'}

def has_href_and_id(tag):
    return tag.has_attr("href") and tag.has_attr("id")

def get(url):
    content = requests.get(url, proxies=proxy).content
    return BeautifulSoup(content)

def parseTitle(content): 
    p_title = content.find_all("td","p_title")
    a_list = [i.find_all(has_href_and_id)[0] for i in p_title]
    href_text = [(a.get("href"), a.get_text().encode("gbk","ignore")) for a in a_list]
    with open("text","wb") as file:
        for k,v in href_text:
            file.write(k+v+"\n")
    return href_text


def parseWord(content):
    c = content.find_all("div", class_="quote-content")
    with open("word","wb") as f:
        for i in c:
            f.write(i.get_text().encode("utf-8"))
name = "/cavaliers"
content = get(url+name)
href_text = parseTitle(content)
count = 0
for href, text in href_text:
    parseWord(get(url+href))
    count = count + 1
    if count > 5:
        break
    
