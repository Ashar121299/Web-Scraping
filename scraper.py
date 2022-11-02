import requests
from bs4 import BeautifulSoup



URL='https://en.wikipedia.org/wiki/History_of_Mexico/'


#print(soup)

#all = soup.find_all(class_="noprint")
#print(len(all))

def get_citations_needed_count(url):
    '''
    takes in a url string and returns an integer
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation=soup.find_all("sup",class_='noprint')
    print(len(citation))
get_citations_needed_count(URL)

def get_citations_needed_report(url):
    '''
    takes in a url string and returns a report string
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    All=soup.find_all(class_="noprint")

    for p in All:
        print(p.parent.text)
get_citations_needed_report(URL)