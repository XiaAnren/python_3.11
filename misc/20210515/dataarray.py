import os
import numpy as np
import pandas as pd
import netCDF4 as nc
from wrf import getvar, ALL_TIMES

os.chdir('/public/home/XiaAnRen/20210515/expset_x105y95t0/exp_07/exp_0727')

dt = 20
idt_emis_s = 207
idt_emis_e = 208
i_emis = 20
j_emis = 17
t_emis = 69
t_eva = 71
emis_rate = 1.2
emis_rate_step = 2.4
dx = 2000
iZ = 27
RE = 1
iZ = iZ - 1

ctrlname = '../wrfout_d01_2021-05-15_00:00:00.ctrl'
ctrlfile = nc.Dataset(ctrlname)
QC_get = getvar(ctrlfile, 'QCLOUD', timeidx = ALL_TIMES) * 1000  # g kg^-1
# QC = np.mean(QC_get[t_emis, iZ, j_emis - RE : j_emis + RE + 1, i_emis - RE : i_emis + RE + 1])

QC_print = QC_get[t_emis, iZ, j_emis - RE : j_emis + RE + 1, i_emis - RE : i_emis + RE + 1].mean()

print(QC_print)
print()
print(type(QC_print))

