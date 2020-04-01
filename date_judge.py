import datetime

def date_judge(j_date):
    today = datetime.date.today().strftime('%Y-%m-%d')
    if(j_date is today):
        return True
    else:
        return False