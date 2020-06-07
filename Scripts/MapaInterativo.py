import ipywidgets
from IPython.core.display import display
from ipywidgets import Layout
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

land = ipywidgets.Checkbox(description='land', style={'description_width': 'initial'})
ocean = ipywidgets.Checkbox(description='ocean', style={'description_width': 'initial'})
coastline = ipywidgets.Checkbox(description='coastline', style={'description_width': 'initial'})
rivers = ipywidgets.Checkbox(description='rivers', style={'description_width': 'initial'})
boarders = ipywidgets.Checkbox(description='boarders', style={'description_width': 'initial'})
lakes = ipywidgets.Checkbox(description='lakes', style={'description_width': 'initial'})
locations = ipywidgets.Checkbox(description='locations', style={'description_width': 'initial'})

box_layout = Layout(display='inline-flex',
                    flex_flow='row',
                    align_items='stretch',
                    border='solid',
                    width='100%')

ui = ipywidgets.HBox([land, ocean, coastline, rivers, boarders, lakes, locations], layout=box_layout)

def create_map(land, ocean, coastline, rivers, boarders, lakes, locations):
    data_crs = ccrs.PlateCarree()
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1, projection=data_crs)
    ax.set_global()
    if land == True: ax.add_feature(cfeature.LAND)
    if ocean == True: ax.add_feature(cfeature.OCEAN)
    if coastline == True: ax.add_feature(cfeature.COASTLINE)
    if rivers == True: ax.add_feature(cfeature.RIVERS)
    if boarders == True: ax.add_feature(cfeature.BORDERS)
    if lakes == True: ax.add_feature(cfeature.LAKES)
    if locations == True:
        poa_lon, poa_lat = -51.2177, -30.0346
        ax.plot(poa_lon, poa_lat, 'ro', transform=data_crs)
        ax.text(poa_lon - 2, poa_lat - 4, 'Porto Alegre', horizontalaligment='right', transform=data_crs)

out = ipywidgets.interactive_output(create_map, {'land': land,
                                                 'ocean': ocean,
                                                 'coastline': coastline,
                                                 'boarders': boarders,
                                                 'lakes': lakes,
                                                 'rivers': rivers,
                                                 'locations': locations})

display(ui, out)
