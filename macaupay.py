from requests_html import HTMLSession

url = 'https://etc.macaupay.com.mo/Ml-Pt/realname_pc/#/cardInquiry'

session = HTMLSession()

r = session.get(url)

result = r.html.render()

print(result)