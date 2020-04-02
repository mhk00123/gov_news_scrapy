from data_scrapy import d_scrapy
import datetime

# 新聞局 - 經濟
def news_eco():
    today = datetime.date.today().strftime('%Y-%m-%d')

    link = 'https://news.gov.mo/list/zh-hant/news/%E7%B6%93%E6%BF%9F%E8%B2%A1%E6%94%BF'

    cookie = 'Cookie: fontSize=Normal; lang=zh-hant; JSESSIONID=33F457456597C9FD3D59ABE554A171C8.app02'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

    header = {
        'Cookie': cookie,
        'User-Agent': user_agent
    }

    item = d_scrapy(link, '.infoContentContainer', header)

    data_num = []
    num = 0
    temp = []
    for i in item:
        str1 = i.text.split('\n')
        if "小時前" in str1[2]:
            temp.append(str1[1])  
            temp.append(str1[0])
            temp.append(today)
            data_num.append(temp)
            temp = []
        else:
            continue

    # print(data_num)

    return data_num

# if __name__ == "__main__":
#     news_eco()