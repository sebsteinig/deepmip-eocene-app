import numpy as np
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from cartopy.util import add_cyclic_point
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from pathlib import Path

from DeepMIP_model_dict import model_dict

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
    # ds_herold = xr.open_dataset('data/herold_etal_eocene_topo_1x1.r180x90.halo.nc')


    # add cyclic longitude for plotting
    

    if projection == "global":
        proj =ccrs.PlateCarree()
    elif projection == "ortho":
        proj =ccrs.Orthographic()

    # plot global map
    fig, ax = plt.subplots(1, subplot_kw=dict(projection=proj))
    # fig, ax = plt.subplots(1)

    # cf1 = ax.contourf(lonsc, lats, geography, cmap='cmo.topo', levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())

    ds_herold.topo.plot.contourf(
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
    ax.set_xticks([-180,-120, -60, 0, 60, 120, 180], crs=ccrs.PlateCarree())
    ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.yaxis.set_major_formatter(LatitudeFormatter())

    ax.set_xlabel('')
    ax.set_ylabel('')

    # ax.set(title = '55Ma paleolocation: LAT = ' + str(np.round(df['Eocene (55Ma) lat'], 1)) + ', LON = ' + str(np.round(df['Eocene (55Ma) lon'], 1)) , xlabel='', ylabel='')

    # plot orthographic ma with site in center
    # ax2 = plt.subplot(gs[1], projection=ccrs.Orthographic(paleo_lon, paleo_lat))
    # ax2 = plt.subplot(gs[1], projection=ccrs.Orthographic(0, 0))
    # # ax2.contourf(lonsc, lats, geography, levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())
    # ax2.contourf(lonsc, lats, geography, cmap='cmo.topo', levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())
    # ax2.coastlines()

    # add site marker at paleolocation
    ax.plot(df['modern lon'], df['modern lat'], 'ro', markersize=8, markerfacecolor='none', markeredgecolor='r', transform=ccrs.PlateCarree())
    ax.plot(df['Eocene (55Ma) lon'], df['Eocene (55Ma) lat'], 'ro', markersize=8, markeredgecolor='black', transform=ccrs.PlateCarree())
    # # if siteName != '':
    #     if (paleo_lon > -100):
    #         labelLon = paleo_lon-5
    #         labelAlignment = 'right'
    #     else:
    #         labelLon = paleo_lon+5
    #         labelAlignment = 'left'        
    #     ax1.text(labelLon, paleo_lat-15, siteName, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=12, transform=ccrs.PlateCarree())
    #     ax2.text(labelLon, paleo_lat-10, siteName, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=12, transform=ccrs.PlateCarree())

    # add common colorbar
    # cbar_ax = fig1.add_axes([0.15, 0.05, 0.7, 0.05])
    # cb = plt.colorbar(cf1, cax=cbar_ax, orientation='horizontal', extend='both')
    # cb.set_label('surface elevation [m]', size=12)
    # plt.tight_layout()

    return fig

def get_model_point_data(df_input, variable):

    # allocate empty list to store results for all models
    data_list = []

    expts = ['piControl', 'deepmip_sens_1xCO2', 'deepmip_sens_2xCO2', 'deepmip_stand_3xCO2', 'deepmip_sens_4xCO2', 'deepmip_stand_6xCO2', 'deepmip_sens_9xCO2']
    expt_labels = ['piControl', 'DeepMIP_1x', 'DeepMIP_2x', 'DeepMIP_3x', 'DeepMIP_4x', 'DeepMIP_6x', 'DeepMIP_9x']

    # loop over all models and experiments
    for model in model_dict.keys():
        for exp_count, exp in enumerate(expts):

            # construct filename following the DeepMIP convention
            model_file = 'data/User_Model_Database_v1.0/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                        '/' + model + '-' + exp + '-' + variable + '-' + model_dict[model]['versn'] + '.mean.nc'

            print(model_file)
            # load data if file for model/experiment combination exists
            if Path(model_file).exists():
                ds_model = xr.open_dataset(model_file, decode_times=False)

                print("found data")

                # get coordinate names
                for coord in ds_model.coords:
                    if coord in ['lat', 'latitude']:
                        lat_name = coord
                    elif coord in ['lon', 'longitude']:
                        lon_name = coord

                if exp == 'piControl':
                    lookup_lat = float(df_input['modern lat'])
                    lookup_lon = float(df_input['modern lon'])
                else:
                    lookup_lat = float(df_input['Eocene (55Ma) lat'])
                    lookup_lon = float(df_input['Eocene (55Ma) lon'])             

                # check for minimum model longitude
                min_model_lon = np.amin(ds_model.coords[lon_name].values)
                if min_model_lon >= 0.0 and lookup_lon < 0.0:
                    # convert lookup_lon from [-180:180] to [0:360]
                    lookup_lon = lookup_lon + 360.0 

                var_data = getattr(ds_model, variable)
                if variable == 'tas':
                    # convert from Kelvin to Celsius
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon}, method='nearest').values - 273.15
                elif variable == 'pr':
                    # convert from kg m-2 s-1 to mm/day
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon}, method='nearest').values * 86400.
                else:
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon}, method='nearest').values

                # store results for individual metrics in a dictionary
                data_list.append(dict(model = model, 
                                         experiment = expt_labels[exp_count], 
                                         annualMean = np.mean(site_data), 
                                         monthlyMin = np.min(site_data), 
                                         monthlyMax = np.max(site_data), 
                                         DJF = np.mean(site_data[[11,0,1]]), 
                                         MAM = np.mean(site_data[[2,3,4]]), 
                                         JJA = np.mean(site_data[[5,6,7]]), 
                                         SON = np.mean(site_data[[8,9,10]]) ))


    # convert dictionary to Pandas dataframe for easier handling and plotting  
    df = pd.DataFrame(data_list)

    print(df)

    return df