import cmaps
import netCDF4 as nc
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.io.shapereader as shapereader
from wrf import getvar, ALL_TIMES

shp_path = '/public/data/shps/CHN_adm1.shp'  # 切记路径一定要英文，血的教训！！！

fig  = plt.figure(figsize=(6,5.5))  # 创建画布
proj = ccrs.PlateCarree()  # 创建投影，选择cartopy的默认投影
ax   = fig.subplots(1, 1, subplot_kw={'projection': proj})  # 子图
extent = [112, 120, 38, 43.5]  # 限定绘图范围（经纬度）

china_map = cfeature.ShapelyFeature(shapereader.Reader(shp_path).geometries(), proj, edgecolor='k', facecolor='none')
ax.add_feature(china_map, linewidth=1)  # 添加读取的数据，设置线宽
ax.set_extent(extent, crs=proj)

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')

path = '/public/home/premopr/data/CFDDA/CAMS10CASE_2023/GEJBGDRA_20210616/2021061606_air_ctrl/WRF_F/'
file = 'wrfout_d02_2021-06-16_00:00:00'
filepath = path + file

ncfile = nc.Dataset(filepath)
# print(ncfile.variables)
QCLOUD = getvar(ncfile, 'QCLOUD', timeidx=ALL_TIMES)
XLAT = getvar(ncfile, 'XLAT')
XLONG = getvar(ncfile, 'XLONG')

# print(QCLOUD)

contourf = ax.contourf(XLONG, XLAT, QCLOUD[40, 20, :, :]*1000, transform=ccrs.PlateCarree(), cmap = cmaps.WhiteBlueGreenYellowRed, extend = 'both')
''' 
cmap = 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 
'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 
'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 
'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 
'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 
'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 
'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 
'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 
'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 
'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 
'viridis', 'viridis_r', 'winter', 'winter_r'
'''
cbar = fig.colorbar(contourf, orientation='horizontal', pad=0.06, aspect=20, shrink=0.8)  # orientation='vertical' / 'horizontal'
# cbar.set_label('T2')

ax.set_title('Cloud water mixing ratio (10-3 kg kg-1)')
plt.suptitle('wrfout_d02_2021-06-16_00:00:00', fontsize = 18)

plt.savefig('wrfout_draw_01', bbox_inches='tight')
