import matplotlib.pyplot as plt
from netCDF4 import Dataset

import cartopy.crs as ccrs

data = Dataset('/Users/Pedro/Documents/temperatura202001.nc')
temp = data.variables['air'][0]
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]


ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat, temp, vmin=-5, vmax=5, cbar_kwargs={'shrink':0.4})
ax.coastlines()
ax.gridlines()

plt.show()