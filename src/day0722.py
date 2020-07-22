import sys
import time
import datetime

print(sys.path)
print(sys.version)
print(sys.argv)
print('time-------')
# time.sleep(2)
print(time.time())
t = time.time()
day = time.ctime(t)
print(day)
print(time.localtime(t))
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print('datetime-----')
print(datetime.time.hour)
# p176