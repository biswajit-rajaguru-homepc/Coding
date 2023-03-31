import subprocess as sb
import time
import datetime

while True:
    with open("temprature.log","a") as logfile:
        sb.run(["sensors"])
