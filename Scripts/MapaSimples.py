import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as N

import cartopy.crs as ccrs

data = Dataset('/Users/Pedro/Documents/temperatura202001.nc')
temp = data.variables['air'][0]
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]


ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat, temp, N.arange(-5., 6., 1), cmap='RdBu_r')
ax.coastlines()
ax.gridlines()

plt.show()