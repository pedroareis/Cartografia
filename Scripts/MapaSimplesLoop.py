import numpy as N
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point
from netCDF4 import Dataset

meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for month in range(1, 5):
    mes = meses[month-1]
    data = Dataset(f'/Users/Pedro/Documents/temperatura2020{mes}.nc')
    temp = data.variables['air'][0]
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    cyclic_data, cyclic_lons = add_cyclic_point(temp, coord=lon)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax_contour = plt.contourf(cyclic_lons, lat, cyclic_data, N.arange(-10., 11, 1), cmap='RdBu_r')
    ax_title = plt.title(f'Anomalia de temperatura 2020/{mes}')
    ax_coastilines = ax.coastlines()
    ax_gridlines = ax.gridlines(draw_labels=True)
    plt.savefig(f'/Users/Pedro/Documents/MeusProjetosPython/temp_anomaly_2020{mes}.png', dpi=300)
