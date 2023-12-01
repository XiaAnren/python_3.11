import os
import netCDF4 as nc
import matplotlib.pyplot as plt

os.chdir('/public/home/XiaAnRen/data3/WRF/4.1.1/WRF/run')
filename = 'wrfout_d02_2023-10-05_00:00:00'
file = nc.Dataset(filename)

# print(file.variables.keys())
'''
dict_keys(['Times', 'XLAT', 'XLONG', 'LU_INDEX', 'ZNU', 'ZNW', 'ZS', 'DZS', 'VAR_SSO', 'U', 'V', 'W', 'PH', 'PHB', 'T', 'THM', 'HFX_FORCE', 'LH_FORCE', 'TSK_FORCE', 
'HFX_FORCE_TEND', 'LH_FORCE_TEND', 'TSK_FORCE_TEND', 'MU', 'MUB', 'NEST_POS', 'P', 'PB', 'FNM', 'FNP', 'RDNW', 'RDN', 'DNW', 'DN', 'CFN', 'CFN1', 'THIS_IS_AN_IDEAL_RUN', 
'P_HYD', 'Q2', 'T2', 'TH2', 'PSFC', 'U10', 'V10', 'RDX', 'RDY', 'RESM', 'ZETATOP', 'CF1', 'CF2', 'CF3', 'ITIMESTEP', 'XTIME', 'QVAPOR', 'QCLOUD', 'QRAIN', 'QICE', 'QSNOW', 
'QGRAUP', 'QNICE', 'QNRAIN', 'SHDMAX', 'SHDMIN', 'SNOALB', 'TSLB', 'SMOIS', 'SH2O', 'SEAICE', 'XICEM', 'SFROFF', 'UDROFF', 'IVGTYP', 'ISLTYP', 'VEGFRA', 'GRDFLX', 'ACGRDFLX', 
'ACSNOM', 'SNOW', 'SNOWH', 'CANWAT', 'SSTSK', 'COSZEN', 'LAI', 'DTAUX3D', 'DTAUY3D', 'DUSFCG', 'DVSFCG', 'VAR', 'CON', 'OA1', 'OA2', 'OA3', 'OA4', 'OL1', 'OL2', 'OL3', 'OL4', 
'MAPFAC_M', 'MAPFAC_U', 'MAPFAC_V', 'MAPFAC_MX', 'MAPFAC_MY', 'MAPFAC_UX', 'MAPFAC_UY', 'MAPFAC_VX', 'MF_VX_INV', 'MAPFAC_VY', 'F', 'E', 'SINALPHA', 'COSALPHA', 'HGT', 'TSK', 
'P_TOP', 'T00', 'P00', 'TLP', 'TISO', 'TLP_STRAT', 'P_STRAT', 'MAX_MSTFX', 'MAX_MSTFY', 'RAINC', 'RAINSH', 'RAINNC', 'SNOWNC', 'GRAUPELNC', 'HAILNC', 'CLDFRA', 'SWDOWN', 'GLW', 
'SWNORM', 'ACSWUPT', 'ACSWUPTC', 'ACSWDNT', 'ACSWDNTC', 'ACSWUPB', 'ACSWUPBC', 'ACSWDNB', 'ACSWDNBC', 'ACLWUPT', 'ACLWUPTC', 'ACLWDNT', 'ACLWDNTC', 'ACLWUPB', 'ACLWUPBC', 'ACLWDNB', 
'ACLWDNBC', 'SWUPT', 'SWUPTC', 'SWDNT', 'SWDNTC', 'SWUPB', 'SWUPBC', 'SWDNB', 'SWDNBC', 'LWUPT', 'LWUPTC', 'LWDNT', 'LWDNTC', 'LWUPB', 'LWUPBC', 'LWDNB', 'LWDNBC', 'OLR', 'XLAT_U', 
'XLONG_U', 'XLAT_V', 'XLONG_V', 'ALBEDO', 'CLAT', 'ALBBCK', 'EMISS', 'NOAHRES', 'TMN', 'XLAND', 'UST', 'PBLH', 'HFX', 'QFX', 'LH', 'ACHFX', 'ACLHF', 'SNOWC', 'SR', 
'SAVE_TOPO_FROM_REAL', 'ISEEDARR_SPPT', 'ISEEDARR_SKEBS', 'ISEEDARR_RAND_PERTURB', 'ISEEDARRAY_SPP_CONV', 'ISEEDARRAY_SPP_PBL', 'ISEEDARRAY_SPP_LSM', 'C1H', 'C2H', 'C1F', 'C2F', 
'C3H', 'C4H', 'C3F', 'C4F', 'PCB', 'PC', 'LANDMASK', 'LAKEMASK', 'SST', 'SST_INPUT'])
'''

time = (file.variables['Times'][:])
QR = (file.variables['QRAIN'][:])
lat = (file.variables['XLAT'][:])
lon = (file.variables['XLONG'][:])

# 查看数据经纬度范围，纬度（latitude）12.470451~35.95028，经度（longitude）104.18975~126.328225
# 格点分辨率为0.5度

# # plt对某个doy的全球sif值作图。左半部分为西半球，右边是东半球
# # 选了doy为10的sif数据作图

plt.contourf(lon[0, :, :], lat[0, :, :], QR[0, 0, :, :])
plt.colorbar(label="QRAIN", orientation="horizontal")
plt.savefig('result2.png', bbox_inches='tight')



