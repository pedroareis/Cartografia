import numpy as np
from netCDF4 import Dataset
from datetime import datetime, timedelta
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

file = Dataset('/Users/Pedro/Downloads/goes.nc')
data = file.variables['CMI'][:, :] - 273.15
sat_h = file.variables['goes_imager_projection'].perspective_point_height
x = file.variables['x'][:] * sat_h
y = file.variables['y'][:] * sat_h
img_extent = (x.min(), x.max(), y.min(), y.max())

plt.figure(figsize=(10, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-222., 10., -90., 90.], crs=ccrs.PlateCarree())

ax.stock_img()

img = ax.imshow(data, vmin=-80, vmax=40, origin='upper', extent=img_extent, cmap='Greys',
                transform=ccrs.Geostationary(central_longitude=-75.0, satellite_height=35786023.0))

plt.colorbar(img, label='Brightness Temperatures (°C)', extend='both', orientation='horizontal',
             pad=0.05, fraction=0.05)

plt.savefig('/Users/Pedro/Documents/ImageGOES.png')
plt.show()
