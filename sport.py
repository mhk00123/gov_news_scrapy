from data_scrapy import d_scrapy
from date_judge import date_judge

# 體發局
def sport():
    link = 'https://www.sport.gov.mo/zh/news'

    item = d_scrapy(link, '.newslist', '')
    
    sp_item = item[0].text.split('\n')

    p_time = sp_item[0][0:10]
    p_title  = sp_item[0][10:]

    r_item = [p_time, p_title, '體發局']

    # print(r_item)
    if(date_judge(p_time)):
        return r_item
    else:
        r_item = []
        return r_item

# if __name__ == "__main__":
#     sport()