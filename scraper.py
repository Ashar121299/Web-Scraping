
import requests
from bs4 import BeautifulSoup
import json




URL='https://en.wikipedia.org/wiki/History_of_Mexico'


#print(soup)

#all = soup.find_all(class_="noprint")
#print(len(all))

def get_citations_needed_count(url):
    '''
    takes in a url string and returns an integer
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation=soup.find_all(class_='noprint Inline-Template Template-Fact')
    return len(citation)


def get_citations_needed_report(url):
    '''
    takes in a url string and returns a report string
    '''
    P=[]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation=soup.find_all(class_='noprint Inline-Template Template-Fact')
    f=open('citationNedded.txt','w')
    for p in citation:
        print(p.parent.text)
        f.write(p.parent.text)
        f.write('\n')
        

if __name__=='__main__':
    print(get_citations_needed_count(URL))
    get_citations_needed_report(URL)