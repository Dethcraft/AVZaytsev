def filter_by_state(data, state='EXECUTED'):
    return [item for item in data if item.get('state') == state]
from datetime import datetime

def sort_by_date(data, descending=True):
    return sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=descending)

