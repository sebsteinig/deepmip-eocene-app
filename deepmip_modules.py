import numpy as np
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from cartopy.util import add_cyclic_point
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cmocean

def get_paleo_location_herold(modern_lat, modern_lon):

    # open Herold et al. (2014) rotation file
    rotation_file = xr.open_dataset('data/LatLon_PD_55Ma_Herold2014.nc') 
    # 1. coarse approximation: look up paleolocation for modern coordinates in rotation file
    paleo_lat = rotation_file.LAT.sel(latitude=modern_lat, longitude=modern_lon, method='nearest').values
    paleo_lon = rotation_file.LON.sel(latitude=modern_lat, longitude=modern_lon, method='nearest').values
    # 2. fine approximation: add delta between modern selected and rotation grid coordinates back to paleolocation
    delta_lat = modern_lat - rotation_file.latitude.sel(latitude=modern_lat, method='nearest').values
    delta_lon = modern_lon - rotation_file.longitude.sel(longitude=modern_lon, method='nearest').values
    paleo_lat += delta_lat
    paleo_lon += delta_lon

    # build dictionary iteratively and convert to dataframe
    d = []
    # for count,lat in enumerate(modern_lat):
    #     d.append(
    #         {
    #             'modern lat': lat,
    #             'modern lon': modern_lon,
    #             'Eocene (55Ma) lat': paleo_lat,
    #             'Eocene (55Ma) lon': paleo_lon,
    #         }
    #     )

    d.append(
        {
            'modern lat': modern_lat,
            'modern lon': modern_lon,
            'Eocene (55Ma) lat': paleo_lat,
            'Eocene (55Ma) lon': paleo_lon,
        }
    )

    df = pd.DataFrame(d)

    # return DataFrame    
    return df

def plot_paleogeography(df, projection):
    ### plot Eocene paleogeography with rotated site(s)
    
    # open Herold et al. (2014) paleogeography
    # cyclic longitude for contourf plot was added with cdo (cdo sethalo,1,0)
    # for better performance, but can also be added in Python with:
    # geography, lonsc = add_cyclic_point(ds_herold.topo, ds_herold.lon)
    ds_herold = xr.open_dataset('data/herold_etal_eocene_topo_1x1.halo.nc')


    # add cyclic longitude for plotting
    

    if projection == "global":
        proj =ccrs.PlateCarree()
    elif projection == "ortho":
        proj =ccrs.Orthographic()

    # plot global map
    fig, ax = plt.subplots(1, subplot_kw=dict(projection=proj))
    # fig, ax = plt.subplots(1)

    # cf1 = ax.contourf(lonsc, lats, geography, cmap='cmo.topo', levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())

    ds_herold.topo.plot(
        ax=ax, 
        cmap='cmo.topo', 
        levels=21, 
        vmin=-5000, 
        vmax=5000, 
        transform=ccrs.PlateCarree(),
        extend='both',
        cbar_kwargs={'orientation': 'horizontal', 'label': 'surface elevation [m]', 'pad': 0.1})
    # add modern coastlines for comparison
    # ax.coastlines(color='gray')

    # add axis tick labels
    # ax.set_xticks([-180,-120, -60, 0, 60, 120, 180], crs=ccrs.PlateCarree())
    # ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    # ax.xaxis.set_major_formatter(LongitudeFormatter())
    # ax.yaxis.set_major_formatter(LatitudeFormatter())

    ax.set_xlabel('')
    ax.set_ylabel('')

    # ax.set(title = '55Ma paleolocation: LAT = ' + str(np.round(df['Eocene (55Ma) lat'], 1)) + ', LON = ' + str(np.round(df['Eocene (55Ma) lon'], 1)) , xlabel='', ylabel='')

    # plot orthographic ma with site in center
    # ax2 = plt.subplot(gs[1], projection=ccrs.Orthographic(paleoLon, paleoLat))
    # ax2 = plt.subplot(gs[1], projection=ccrs.Orthographic(0, 0))
    # # ax2.contourf(lonsc, lats, geography, levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())
    # ax2.contourf(lonsc, lats, geography, cmap='cmo.topo', levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())
    # ax2.coastlines()

    # add site marker at paleolocation
    # ax.plot(df['modern lon'], df['modern lat'], 'ro', markersize=8, markerfacecolor='none', markeredgecolor='r', transform=ccrs.PlateCarree())
    # ax.plot(df['Eocene (55Ma) lon'], df['Eocene (55Ma) lat'], 'ro', markersize=8, markeredgecolor='black', transform=ccrs.PlateCarree())
    # # if siteName != '':
    #     if (paleoLon > -100):
    #         labelLon = paleoLon-5
    #         labelAlignment = 'right'
    #     else:
    #         labelLon = paleoLon+5
    #         labelAlignment = 'left'        
    #     ax1.text(labelLon, paleoLat-15, siteName, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=12, transform=ccrs.PlateCarree())
    #     ax2.text(labelLon, paleoLat-10, siteName, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=12, transform=ccrs.PlateCarree())

    # add common colorbar
    # cbar_ax = fig1.add_axes([0.15, 0.05, 0.7, 0.05])
    # cb = plt.colorbar(cf1, cax=cbar_ax, orientation='horizontal', extend='both')
    # cb.set_label('surface elevation [m]', size=12)
    # plt.tight_layout()

    return fig