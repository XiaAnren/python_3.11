import os
import pandas as pd

os.chdir('/public/home/XiaAnRen/data3/vscode/python_3.11/csv')

read = pd.read_csv('test.csv')

print(read.keys())
print(read['data_a'])
print(list(read['data_a']))
