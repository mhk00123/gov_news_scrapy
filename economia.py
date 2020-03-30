from data_scrapy import d_scrapy

def economia():
    link = 'https://www.economia.gov.mo/zh_TW/web/public/pg_nc_wn'

    item = d_scrapy(link,'')

    print(item)

if __name__ == "__main__":
    economia()