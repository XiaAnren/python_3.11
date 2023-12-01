import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

os.chdir('/public/home/XiaAnRen/data3/vscode/python_3.11/plt')

# font = FontProperties(fname='/public/home/XiaAnRen/data3/vscode/python_3.11/plt/simsun.ttc')

# config = {
#     "mathtext.fontset":'stix',
#     "font.family":'serif',
#     "font.serif": ['SimSun'],
#     # "font.size": 10,			# 字号，大家自行调节
#     # 'axes.unicode_minus': False # 处理负号，即-号
# }
# rcParams.update(config)
# 载入TimesSong（下载链接中），将'filepath/TimesSong.ttf'换成你自己的文件路径
# SimSun = FontProperties(fname='/public/home/XiaAnRen/data3/vscode/python_3.11/plt/SunTimes.ttf')

import numpy as np
x = np.linspace(0, 10, 1000)
# 作图
plt.figure(dpi = 200)
plt.plot(x, np.sin(x), label=u"宋 - 1")
plt.plot(x, np.cos(x), label=u"宋 - 2")
# 测试
plt.legend()
plt.title(u'宋体 title')		  # 中英文测试
plt.xlabel(u'宋体 xlabel')
plt.ylabel('$y_{label}$')	  # 公式测试
plt.text(3, 0.5, u"test")

plt.title(r'宋体 Times New Roman $\mathrm{Times \; New \; Roman}\/\/ \alpha_i > \beta_i$')
# plt.axis('off')
plt.savefig("font.png")
