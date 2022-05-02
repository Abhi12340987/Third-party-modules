import time
import os
import pandas

while True:
    if os.path.exists("Third party modules/original.csv"):
        data = pandas.read_csv("Third party modules/original.csv")
        print(data.mean())
    
    else:
        print("File does not exist")
    
    time.sleep(5)


import sys
sys.builtin_module_names #print out all built-in modules