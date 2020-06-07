import numpy as N
import matplotlib.pyplot as plt
from netCDF4 import Dataset

import cartopy.crs as ccrs
import cartopy.feature

data = Dataset('/Users/Pedro/Documents/temperatura202001.nc')
temp = data.variables['air'][0]
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]


fig = plt.figure(figsize=[10, 5])
ax1 = plt.subplot(1, 2, 1, projection=ccrs.PlateCarree())
plt.contourf(lon, lat, temp, 20)
plt.title('Mapa 1')

ax2 = plt.subplot(1, 2, 2, projection=ccrs.PlateCarree(),
                  sharex=ax1, sharey=ax1)
plt.contourf(lon, lat, temp, 20)
plt.title('Mapa 2')

ax1.add_feature(cartopy.feature.LAND)
ax2.add_feature(cartopy.feature.LAND)
ax1.add_feature(cartopy.feature.OCEAN)
ax2.add_feature(cartopy.feature.OCEAN)

ax1.gridlines()
ax2.gridlines()

#plt.savefig('/Users/Pedro/Documents/teste1.png')
plt.show()