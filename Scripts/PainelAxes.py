import numpy as N
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from cartopy.util import add_cyclic_point
import cartopy.crs as ccrs
import cartopy.feature
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER

fig = plt.figure(figsize=[20, 12])
meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for month in range(1, 5):
    mes = meses[month-1]
    data = Dataset(f'/Users/Pedro/Documents/temperatura2020{mes}.nc')
    temp = data.variables['air'][0]
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    cyclic_data, cyclic_lons = add_cyclic_point(temp, coord=lon)
    ax = plt.subplot(2, 2, month, projection=ccrs.PlateCarree())
    ax_contour = plt.contourf(cyclic_lons, lat, cyclic_data, N.arange(-10., 11, 1), cmap='RdBu_r')
    ax_title = plt.title(f'Anomalia de temperatura 2020/{mes}', pad=7.)
    ax_coastlines = ax.coastlines()
    ax_gridlines = ax.gridlines(draw_labels=True)

# plt.savefig('/Users/Pedro/Documents/teste1.png')
plt.show()