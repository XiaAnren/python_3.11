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
minutes_emis_to_evaluation = 2
emis_rate = 1.2
emis_rate_step = 2.4
dx = 2000
iZ = 27
RE = 1
draw_timescale = 15
agi_r = 1.69e-5

rho_agi = 5.683
v_agi = 4 * np.pi * pow(agi_r, 3) / 3
m_agi = 1e6 * rho_agi * v_agi
area = dx * dx
# e_m = emis_rate * dt * (idt_emis_e - idt_emis_s + 1) / 1e6
# e_m = area * e_m
# e_n = emis_rate * dt * (idt_emis_e - idt_emis_s + 1) / m_agi
# e_n = area * e_n
# e_nm = e_n / e_m
nkm = (RE * 2 + 1) * (RE * 2 + 1) * (dx / 1000) * (dx / 1000)
iZ = iZ - 1
mt = minutes_emis_to_evaluation

ctrlname = '../wrfout_d01_2021-05-15_00:00:00.ctrl'
ctrlfile = nc.Dataset(ctrlname)
QC_get = getvar(ctrlfile, 'QCLOUD', timeidx = ALL_TIMES) * 1000  # g kg^-1
QC = np.mean(QC_get[t_emis, iZ, j_emis - RE : j_emis + RE + 1, i_emis - RE : i_emis + RE + 1])  # ctrl的QC值

lep_m_list = []
dqc_list = []

for filename in os.listdir():
# for filename in ['wrfout_d01_2021-05-15_00:00:00.exp_0727.0050']:
    print(filename)
    ncfile = nc.Dataset(filename)

    qc_get = getvar(ncfile, 'QCLOUD', timeidx = ALL_TIMES) * 1000
    z_get = getvar(ncfile, 'z', timeidx = ALL_TIMES)
    # tc_get        = wrf_user_getvar(a,"tc",-1)
    rh_get = getvar(ncfile, 'rh', timeidx = ALL_TIMES)
    # wa_get        = wrf_user_getvar(a,"wa",-1)
    # p_get         = wrf_user_getvar(a,"pressure",-1)
    TK = getvar(ncfile, 'tk', timeidx = ALL_TIMES)
    # Q             = wrf_user_getvar(a,"QVAPOR",-1)
    PRES = getvar(ncfile, 'pressure', timeidx = ALL_TIMES) * 100
    RD = 287
    ES = 6.112 * np.exp(17.67 * (TK - 273.15) / (TK - 29.65))
    E = ES * rh_get
    rho_get = (PRES / 1000) * (1000 / RD) * (1 / TK) * (1 - 0.378 * E / PRES)
    NAGIAER_get = getvar(ncfile, 'NAGIAER', timeidx = ALL_TIMES)
    AGIAER_get = getvar(ncfile, 'AGIAER', timeidx = ALL_TIMES)
    # qv_get        = wrf_user_getvar(a,"QVAPOR",-1)*1000
    # qc_get        = wrf_user_getvar(a,"QCLOUD",-1)*1000
    # qi_get        = wrf_user_getvar(a,"QICE",-1)*1000
    # qs_get        = wrf_user_getvar(a,"QSNOW",-1)*1000
    # qr_get        = wrf_user_getvar(a,"QRAIN",-1)*1000
    # qg_get        = wrf_user_getvar(a,"QGRAUP",-1)*1000
    ACNDEP_get = getvar(ncfile, 'ACNDEP', timeidx = ALL_TIMES)
    ACNCDF_get = getvar(ncfile, 'ACNCDF', timeidx = ALL_TIMES)
    ACNIMF_get = getvar(ncfile, 'ACNIMF', timeidx = ALL_TIMES)
    ACNCTF_get = getvar(ncfile, 'ACNCTF', timeidx = ALL_TIMES)
    ACNIMD_get = getvar(ncfile, 'ACNIMD', timeidx = ALL_TIMES)
    ACNICE_get = ACNDEP_get + ACNCDF_get + ACNIMF_get + ACNCTF_get

    agim = 0
    for j in range(j_emis - RE, j_emis + RE + 1):
        for i in range(i_emis - RE, i_emis + RE + 1):
            rhom  = rho_get[t_eva, iZ, j, i]
            AGIAER = AGIAER_get[t_eva, iZ, j, i]
            dz2  = 0.5 * (z_get[t_eva, iZ + 1, j, i] - z_get[t_eva, iZ - 1, j, i])
            ve   = area * dz2
            local2= (ACNICE_get[t_eva, iZ, j, i] + ACNIMD_get[t_eva, iZ, j, i]) / (NAGIAER_get[t_eva, iZ, j, i] + 1)
            agim = (local2 + 1) * AGIAER * ve * rhom / 1e6 + agim
    lep_m = agim / nkm
    lep_m_list.append(lep_m.data)

    qc1 = qc_get[t_eva, iZ, j_emis - RE : j_emis + RE + 1, i_emis - RE : i_emis + RE + 1]
    qc2 = QC_get[t_eva, iZ, j_emis - RE : j_emis + RE + 1, i_emis - RE : i_emis + RE + 1]
    dqc = np.mean((qc1 - qc2) / mt)
    if QC >= 0:
        accdqc = 100 * (dqc * mt * draw_timescale) / QC
    else:
        accdqc = 0 * dqc
    dqc_list.append(accdqc.data)

    emis_rate += emis_rate_step
    # print(emis_rate)

# 字典中的key值即为csv中列名
csv = pd.DataFrame({'lep_m' : lep_m_list, 'dqc' : dqc_list})

# 将DataFrame存储为csv，index表示是否显示行名，default=True
csv.to_csv('/public/home/XiaAnRen/data3/vscode/python_3.11/misc/20210515/20210515.csv', index=False, sep=',')
