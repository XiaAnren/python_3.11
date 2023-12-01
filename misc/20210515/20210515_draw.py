import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

os.chdir('/public/home/XiaAnRen/data3/vscode/python_3.11/misc/20210515')

minutes_emis_to_evaluation = 2
draw_timescale = 15

csv = pd.read_csv('20210515.csv')

lep_m_list = csv['lep_m']
dqc_list = csv['dqc']

# print(read.keys())
# print(read['data_a'])
# print(list(read['data_a']))

plt.plot(lep_m_list, dqc_list, linewidth=2)

plt.xlabel('agi (g/km2)', fontsize=12)  # x轴名称，字体大小
plt.ylabel('delta QC (%) after {} min'.format(str(minutes_emis_to_evaluation * draw_timescale)), fontsize=12)  # y轴名称，字体大小
plt.xticks(size=12)  # x轴坐标值，字体大小
plt.yticks(size=12)  # y轴坐标值，字体大小
# plt.margins(x=0, y=0)

ax = plt.subplot()
ax.set_xlim(0, 350)
ax.set_ylim(-35, 5)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
# ax.spines['left'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# 去除左右边框

plt.grid(axis='y')
# plt.grid()

plt.savefig('20210515.png', bbox_inches='tight')
plt.close()
