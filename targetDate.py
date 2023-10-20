from datetime import datetime, timedelta

def date_nb_days(a0, a, p):
    days = 0
    daily_rate = p / 36000
    while a0 < a:
        a0 += a0 * daily_rate
        days += 1
    date = datetime(2016, 1, 1) + timedelta(days=days)
    return date.strftime('%Y-%m-%d')

print(date_nb_days(100, 101, 0.98))
