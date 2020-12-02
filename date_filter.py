from datetime import datetime


def date_filter():
    end_date = '2020-12-16 10:00'
    end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
    now_date = datetime.now().strftime('%Y-%m-%d %H:%M')
    now_date = datetime.strptime(now_date, '%Y-%m-%d %H:%M')
    return end_date, now_date
