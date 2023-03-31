# import subprocess as sp

# list = sp.run(["bash",'-c','ls'],encoding='utf-8',capture_output=True).stdout.strip()

# #print(list.split())

# for file in list.split():
#     new_name = input(f'{file} -> ').strip()
#     if (new_name)


from pathlib import Path

for file in Path().iterdir():
    if file.is_file():
        new_name = input(f'rename {file} -> ').strip()
        if new_name != '':
            file.rename(new_name)


        

     
    

    