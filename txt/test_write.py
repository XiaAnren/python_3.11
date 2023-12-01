import os

os.chdir('/public/home/XiaAnRen/data3/vscode/python_3.11/txt')

with open('write_txt', 'w', encoding='UTF-8') as txt:
    data = [1, 2]
    data = map(lambda x: '{}\t'.format(x), data)
    txt.writelines(data)


with open('write_txt', 'r', encoding='UTF-8') as txt:
    print(txt.readlines())
