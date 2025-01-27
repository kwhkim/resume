print('hello, there!')

x = 3
for i in range(x):
    print(i)

# 올해 크리스마스까지 남은 일수를 구하는 함수
from datetime import datetime
def days_until_christmas():
    today = datetime.today()
    christmas = datetime(year=today.year, month=12, day=25)
    days = (christmas - today).days
    return days

# 현재 날짜가 속한 분기를 계산하는 함수
def current_quarter():
    """
    Calculate the current quarter of the year.
    """
    month = datetime.today().month
    return (month - 1) // 3 + 1
    
    