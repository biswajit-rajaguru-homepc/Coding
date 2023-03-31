import datetime 
import time

while True:
    with open("logfile","a") as log:
        log.write(str(datetime.datetime.now()) + '\n')
    time.sleep(2)

