from sport import sport
from industry import industry
from news_eco import news_eco
from news_dsal import news_dsal
from news_icm import news_icm


if __name__ == "__main__":
    data_sport = sport()          # 體發局
    data_industry = industry()    # 旅遊局

    #return long list
    data_eco = news_eco()           # 經濟局
    data_dsal = news_dsal()         # 勞工事務局
    data_icm = news_icm()           # 文化局 

    data_list = [data_sport, data_industry, data_eco, data_dsal, data_icm]

    for i in data_list:
        if i[0] == '':
            continue
        else:
            print(i)
