import os
import sys

Path = "./data/tinydata/"
filelist = os.listdir(Path)
sys.stdout = open("./code/result.txt", "a")
for i in filelist:
    if i.endswith(".txt"):  # You could also add "and i.startswith('f')
        #print(i)
        os.system("python code/main.py " + i + " < " + Path + i)
        
        
sys.stdout.close()


