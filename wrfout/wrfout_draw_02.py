import cmaps
import numpy as np
import netCDF4 as nc
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.io.shapereader as shapereader
from wrf import getvar, ALL_TIMES
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter  # 导入Cartopy专门提供的经纬度的Formatter

shp_path = '/public/data/shps/CHN_adm1.shp'  # 切记路径一定要英文，血的教训！！！

path = '/public/home/premopr/data/CFDDA/CAMS10CASE_2023/GEJBGDRA_20210616/2021061606_air_ctrl/WRF_F/'
file = 'wrfout_d02_2021-06-16_00:00:00'
filepath = path + file

fig  = plt.figure(figsize = (8, 4.8))  # 创建画布
proj = ccrs.PlateCarree()  # 创建投影，选择cartopy的默认投影
ax   = fig.subplots(1, 1, subplot_kw = {'projection': proj})  # 子图
extent = [112, 120, 38, 43.5]  # 限定绘图范围（经纬度）

china_map = cfeature.ShapelyFeature(shapereader.Reader(shp_path).geometries(), proj, edgecolor = 'k', facecolor = 'none')
ax.add_feature(china_map, linewidth = 1)  # 添加读取的数据，设置线宽
ax.set_extent(extent, crs = proj)

# 设置坐标轴
ax.set_xticks(np.arange(113, 120, 1))
ax.set_yticks(np.arange(39, 43.5, 1))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

# 设置网格线
gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth = 1, color = 'k', alpha = 0.5, linestyle = '--')  # draw_labels = True自动添加坐标轴

# 读取nc文件
ncfile = nc.Dataset(filepath)
QCLOUD = getvar(ncfile, 'QCLOUD', timeidx = ALL_TIMES)  # timeidx = ALL_TIMES提取所有时刻的值
XLAT = getvar(ncfile, 'XLAT')
XLONG = getvar(ncfile, 'XLONG')

# 画等值线图
contourf = ax.contourf(XLONG, XLAT, QCLOUD[40, 20, :, :], 
                       levels=np.arange(0, 0.0024, 0.0003),  # colorbar范围与间隔
                       transform=ccrs.PlateCarree(), 
                       cmap = cmaps.WhiteBlueGreenYellowRed,  # 用NCL颜色映射表
                       extend = 'both')  # 控制colorbar两端是否允许扩充，扩充后生成尖角，可选择的变量有'neither','both', 'min', 'max'。需要注意，该参数不仅是生成尖角，填色亦会出现变化。
cbar = fig.colorbar(contourf, orientation='vertical',  # orientation='vertical' / 'horizontal'（垂直 / 水平）
                    pad=0.03, aspect=20, shrink=0.8)  # pad：与子图距离；aspect：长宽比例；shrink：收缩比例

ax.set_title('Cloud water mixing ratio (kg kg-1)')
plt.suptitle('wrfout_d02_2021-06-16_00:00:00', fontsize = 18)

plt.savefig('wrfout_draw_02', bbox_inches='tight')
