import datetime
from decimal import Decimal


goods = {}
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = datetime.datetime.strptime(
        expiration_date, 
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    items[title].append(
    {'amount': amount, 'expiration_date': expiration_date}
    )


def add_by_note(items, note):
    parts = str.split(note, ' ')
    if len(parts[-1].split('-')) == 3:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = str.join(' ', parts[0:-2])
        add(items, title, amount, expiration_date)
    else:
        amount = Decimal(parts[-1])
        title = str.join(' ', parts[0:-1])
        add(items, title, amount)


def find(items, needle):
    found = []
    keys = list(items.keys())
    for title in keys:
        if title.lower().find(needle.lower()) > -1:
            found.append(title)
    return found


def get_amount(items, needle): 
    value = Decimal('0')
    for found in find(items, needle):
        for title in items[found]:
            for amount in title.values():
                if type(amount) == Decimal:
                    value += amount
    return value


def get_expired(items, in_advance_days=0):
    # today = datetime.date.today()
    # today = datetime.date(2023, 12, 10)
    expired = []
    today = datetime.date.today()
    for title in items.keys():
        end_list = [title, Decimal(0)]        
        for i in range(len(items[title])):
            date = items[title][i]['expiration_date']            
            if type(date) == datetime.date:                
                if date - today <= datetime.timedelta(days=in_advance_days):
                    end_list[1] += items[title][i]['amount']
        if end_list[1] != Decimal(0):
            expired.append(tuple(end_list)) 
    return expired