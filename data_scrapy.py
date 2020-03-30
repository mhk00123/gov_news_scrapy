from requests_html import HTMLSession

def d_scrapy(url, target, hd):
    session = HTMLSession()
    r = session.get(url, headers = hd)
    r.html.render(timeout=4, sleep=2)
    item = r.html.find(target)
    r.close()
    
    return item