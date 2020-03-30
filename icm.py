# from requests_html import HTMLSession

# session = HTMLSession()

# r = session.get(link)

# r.html.render()

from data_scrapy import d_scrapy

def icm():
    link = 'https://www.icm.gov.mo/cn/news/'
    item = d_scrapy(link, '#newslist')
    
    for i in item:
        print(i.text)

if __name__ == "__main__":
    icm()