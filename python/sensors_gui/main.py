#!/usr/bin/python -u

# # subprocess.popen

# import subprocess
# from time import sleep

# mycmd = [
#     'timer.py',
#     '5'
# ]

# with subprocess.Popen(mycmd,stdout = subprocess.PIPE) as process:
#     print(process);
#     # def poll_and_read():
#     #     print(f'Output from poll {process.poll()}')
# #         print(f"Output from stdout {process.stdout.read().decode('utf-8')}")
        
# #     #     # return 0
#     #     # poll_and_read()
#     #     # sleep(1)
#     #     # poll_and_read()
#     #     # sleep(1)
    

# # import subprocess
# # from time import sleep

# # with subprocess.Popen(
# #     ["python", "timer.py", "5"], stdout=subprocess.PIPE
# # ) as process:

#     def poll_and_read():
#         print(f"Output from poll: {process.poll()}")
#         print(f"Output from stdout: {process.stdout.read1().decode('utf-8')}")

#     poll_and_read()
#     sleep(3)
#     poll_and_read()
#     sleep(3)
#     poll_and_read()

# popen_timer.py

# import subprocess 
# from time import sleep

# with subprocess.Popen(
#     ["python", "-u", "timer.py", "5"],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.STDOUT,
#     encoding='utf-8') as process:

#     def poll_and_read():
#         print(f"Output from poll: {process.poll()}",flush=True)
#         outs, errs = process.communicate(timeout=10)
#         print(outs,flush=True)

#     poll_and_read()
#     sleep(1)
#     poll_and_read()
#     # sleep(1)
#     # poll_and_read()
    
# import subprocess as sbp
# from time import sleep

# with sbp.Popen(
#     ["python", "-u", "timer.py", "5"], 
#     stdout=sbp.PIPE, stderr=sbp.STDOUT, 
#     encoding='utf-8') as proc:
    
#     def poll_and_read():
#         # print(f'Output from poll: {proc.poll()}', flush=True)
#         outs = proc.stdout.read1(1)
#         print(outs,end='',flush = True)
    
#     while(True):
#         sleep(0.15)
#         poll_and_read()


# popen_timer.py

import subprocess
from time import sleep

with subprocess.Popen(
    ["python", "timer.py", "5"], stdout=subprocess.PIPE
) as process:

    def poll_and_read():
        # process.stdout.seek(0)
        outs = process.stdout.read1().decode('utf-8')
        print(f"Poll:{process.poll()}\nstdout: {outs}")
        

    
    poll_and_read()
    sleep(3)
    poll_and_read()
    sleep(3)
    poll_and_read()
        
