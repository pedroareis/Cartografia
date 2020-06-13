import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as N
from cartopy.util import add_cyclic_point
import matplotlib

import cartopy.crs as ccrs

data = Dataset('/Users/Pedro/Documents/temperatura202001.nc')
temp = data.variables['air'][0]
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
add_cyclic_data, add_cyclic_lon = add_cyclic_point(temp, coord=lon)

ax = plt.axes(projection=ccrs.PlateCarree())
ax_cf = ax.contourf(add_cyclic_lon, lat, add_cyclic_data, N.arange(-8., 8.1, 1), cmap='RdBu_r')
ax_cb = plt.colorbar(ax_cf, fraction=0.046, pad=0.04, orientation='horizontal', label='oC')
ax.coastlines()
ax.gridlines(draw_labels=True)
plt.figure(figsize=(10,10))
plt.show()