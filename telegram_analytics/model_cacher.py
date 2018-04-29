from models.telegram_members_model import TelegramMembers

from utils.timeit import timeit
from utils.schedule_logger import with_logging

from datetime import datetime
from time import sleep, time

dates = list(reversed(TelegramMembers.getAllDates()))

for date in dates:
    print(date)
hours = 4
start = dates[0]
end = dates[-1]
df = TelegramMembers.getDataBetweenDateRange(start, end)
print(start)
print(end)
interval = end-start
print(f'interval:{interval}')
# df.to_pickle('one_hour.cache')
