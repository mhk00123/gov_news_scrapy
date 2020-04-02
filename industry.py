from data_scrapy import d_scrapy
from date_judge import date_judge

# 旅遊局
def industry():
    link = 'https://industry.macaotourism.gov.mo/cn/pressroom/index.php'

    item = d_scrapy(link, '.press_title', '')

    sp_item = item[0].text.split('\n')

    p_title = sp_item[0]
    p_time  = sp_item[1].replace('[','').replace(']','')

    r_item = ['旅遊局', p_title, p_time ]

    # print(r_item)

    if(date_judge(p_time)):
        return r_item
    else:
        r_item = []
        return r_item