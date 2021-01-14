from bs4 import BeautifulSoup
import os
import requests

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


def scrap():
    print("Scrapping")
    URL = "https://www.wp.pl/"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
if __name__ == "__main__":
    scrap()