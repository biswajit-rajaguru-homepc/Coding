#!/usr/bin/python

import subprocess as sb
from datetime import datetime

def log_uptime():
    home = sb.run(["bash",'-c','echo $HOME'],encoding='utf-8',capture_output=True).stdout.strip()
    uptime = sb.run(["bash", '-c', "uptime -p"], encoding='utf-8', capture_output=True).stdout.strip()
    logfile_name = home+r'/mylogs/uptime_log'
    now = datetime.now().strftime('Date: %d %m %Y, Time: %H %M %S, ')
# sb.run(['bash', '-c', 'mkdir -p $HOME/logs'])
# with open(logfile_name,'a+') as logfile:
    # logfile.write()
    data_line = now + 'Session: '+uptime[3:]+'\n'
#print(f'{data_line}')

    sb.run(['bash', '-c', 'mkdir -p $HOME/mylogs'])
    with open(logfile_name,'a+') as f:
        f.write(data_line)



