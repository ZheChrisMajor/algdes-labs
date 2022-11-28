import os
import sys

# Script to run all files in ./data/ and store the results in a txt.
Path = "./data/"
filelist = os.listdir(Path)
sys.stdout = open("./code/result.txt", "w")
for i in filelist:
    if i.endswith(".txt"):  # You could also add "and i.startswith('f')
        os.system("python code/main.py " + i + " < " + Path + i)
               
sys.stdout.close()
