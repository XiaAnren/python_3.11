import os
import pandas as pd

os.chdir('/public/home/XiaAnRen/data3/vscode/python_3.11/csv')

# 任意的多组列表
a = [1, 2, 3]
b = [4, 5, 6]

# 字典中的key值即为csv中列名
write = pd.DataFrame({'data_a' : a, 'data_b' : b})

# 将DataFrame存储为csv，index表示是否显示行名，default=True
write.to_csv('test.csv', index=False, sep=',')
