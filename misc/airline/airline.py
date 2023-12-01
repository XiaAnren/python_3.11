import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeat
import shapely.geometry as sgeom
import cartopy.io.shapereader as shapereader
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter  # 导入Cartopy专门提供的经纬度的Formatter

shp_path = '/public/data/shps/CHN_adm1.shp'  # 切记路径一定要英文，血的教训！！！

fig  = plt.figure(figsize=(6,6))  # 创建画布
proj = ccrs.PlateCarree()  # 创建投影，选择cartopy的默认投影
ax   = fig.subplots(1, 1, subplot_kw={'projection': proj})  # 子图
extent = [109.5, 120, 34.5, 45]  # 限定绘图范围

china_map = cfeat.ShapelyFeature(shapereader.Reader(shp_path).geometries(), proj, edgecolor='k', facecolor='none')
ax.add_feature(china_map, linewidth=1)  # 添加读取的数据，设置线宽
ax.set_extent(extent, crs=proj)

# ax.add_geometries(shapereader.Reader(shp_path).geometries(), crs=proj, #facecolor='none',edgecolor='k',linewidth=1)
# ax.set_extent(extent, crs=proj)

# x_extent = list(range(111, 120, 2))  # 经纬度范围,#直接使用(-180,-120,-60,0,60,120,180)会异常，需要写成(0, 60, 120, 180, 240, 300, 360)的形式
# y_extent = list(range(36, 45, 2))

ax.add_feature(cfeat.LAND)  # 添加陆地
ax.add_feature(cfeat.OCEAN)  # 添加海洋
# ax.set_xticks(x_extent, crs=ccrs.PlateCarree())  # 添加经纬度
# ax.set_yticks(y_extent, crs=ccrs.PlateCarree())

# 利用Formatter格式化刻度标签
# lon_formatter = LongitudeFormatter(zero_direction_label=False)
# lat_formatter = LatitudeFormatter()
# ax.xaxis.set_major_formatter(lon_formatter)
# ax.yaxis.set_major_formatter(lat_formatter)

# ax.gridlines(linestyle='--')  # 添加网格，线样式为'--'
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')
# ax.tick_params(color = 'blue', direction='in')  # 更改刻度指向为朝内，颜色设置为蓝色

# 绘制飞行轨迹
with open('20210616_wrf_airline') as txtfile:
    fileline = txtfile.readlines()

for index in range(len(fileline) - 1):
    line1 = fileline[index].split(' ')
    line2 = fileline[index + 1].split(' ')
    point_1 = line1[6], line1[7]
    point_2 = line2[6], line2[7]
    ax.add_geometries([sgeom.LineString([point_1,point_2])], crs=ccrs.PlateCarree(), linewidth = 1, edgecolor='red')

plt.savefig('airline', bbox_inches='tight')


