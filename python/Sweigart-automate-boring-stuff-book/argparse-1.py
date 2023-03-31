
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the text", type=str)
# parser.add_argument("square", help="print the square of a no", type=int)
# parser.add_argument("--o1", help="Option 1", type =int)
# parser.add_argument("--verbose", help=" be more verbose-flag", action="store_true")
# args = parser.parse_args()

# #args.echo="Hello"
# print(args.verbose)
#print(" ".join([args.echo  for _ in range(3)]))

# import pathlib
# mypath=pathlib.Path(input("Directory Name: "))
# for item in mypath.iterdir():
#     print(f"{item} is a {'dir' if item.is_dir() else 'file'}")

# def generate_greeting(greeting,end):
#     return lambda name: greeting + " " + name + end

# namaskaram = generate_greeting("Namaskram",".")
# hello = generate_greeting("Hello", "!")
# name = input("Name: ")
# print(hello(name),namaskaram(name),sep='\n')

import time
def inf_seq():
    num = 0
    while(True):
        yield num
        num += 1
inf_seqv = inf_seq()
for n in inf_seqv:
    print(n, end=" ", flush=True)
    time.sleep(.1)
