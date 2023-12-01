import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs   
import cartopy.feature as cfeat 
from cartopy.io.shapereader import Reader  #读取自定的shp文件
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter 
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
from copy import copy
import shapely.geometry as sgeom
from wrf import getvar, interpline, CoordPair,get_cartopy, cartopy_xlim, cartopy_ylim, latlon_coords,geo_bounds
import netCDF4 as nc
import matplotlib.ticker as ticker

path = '/public/home/premopr/data/CFDDA/CAMS10CASE_2023/GEJBGDRA_20210616/2021061606_air_ctrl/WRF_F/'
filename = 'wrfout_d02_2021-06-16_00:00:00'
ncfile = nc.Dataset(path + filename)
t2 = getvar(ncfile, "T2")

t2 = t2 - 273.15

lats = getvar(ncfile, "XLAT")
lons = getvar(ncfile, "XLONG")

# 选择经纬度使其通过区域中心作为插值线
start_lat = lats[0, (lats.shape[-1]-1)//2]
end_lat = lats[-1, (lats.shape[-1]-1)//2]
start_lon = lons[0, (lons.shape[-1]-1)//2]
end_lon = lons[-1, (lons.shape[-1]-1)//2]

# 创建 CoordPairs
start_point = CoordPair(lat=start_lat, lon=start_lon)
end_point = CoordPair(lat=end_lat, lon=end_lon)

# t2_line = interpline(t2, wrfin=ncfile, start_point=start_point, end_point=end_point, latlon=True)

slp = getvar(ncfile, "slp")

# 获取 cartopy 地图对象
cart_proj = get_cartopy(slp)
print (cart_proj)

# 获取 x轴的边界数组
xlims = cartopy_xlim(slp)

# 获取y轴的边界数组
ylims = cartopy_ylim(slp)

##########################WRFout的绘制########################
proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(12,6),dpi=150)
ax1 = plt.subplot(121, projection = proj)
ax1.add_feature(cfeat.COASTLINE, linewidth=0.6, zorder=1)
ac = ax1.contourf(lons,lats,t2,levels=np.arange(12,36,3),cmap='Spectral_r',extend='both')

ax1.set_xticks(np.arange(106,120,3))
new=np.arange(106,120,3)
ax1.set_yticks(np.arange(16,30,3))
ax1.xaxis.set_major_formatter(LongitudeFormatter())
ax1.yaxis.set_major_formatter(LatitudeFormatter())
ax1.set_title('WRFout')



l,b,w,h = 0.25, 0.05, 0.5, 0.02
rect = [l,b,w,h]
cbar_ax = fig.add_axes(rect)
cb = fig.colorbar(ac, cax = cbar_ax,orientation='horizontal',spacing='proportional')
cb.set_label('temperture (deg C)')

plt.suptitle('Temperture at 2M   2020-05-21 12:00:00',fontsize=18)

fig.show
# fig.savefig('result', bbox_inches='tight')
