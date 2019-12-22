import os
print(os.environ.get('PYTHONPATH'))
# output
# D:\Workspace\Python

import sys
print(sys.path)
# output
# ['D:\\Workspace\\Python\\snippets', 'D:\\Workspace\\Python', 'C:\\Users\\Ashok\\Anaconda3\\envs\\Python\\python37.zip', 'C:\\Users\\Ashok\\Anaconda3\\envs\\Python\\DLLs', 'C:\\Users\\Ashok\\Anaconda3\\envs\\Python\\lib', 'C:\\Users\\Ashok\\Anaconda3\\envs\\Python', 'C:\\Users\\Ashok\\Anaconda3\\envs\\Python\\lib\\site-packages']


# info: sys.path is a list, so you can add other packages for lookup just the way you add to list data structure


