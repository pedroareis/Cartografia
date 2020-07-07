import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as N
from cartopy.util import add_cyclic_point
import matplotlib

import cartopy.crs as ccrs

#map = Basemap(projection='cyl',llcrnrlat=-45,urcrnrlat=-20,\
#llcrnrlon=-70,urcrnrlon=-35,resolution='c',area_thresh=1000)


#parallels = N.arange(-90.,90.,1.)
#map.drawparallels(parallels,color='0.3',zorder=1,linewidth=0.7)
#parallels = N.arange(-90.,90.,5.)
#map.drawparallels(parallels,labels=[1,0,0,0],fontsize=14,color='0.3',zorder=1,linewidth=1.5)
#meridians = N.arange(-180.,180.,1.)
#map.drawmeridians(meridians,color='0.3',zorder=1,linewidth=0.7)
#meridians = N.arange(-180.,180.,5.)
#map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=14,color='0.3',zorder=1,linewidth=1.5)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

lon = [-52.40, -50.22, -49.19, -48.46, -47.95, -46.69, -45.82, -44.98, -43.45]
lat = [-29.38, -30.56, -31.68,-32.66, -33.44, -34.33, -34.86, -35.01, -34.78]
lon2 = [-52.40, -50.22, -49.19, -48.46, -47.95, -46.69, -45.82, -44.98, -43.45]
lat2 = [-29.38, -30.56, -31.68,-32.66, -33.44, -34.33, -34.86, -35.01, -34.78]
lon3 = -54.40
lat3 = -29.38
lon4 = -43.45
lat4 = -32.78
#lon5 = -56.5
#lat5 = -25
#lon6 = -53
#lat6 = -34
#lon7 = -48
#lat7 = -34.5
#lon8 = -57.5
#lat8 = -25
x,y = ax(lon, lat)

plt.annotate('30/06 - 12 UTC - 999 hPa', xy=(lon3,lat3), color='k', fontsize=15, fontweight='bold',
             bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 5})
plt.annotate('01/07 - 12 UTC - 972 hPa', xy=(lon4,lat4), color='k', fontsize=15, fontweight='bold',
             bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 5})
#plt.annotate('10/26 - 09 UTC - 1007 hPa', xy=(lon5,lat5), color='k', fontsize=15, fontweight='bold',
#             bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 5})

map.plot(x, y, linestyle='--',color='k')
map.plot(lon8,lat8, 'ko', markersize=16 )
map.plot(x, y, 'yo', markersize=13)
map.plot(lon6,lat6, 'ko', markersize=16 )
map.plot(lon7,lat7, 'ko', markersize=16 )
map.plot(lon2,lat2, 'ro', markersize=13 )

ax.coastlines()
ax.gridlines(draw_labels=True)
plt.figure(figsize=(10,10))

#map.shadedrelief()
#map.drawmapboundary()
#plt.savefig('SouthAmerica.png', dpi=300)
#plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.show()


