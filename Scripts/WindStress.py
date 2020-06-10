import numpy as N
import cartopy.crs as ccrs
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from global_land_mask import globe
import cartopy.feature as cfeature
from cartopy.util import add_cyclic_point

u10 = Dataset('/Users/Pedro/Documents/DadosNC/u10_8090.nc')
v10 = Dataset('/Users/Pedro/Documents/DadosNC/v10_8090.nc')

u10w = u10.variables['uwnd'][0]
v10w = v10.variables['vwnd'][0]

lat = u10.variables['lat'][:]
lon = u10.variables['lon'][:]
lat_grid, lon_grid = N.meshgrid(lat, lon)
is_on_land = globe.is_land(lat_grid, lon_grid-180)

wind_speed = N.hypot(u10w, v10w)
Pair = 1.22
CD = 0.0013
t = CD * wind_speed

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-75, 20, -75, 10])
cyclic_t, cyclic_lon = add_cyclic_point(t, coord=lon)
ax_cf = plt.contourf(cyclic_lon, lat, cyclic_t, 20, cmap='RdBu_r')
plt.colorbar(ax_cf, orientation='horizontal', shrink=0.8, pad=.09, label='Pa')
ax_q = ax.quiver(lon, lat, u10w, v10w)
ax_T = plt.title('Mean Wind Stress\n1980-90')
ax.gridlines()
ax.coastlines()

plt.savefig('/Users/Pedro/Documents/DadosNC/teste.png', dpi=300)
plt.show()