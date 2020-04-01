from requests_html import HTMLSession
import time 
def d_scrapy(url, target, hd): #link, CSS Selector, header
    try:
        session = HTMLSession()
        r = session.get(url, headers = hd)
        time.sleep(2)
        r.html.render(timeout=4, sleep=2)
        item = r.html.find(target)
        r.close()
    except:
        r.close()
        r_item = ['']
        return r_item
    else:
        r.close()
        return item