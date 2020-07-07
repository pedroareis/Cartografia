
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy import feature
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.mpl.ticker as cticker

nc = Dataset('/Users/Pedro/Downloads/20200701.nc')

pmnn = nc.variables['PRMSL_L101'][2]
pmnnhpa = pmnn / 100

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-65, -30, -15, -45])
ax.coastlines()
ax.gridlines()
countries = ax.add_feature(feature.BORDERS)
ocean = ax.add_feature(feature.OCEAN)
land = ax.add_feature(feature.LAND)

ax.set_xticks([-60, -55, -50, -45, -40, -35, -30], crs=ccrs.PlateCarree())
ax.set_xticklabels([-60, -55, -50, -45, -40, -35, -30])
ax.set_yticks([-45, -40, -35, -30, -25, -20, -15], crs=ccrs.PlateCarree())
ax.set_yticklabels([-45, -40, -35, -30, -25, -20, -15])
ax.yaxis.tick_left()

lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.grid(linewidth=2, color='black', alpha=0.5, linestyle='--')




CS = plt.contour(lon,lat,pmnnhpa,np.arange(960,1046,2),colors='k')
plt.clabel(CS, inline=1,fmt='%1.f', fontsize=10)

plt.title('MSLP (hPa)\n2020.07.01 - 12:00 UTC',fontsize=12)
plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.savefig('MSLP2020070112.png', dpi=300)
plt.show()