import os
import time


tmp = os.popen("pmset -g batt").read()
raw_data = tmp.split(";")[0]
percentage = raw_data[len(raw_data)-4:].strip()[:2]
print(percentage)
