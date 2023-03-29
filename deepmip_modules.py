import numpy as np
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cmocean
import seaborn as sns
import holoviews as hv
from holoviews import opts

from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from pathlib import Path

from deepmip_dicts import exp_dict, model_dict, variable_dict

hv.extension('bokeh')

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

def get_model_point_data(modern_lat, modern_lon, paleo_lat, paleo_lon, variable):

    # allocate empty list to store results for all models
    data_list = []


    # loop over all models and experiments
    for exp in exp_dict.keys():
        for model in model_dict.keys():

            # construct filename following the DeepMIP convention
            model_file = 'data/User_Model_Database_v1.0/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                        '/' + model + '-' + exp + '-' + variable + '-' + model_dict[model]['versn'] + '.mean.nc'

            # load data if file for model/experiment combination exists
            if Path(model_file).exists():
                ds_model = xr.open_dataset(model_file, decode_times=False)

                # get coordinate names
                for coord in ds_model.coords:
                    if coord in ['lat', 'latitude']:
                        lat_name = coord
                    elif coord in ['lon', 'longitude']:
                        lon_name = coord

                if exp == 'piControl':
                    lookup_lat = modern_lat
                    lookup_lon = modern_lon
                else:
                    lookup_lat = paleo_lat
                    lookup_lon = paleo_lon            

                # check for minimum model longitude
                min_model_lon = np.amin(ds_model.coords[lon_name].values)
                if min_model_lon >= 0.0 and lookup_lon < 0.0:
                    # convert lookup_lon from [-180:180] to [0:360]
                    lookup_lon = lookup_lon + 360.0 

                var_data = getattr(ds_model, variable)
                if variable == 'tas':
                    # convert from Kelvin to Celsius
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon}, method='nearest').values - 273.15
                    unit = '°C'
                elif variable == 'pr':
                    # convert from kg m-2 s-1 to mm/day
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon}, method='nearest').values * 86400.
                    unit = 'mm/day'
                else:
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon}, method='nearest').values
                    unit = variable_dict[variable]['unit']
                # store results for individual metrics in a dictionary
                data_list.append(dict(  model_short = model_dict[model]['abbrv'], 
                                        model = model,
                                        experiment = exp_dict[exp]['medium_name'], 
                                        CO2 = float(exp_dict[exp]['CO2']), 
                                        lat = np.round(lookup_lat, 2),
                                        lon = np.round(lookup_lon,2),
                                        var = variable,
                                        unit = unit,
                                        annual_mean = np.mean(site_data), 
                                        monthly_min = np.min(site_data), 
                                        monthly_max = np.max(site_data), 
                                        DJF = np.mean(site_data[[11,0,1]]), 
                                        MAM = np.mean(site_data[[2,3,4]]), 
                                        JJA = np.mean(site_data[[5,6,7]]), 
                                        SON = np.mean(site_data[[8,9,10]]),
                                        Jan = site_data[0],
                                        Feb = site_data[1],
                                        Mar = site_data[2],
                                        Apr = site_data[3],
                                        May = site_data[4],
                                        Jun = site_data[5],
                                        Jul = site_data[6],
                                        Aug = site_data[7],
                                        Sep = site_data[8],
                                        Oct = site_data[9],
                                        Nov = site_data[10],
                                        Dec = site_data[11] ))

    # convert dictionary to Pandas dataframe for easier handling and plotting  
    df = pd.DataFrame(data_list).round(1)

    # calculate ensemble mean for each site and experiment
    for exp in exp_dict.keys():  
        df.loc[len(df)] = df.loc[(df['experiment'] == exp_dict[exp]['medium_name'])].mean(numeric_only=True)
        # set ensemble mean metadata
        df.loc[len(df)-1,'model'] = 'ensemble_mean'
        df.loc[len(df)-1,'experiment'] = exp_dict[exp]['medium_name']
        df.loc[len(df)-1,'var'] = variable
        df.loc[len(df)-1,'unit'] = variable_dict[variable]['unit']

    return df

def location_data_boxplot(df, variable):

    df_plot = df[(df.model != 'ensemble_mean')]

    # change dataframe from wide (9 columns) to long (3 columns) format to use hue method in seaborn boxplot
    dfMelt = pd.melt(df_plot, id_vars=['experiment'], value_vars=['annual_mean','monthly_min','monthly_min','monthly_max','DJF','MAM','JJA','SON'])
    
    # define figure layout first
    fig, axes = plt.subplots(2, 1, figsize=(13, 16))

    # generate list of medium-length experiment anmes for plot ordering
    list_medium_names = []
    for key, value in exp_dict.items():
        list_medium_names.append(value['medium_name'])

    # boxplot with seaborn (https://seaborn.pydata.org/generated/seaborn.boxplot.html)
    ax3 = sns.boxplot(data=dfMelt, x="experiment", y="value", hue='variable', hue_order=['annual_mean', 'monthly_min', 'monthly_max'], order=list_medium_names, palette = ['tab:green','tab:blue','tab:red'], linewidth=2.0, ax=axes[0])
    ax3 = sns.swarmplot(data=dfMelt, x="experiment", y="value", hue='variable', hue_order=['annual_mean', 'monthly_min', 'monthly_max'], order=list_medium_names, palette = ['tab:green','tab:blue','tab:red'], linewidth=1.5, edgecolor='black', size=5, dodge=True, ax=axes[0])

    ax4 = sns.boxplot(data=dfMelt, x="experiment", y="value", hue='variable', hue_order=['DJF', 'MAM', 'JJA', 'SON'], palette = ['tab:blue', 'tab:orange', 'tab:green','tab:red'], linewidth=2.0, ax=axes[1])
    ax4 = sns.swarmplot(data=dfMelt, x="experiment", y="value", hue='variable', hue_order=['DJF', 'MAM', 'JJA', 'SON'], palette = ['tab:blue', 'tab:orange', 'tab:green','tab:red'], linewidth=1.5, edgecolor='black', size=5, dodge=True, ax=axes[1])

    # add optional proxy estimates as reference
    # if (showProxy):
    #     if proxyMin != '':
    #         ax3.axhline(proxyMin, ls='--', color='lightcoral', zorder=0.)
    #         ax4.axhline(proxyMin, ls='--', color='lightcoral', zorder=0.)
    #     if proxyMax != '':
    #         ax3.axhline(proxyMax, ls='--', color='lightcoral', zorder=0.)
    #         ax4.axhline(proxyMax, ls='--', color='lightcoral', zorder=0.) 
    #     if proxyMin != '' and proxyMax != '':
    #         ax3.axhspan(proxyMin, proxyMax, facecolor='lightcoral', alpha=0.4, zorder=0.)
    #         ax4.axhspan(proxyMin, proxyMax, facecolor='lightcoral', alpha=0.4, zorder=0.)
    #         ax3.text(0.5, proxyMax, proxyLabel, color='lightcoral', verticalalignment='bottom')
    #         ax4.text(0.5, proxyMax, proxyLabel, color='lightcoral', verticalalignment='bottom')


    # modify legends and axes
    # if (siteName != ''):
    #     titleString = 'DeepMIP ' + deepmipVariableDict[variable]['longname'] + ' for "' + siteName + '": LAT = ' + str(np.round(paleoLat, 1)) + ', LON = ' + str(np.round(paleoLon, 1)) 
    # else:
    #     titleString = 'DeepMIP ' + deepmipVariableDict[variable]['longname'] + ' at: LAT = ' + str(np.round(paleoLat, 1)) + ', LON = ' + str(np.round(paleoLon, 1)) 
    titleString = 'DeepMIP ' + variable_dict[variable]['longname']

    yLabel = variable_dict[variable]['label']

    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles[0:3], labels[0:3], fontsize='16');
    ax3.set(title = titleString, xlabel='', ylabel=yLabel);
    [ax3.axvline(x, color = 'gray', linestyle='-', linewidth=0.5, zorder=0.) for x in [0.5,1.5,2.5,3.5,4.5,5.5,6.5]]

    handles2, labels2 = ax4.get_legend_handles_labels()
    ax4.legend(handles2[0:4], labels2[0:4], fontsize='16');
    ax4.set(title = titleString, xlabel='', ylabel=yLabel);
    [ax4.axvline(x, color = 'gray', linestyle='-', linewidth=0.5, zorder=0.) for x in [0.5,1.5,2.5,3.5,4.5,5.5,6.5]]

    # plt.tight_layout()
    # plt.show()

    return fig

def box_whisker_plot(df, metric):

    df_plot = df[(df.model != 'ensemble_mean')]
    dfEocene = df_plot.loc[df_plot['experiment'] != 'piControl']

        # generate list of medium-length experiment anmes for plot ordering
    list_medium_names = []
    for key, value in exp_dict.items():
        list_medium_names.append(value['medium_name'])

    # box = hv.BoxWhisker(dfEocene,
    #                      kdims=['CO2'],
    #                      vdims=[metric]
    #                     ).opts(
    #                     opts.BoxWhisker(logx=True,box_color='white', width=940, height=400, show_legend=False, whisker_color='black',box_fill_color='#63c5da')
    #                     )

    scatter = hv.Scatter(dfEocene,
                     kdims=['CO2'],
                     vdims=[metric, 'model_short','annual_mean']
                    ).redim.values(**{'experiment':list_medium_names}
                    ).groupby(
                        'model_short'
                    ).overlay(
                    ).opts(
                        opts.Scatter(
                                logx=True,
                                jitter=0.2,
                                width=705, 
                                height=400, 
                                show_legend=True, 
                                legend_position='top', 
                                # legend_offset=(0, 119), 
                                size=12, 
                                tools=['hover', 'wheel_zoom'], 
                                line_color='black', 
                                fontsize={'legend': 10.8})) 
    
    # composition = box * scatter
    composition = scatter


    return composition
