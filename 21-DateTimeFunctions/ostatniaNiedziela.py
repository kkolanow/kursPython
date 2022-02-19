import datetime

def isSameMonth(month, date):
    return date.month == month


this_month = datetime.date.today().month
 
sunday = datetime.datetime.today()
while(sunday.isoweekday() != 7):
    sunday = datetime.timedelta(days=1) + sunday


this_month = sunday.month



print(this_month)

while isSameMonth(this_month,sunday + datetime.timedelta(days=7)):
    sunday = sunday + datetime.timedelta(days=7)

print(sunday)

