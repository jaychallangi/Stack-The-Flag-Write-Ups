import datetime, pytz
import random

t = pytz.timezone('Asia/Singapore').localize(datetime.datetime(2022,9,22,9,41,17))
print(t)
seed = int(t.timestamp())
random.seed(seed)
token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
print(token)
#asertghnil