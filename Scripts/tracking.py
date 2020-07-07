import cartopy.feature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from netCDF4 import Dataset


fig = plt.figure(figsize=(10,10))

fname = Dataset('/Users/Pedro/Downloads/goes.nc')
data1 = fname.variables[]

ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([-70, -35, -20, -45])
lon = [-52.40, -50.22, -49.19, -48.46, -47.95, -46.69, -45.82, -44.98, -43.45]
lat = [-29.38, -30.56, -31.68,-32.66, -33.44, -34.33, -34.86, -35.01, -34.78]



#ax.add_feature(cartopy.feature.OCEAN)
#ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.BORDERS, linestyle=':', edgecolor='gray')
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax.coastlines()

ax.plot(-63., -29.42, 'ob', transform=ccrs.PlateCarree())

transform = ccrs.PlateCarree()._as_mpl_transform(ax)
ax.annotate('30/06 - 12 UTC - 999 hPa', xy=(-63.,-29.42), color='k', fontsize=15, fontweight='bold',
             bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 5})

#ax.annotate('Delhi', xy=(113, 40.5), xytext=(77.23, 28.61),
#            arrowprops=dict(facecolor='gray',
#                            arrowstyle="simple",
#                            connectionstyle="arc3,rad=-0.2",
#                            alpha=0.5),
#            xycoords=transform,
#            ha='right', va='top')
ax.gridlines(draw_labels=True)
plt.show()