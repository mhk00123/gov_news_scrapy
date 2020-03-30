from data_scrapy import d_scrapy

def industry():
    link = 'https://industry.macaotourism.gov.mo/cn/pressroom/index.php'

    item = d_scrapy(link, '.press_title', '')

    sp_item = item[0].text.split('\n')

    p_title = sp_item[0]
    p_time  = sp_item[1].replace('[','').replace(']','')

    r_item = [p_time, p_title]

    # print(r_item)

    return r_item

# if __name__ == "__main__":
#     industry()