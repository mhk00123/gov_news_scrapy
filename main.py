from sport import sport
from industry import industry
from news import news

import datetime

if __name__ == "__main__":
    data_sport    = sport()
    data_industry = industry()
    data_news = news() #return long list

    print(data_sport)
    print(data_industry)
    print(data_news)
    
    today = datetime.date.today().strftime('%Y-%m-%d')
