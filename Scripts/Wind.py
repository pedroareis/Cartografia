import matplotlib.pyplot as plt
from netCDF4 import Dataset
import cartopy.crs as ccrs
import numpy as N
import cartopy.feature as cfeature

u = Dataset('/Users/Pedro/Documents/DadosNC/u10_1019.nc')
v = Dataset('/Users/Pedro/Documents/DadosNC/v10_1019.nc')

uwind = u.variables['uwnd'][0]
vwind = v.variables['vwnd'][0]
lat = u.variables['lat'][:]
lon = u.variables['lon'][:]
speed = N.sqrt(uwind**2 + vwind**2)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, edgecolor='k')
ax.add_feature(cfeature.OCEAN, color='w', edgecolor='k')
ax.set_extent([-80, -30, -75, 15])
ax_cf = ax.streamplot(lon, lat, uwind, vwind, density=20)
plt.show()

