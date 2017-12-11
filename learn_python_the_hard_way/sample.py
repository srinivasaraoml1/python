# sample program to test pip installation, requests, beautifulsoup

import requests

from bs4 import BeautifulSoup

def make_soup(html_string):
       return BeautifulSoup(html_string, 'html.parser')

def main():
    url = "http://news.google.co.in"
    data = requests.get(url)
    soup = make_soup(data.text)
    #print(soup.prettify())

    lida = soup.find_all("a")
    for d in lida:
        print(d.string, d["href"])

        # if "Donald Trump" in d.string:
        #     print(d["href"])
        # if "news" in d["href"]:
        #     print(d.string)



main()
