# This program monitors the battery percentage status of the mac
# It notifies as low battery if the percentage is at 20 while usage
# It notifies the user to unplug charger while the percentage is at 80 while charging

# Sample output report to be refined:
#   Now drawing from 'AC Power'
#    -InternalBattery-0 (id=3145827)	67%; charging; 1:21 remaining present: true

import os
import time

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

def battery_percentage():
    tmp = os.popen("pmset -g batt").read()
    raw_data = tmp.split(";")[0]
    percentage = raw_data[len(raw_data)-4:].strip()[:2]
    return percentage

def main():
    while True :
        tmp = battery_percentage()
        print(tmp)
        if int(tmp)<=20:
            notify(title    = 'Battery Status Notification',
                subtitle = 'with python',
                message  = 'Low battery, Plug charger')
            break
        elif int(tmp)>80:
            notify(title    = 'Battery Status Notification',
                subtitle = 'with python',
                message  = 'Unplug charger')
            break
        else:
            time.sleep(3)
            continue

main()
