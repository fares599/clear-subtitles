#!/bin/python3
import os
import re


folder_list=os.listdir()
print(folder_list)
for folder in folder_list:
    if os.path.isdir(folder):
        content=os.listdir(folder)
        os.chdir(f'{os.getcwd()}/{folder}') 
        for file in content:
            target=re.search(".srt",file)
            execpting1=re.search("Arabic.srt",file)
            execpting2=re.search("English.srt",file)

            if target and not execpting1 and not execpting2:
                os.remove(f'{file}')

        os.chdir('..')
