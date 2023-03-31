#!/usr/bin/python
import subprocess

mycmd = [
    'learn_subprocess.py',
    '5'    
]

mycmd1 = [
    'python',
    'magic_number.py'
]

mycmd3 = [
    'reaction_game.py'
]
# (['learn_subprocess.py', '10'])
#subprocess.run(mycmd, timeout=4)
# try:
#     subprocess.run(mycmd)

# except FileNotFoundError as exc:
#     print(f'can\'t find executable {mycmd[0]}\n')

# except subprocess.CalledProcessError as exc:
#     print(f'Process failed with return code {exc.returncode}\n',)

# except subprocess.TimeoutExpired as exc:
#     print('\n Process timed out\n')

# def ten():
#     return 10
# a = {
#     'a':'10',
#     'b':'10'
# }

# class dummy():
#     """docstring for dummy."""
#     def __init__(self):
#         self.v=11
    
# p1 = dummy()  

# a = sum( int(subprocess.run(mycmd1,capture_output=True).stdout) for _ in range(10))
# print(a)

# b = sum(int(subprocess.run(mycmd1,capture_output=True,encoding='utf-8').stdout) for _ in range(2))
# print(b)

# a = subprocess.run(mycmd3,encoding='utf-8', input='\n\n')

from tempfile import TemporaryFile

with TemporaryFile() as f:
    subprocess.run('sensors',encoding='utf-8',stdout=f)
    f.seek(0)
    result = subprocess.run('cat', stdin=f,stdout=subprocess.PIPE,encoding='utf-8').stdout

print(result).