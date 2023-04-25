import numpy as np
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cmocean
import seaborn as sns
import holoviews as hv
from holoviews import opts
from bokeh.models import BoxAnnotation

from matplotlib.colors import BoundaryNorm
import matplotlib.colors as colors
from cartopy.util import add_cyclic_point

from pathlib import Path

from deepmip_dicts import exp_dict, model_dict, variable_dict

hv.extension('bokeh')

def get_paleo_locations(modern_lat, modern_lon):

    # models use two different paleogeographic reconstructions:
    # 1. most model use the Herold et al. (2014) reconstruction, hereafter "H14"
    # 2. NorESM1_F uses the Baatsen et al. (2016) reconstruction, hereafter "B16"

    # open both rotation files used by the models
    rotation_file_H14 = xr.open_dataset('data/LatLon_PD_55Ma_Herold2014.nc') 
    rotation_file_B16 = xr.open_dataset('data/LatLon_PD_55Ma_Baatsen2016.nc') 

    # 1. coarse approximation: look up paleolocation for modern coordinates in rotation file
    paleo_lat_H14 = rotation_file_H14.LAT.sel(latitude=modern_lat, longitude=modern_lon, method='nearest').values
    paleo_lon_H14 = rotation_file_H14.LON.sel(latitude=modern_lat, longitude=modern_lon, method='nearest').values
  
    paleo_lat_B16 = rotation_file_B16.LAT.sel(latitude=modern_lat, longitude=modern_lon, method='nearest').values
    paleo_lon_B16 = rotation_file_B16.LON.sel(latitude=modern_lat, longitude=modern_lon, method='nearest').values

    # 2. fine approximation: add delta between modern selected and rotation grid coordinates back to paleolocation
    delta_lat_H14 = modern_lat - rotation_file_H14.latitude.sel(latitude=modern_lat, method='nearest').values
    delta_lon_H14 = modern_lon - rotation_file_H14.longitude.sel(longitude=modern_lon, method='nearest').values
    paleo_lat_H14 += delta_lat_H14
    paleo_lon_H14 += delta_lon_H14

    delta_lat_B16 = modern_lat - rotation_file_H14.latitude.sel(latitude=modern_lat, method='nearest').values
    delta_lon_B16 = modern_lon - rotation_file_H14.longitude.sel(longitude=modern_lon, method='nearest').values
    paleo_lat_B16 += delta_lat_B16
    paleo_lon_B16 += delta_lon_B16

    # build dictionary iteratively and convert to dataframe
    d = []
    d.append(
        {
            'modern lat': modern_lat,
            'modern lon': modern_lon,
            'Eocene (55Ma) lat H14': paleo_lat_H14,
            'Eocene (55Ma) lon H14': paleo_lon_H14,
            'Eocene (55Ma) lat B16': paleo_lat_B16,
            'Eocene (55Ma) lon B16': paleo_lon_B16,
        }
    )

    df = pd.DataFrame(d)

    # return DataFrame    
    return df

# def get_model_point_data(modern_lat, modern_lon, paleo_lat, paleo_lon, variable):
def get_model_point_data(df, variable):

    # allocate empty list to store results for all models
    data_list = []

    # loop over all models and experiments
    for exp in exp_dict.keys():
        for model in model_dict.keys():

            # construct filename following the DeepMIP convention
            if variable == "tos":
                model_file = 'data/data_for_DeepMIP_app/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                            '/' + model + '-' + exp + '-' + variable + '-' + model_dict[model]['versn'] + '.mean.r180x90.filled.nc'
            else:
                model_file = 'data/data_for_DeepMIP_app/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                            '/' + model + '-' + exp + '-' + variable + '-' + model_dict[model]['versn'] + '.mean.r180x90.nc'    
                            
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
                    lookup_lat = float(df['modern lat'])
                    lookup_lon = float(df['modern lon'])
                else:
                    lookup_lat = float(df['Eocene (55Ma) lat ' + model_dict[model]['rotation']])
                    lookup_lon = float(df['Eocene (55Ma) lon ' + model_dict[model]['rotation']])            



                # check for minimum model longitude
                min_model_lon = np.amin(ds_model.coords[lon_name].values)
                if min_model_lon >= 0.0 and lookup_lon < 0.0:
                    # convert lookup_lon from [-180:180] to [0:360]
                    lookup_lon_model = lookup_lon + 360.0 
                else:
                    lookup_lon_model = lookup_lon


                var_data = getattr(ds_model, variable)
                if variable == 'tas':
                    # convert from Kelvin to Celsius
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon_model}, method='nearest').values - 273.15
                    unit = '°C'
                elif variable == 'pr':
                    # convert from kg m-2 s-1 to mm/day
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon_model}, method='nearest').values * 86400.
                    unit = 'mm/day'
                else:
                    site_data = var_data.sel(**{lat_name: lookup_lat}, **{lon_name: lookup_lon_model}, method='nearest').values
                    unit = variable_dict[variable]['unit']

                # get GMST
                exp_list = model_dict[model]['exps']
                gmst_list = model_dict[model]['gmst']

                # check vailable model experiments against full list
                for count, model_exp in enumerate(exp_list):
                    if model_exp == exp:
                        gmst = gmst_list[count]

                # store results for individual metrics in a dictionary
                data_list.append(dict(  model_short = model_dict[model]['abbrv'], 
                                        model = model,
                                        experiment = exp_dict[exp]['medium_name'], 
                                        CO2 = float(exp_dict[exp]['CO2']),
                                        GMST = gmst,  
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
        df.loc[len(df)-1,'model_short'] = 'mean'
        df.loc[len(df)-1,'experiment'] = exp_dict[exp]['medium_name']
        df.loc[len(df)-1,'var'] = variable
        df.loc[len(df)-1,'unit'] = unit


    return df.round(1)

def location_data_boxplot(df, proxy_flag, proxy_mean, proxy_std, proxy_label ):

    df_plot = df[(df.model != 'ensemble_mean')]

    # get paleolocation
    df_Eocene = df_plot.loc[df_plot['experiment'] != 'piControl']
    plat = df_Eocene.iloc[0]['lat']
    plon = df_Eocene.iloc[0]['lon']

    variable = df_plot.iloc[0]['var']

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

    #add optional proxy estimates as reference
    if proxy_flag:
        if proxy_std != '':
            ax3.axhspan(proxy_mean - proxy_std, proxy_mean + proxy_std, facecolor='lightcoral', alpha=0.4, zorder=0.)
            ax4.axhspan(proxy_mean - proxy_std, proxy_mean + proxy_std, facecolor='lightcoral', alpha=0.4, zorder=0.)
            ax3.text(1.5, proxy_mean + proxy_std, proxy_label, fontsize=20, color='lightcoral', verticalalignment='bottom')
            ax4.text(1.5, proxy_mean + proxy_std, proxy_label, fontsize=20, color='lightcoral', verticalalignment='bottom')


    # modify legends and axes
    # if (siteName != ''):
    #     titleString = 'DeepMIP ' + deepmipVariableDict[variable]['longname'] + ' for "' + siteName + '": LAT = ' + str(np.round(paleoLat, 1)) + ', LON = ' + str(np.round(paleoLon, 1)) 
    # else:
    #     titleString = 'DeepMIP ' + deepmipVariableDict[variable]['longname'] + ' at: LAT = ' + str(np.round(paleoLat, 1)) + ', LON = ' + str(np.round(paleoLon, 1)) 
    titleString = 'DeepMIP (~55 Ma) ' + variable_dict[variable]['longname']+ ' (LAT = ' + str(np.round(plat, 1)) + ' / LON = ' + str(np.round(plon, 1)) + ')' 

    yLabel = variable_dict[variable]['longname'] + ' [' + df.iloc[0]['unit'] + ']'

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

def box_whisker_plot(df, var_y, var_x, proxy_check, proxy_mean, proxy_std, proxy_label):

    df_plot = df[(df.model != 'ensemble_mean')]

    # get paleolocation
    df_Eocene = df_plot.loc[df_plot['experiment'] != 'piControl']
    plat = df_Eocene.iloc[0]['lat']
    plon = df_Eocene.iloc[0]['lon']

    if var_x == "experiment":
        df_redcued = df_plot
        log_x = False
    elif var_x == "CO2":
        log_x = True
        df_redcued = df_plot.loc[df_plot['experiment'] != 'piControl']
    elif var_x == "GMST":
        log_x = False
        df_redcued = df_plot.loc[df_plot['experiment'] != 'piControl']   

    x_label='tes'   
        # generate list of medium-length experiment anmes for plot ordering
    list_medium_names = []
    for key, value in exp_dict.items():
        list_medium_names.append(value['medium_name'])

    # add proxy reference annotation
    if proxy_check:
        hspan  = hv.HSpan(proxy_mean - proxy_std, proxy_mean + proxy_std).opts(
                    opts.HSpan(color='lightcoral', alpha=0.4))
        
        if var_x == "experiment":
            text_x = 'DeepMIP_1x'
        elif var_x == "CO2":
            text_x = 500           
        elif var_x == "GMST":
            text_x = 20        

        htext  = hv.Text(text_x, proxy_mean + 1.2 * proxy_std, proxy_label).opts(
                    opts.Text(color='lightcoral'))
        
    scatter = hv.Scatter(df_redcued,
                     kdims=[var_x],
                     vdims=[var_y, 'model_short'],
                    ).redim.values(**{'experiment':list_medium_names}
                    ).groupby(
                        'model_short'
                    ).overlay(
                    ).opts(
                        opts.Scatter(
                                logx=log_x,
                                xlabel=var_x,
                                ylabel=var_y,
                                jitter=0.2,
                                width=705, 
                                height=400, 
                                show_legend=True, 
                                legend_position='top', 
                                size=12, 
                                tools=['hover', 'wheel_zoom'], 
                                line_color='black', 
                                fontsize={'legend': 10.8})) 
    

    if var_x == "experiment":

        box = hv.BoxWhisker(df_redcued,
                            kdims=[var_x],
                            vdims=[var_y]
                            ).opts(
                            opts.BoxWhisker(
                                    logx=log_x,
                                    box_color='white',
                                    width=705, 
                                    height=400, 
                                    show_legend=False, 
                                    whisker_color='black',
                                    box_fill_color='#63c5da')
                            )
    
        if proxy_check:
            composition = hspan * box * scatter * htext
        else:
            composition = box * scatter
          


    else:

        line = hv.Curve(df_redcued,
                        kdims=[var_x],
                        vdims=[var_y, 'model_short']
                        ).redim.values(**{'experiment':list_medium_names}
                        ).groupby(
                            'model_short'
                        ).overlay(
                        ).opts(
                            opts.Scatter(
                                    size=12)) 

        if proxy_check:
            composition =  hspan * htext * line * scatter
        else:
            composition =  scatter * line          


    return composition

def plot_global_paleogeography(df, projection, proxy_label, outline_colour, grid_check, labels_check):
    ### plot Eocene paleogeography with rotated site(s)
    
    # open Herold et al. (2014) paleogeography
    # cyclic longitude for contourf plot was added with cdo (cdo sethalo,1,0)
    # for better performance, but can also be added in Python with:
    # geography, lonsc = add_cyclic_point(ds_herold.topo, ds_herold.lon)
    ds_herold = xr.open_dataset('data/herold_etal_eocene_topo_1x1.halo.nc')
    # ds_herold = xr.open_dataset('data/herold_etal_eocene_topo_1x1.r180x90.halo.nc')


    # add cyclic longitude for plotting
    

    if projection == "Equirectangular":
        proj =ccrs.PlateCarree()
        cbar_orientation = 'horizontal'
        cbar_pad = 0.1
    elif projection == "Robinson":
        proj =ccrs.Robinson(central_longitude=0)
        cbar_orientation = 'horizontal'
        cbar_pad = 0.1
    elif projection == "Orthographic":
        proj =ccrs.Orthographic(central_longitude=float(df['Eocene (55Ma) lon H14']), central_latitude= float(df['Eocene (55Ma) lat H14']))
        cbar_orientation = 'vertical'
        cbar_pad = 0.05

    # plot global map
    fig, ax = plt.subplots(1, subplot_kw=dict(projection=proj))

    # modify colors for shallow ocean and high orography slightly  
    cmap = plt.cm.get_cmap(cmocean.cm.topo)
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmaplist[106] = cmaplist[122]
    cmaplist[255] = cmaplist[245]
    cmap_mod = colors.LinearSegmentedColormap.from_list('mcm',cmaplist, cmap.N)
    norm = colors.TwoSlopeNorm(vmin=-6000., vcenter=0, vmax=3500)

    ds_herold.topo.plot.contourf(
        ax=ax, 
        # cmap='cmo.topo', 
        cmap = cmap_mod,
        norm = norm,
        levels = [-6000,-5000,-4000,-3000,-2000,-1000,0,500,1000,1500,2000,2500,3000,3500],
        transform=ccrs.PlateCarree(),
        extend='neither',
        cbar_kwargs={'orientation': cbar_orientation, 'label': 'surface elevation [m]', 'pad': cbar_pad})
    # add modern coastlines for comparison
    ax.coastlines(color=outline_colour)

    gl = ax.gridlines(draw_labels = labels_check, linewidth=1., color='darkgray', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.xlines = grid_check
    gl.ylines = grid_check

    if projection == "Robinson" or projection == "Orthographic":
            gl.bottom_labels = False


    if proxy_label != '':
        ax.set_title(label = '55 Ma paleolocation for ' + proxy_label +  ': LAT = ' + str(np.round(float(df['Eocene (55Ma) lat H14']), 1)) + ', LON = ' + str(np.round(float(df['Eocene (55Ma) lon H14']), 1)) , fontsize=10)
    else:
        ax.set_title(label = '55 Ma paleolocation: LAT = ' + str(np.round(float(df['Eocene (55Ma) lat H14']), 1)) + ', LON = ' + str(np.round(float(df['Eocene (55Ma) lon H14']), 1)) , fontsize=10)

    # plot orthographic ma with site in center
    # ax2 = plt.subplot(gs[1], projection=ccrs.Orthographic(paleo_lon, paleo_lat))
    # ax2 = plt.subplot(gs[1], projection=ccrs.Orthographic(0, 0))
    # # ax2.contourf(lonsc, lats, geography, levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())
    # ax2.contourf(lonsc, lats, geography, cmap='cmo.topo', levels=20, vmin=-5200, vmax=5200, transform=ccrs.PlateCarree())
    # ax2.coastlines()

    # add site marker at paleolocation
    ax.plot(df['modern lon'], df['modern lat'], 'ro', markersize=9, markerfacecolor='none', markeredgecolor='r', transform=ccrs.PlateCarree())
    ax.plot(df['Eocene (55Ma) lon H14'], df['Eocene (55Ma) lat H14'], 'ro', markersize=9, markeredgecolor='black', transform=ccrs.PlateCarree())
    ax.set_global()
    if proxy_label != '':
        if (float(df['Eocene (55Ma) lon H14']) > -100):
            labelLon = float(df['Eocene (55Ma) lon H14'])-5
            labelAlignment = 'right'
        else:
            labelLon = float(df['Eocene (55Ma) lon H14'])+5
            labelAlignment = 'left' 

        if projection == "Orthographic":      
            ax.text(labelLon, float(df['Eocene (55Ma) lat H14'])-7, proxy_label, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=10, transform=ccrs.PlateCarree())
        elif projection == "Robinson": 
            ax.text(labelLon, float(df['Eocene (55Ma) lat H14'])-15, proxy_label, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=10, transform=ccrs.PlateCarree())
        else:
            ax.text(labelLon, float(df['Eocene (55Ma) lat H14'])-18, proxy_label, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=10, transform=ccrs.PlateCarree())

    # add common colorbar
    # cbar_ax = fig1.add_axes([0.15, 0.05, 0.7, 0.05])
    # cb = plt.colorbar(cf1, cax=cbar_ax, orientation='horizontal', extend='both')
    # cb.set_label('surface elevation [m]', size=12)
    # plt.tight_layout()

    return fig

def plot_model_geographies(df, projection, proxy_label, outline_colour, grid_check, labels_check):
    ### plot Eocene paleogeography around rotated site for each DeepMIP model
    
    if projection == "Equirectangular":
        proj =ccrs.PlateCarree()
        cbar_orientation = 'horizontal'
        cbar_pad = 0.1
    elif projection == "Robinson":
        proj =ccrs.Robinson(central_longitude=0)
        cbar_orientation = 'horizontal'
        cbar_pad = 0.1
    elif projection == "Orthographic":
        proj =ccrs.Orthographic(central_longitude=float(df['Eocene (55Ma) lon H14']), central_latitude= float(df['Eocene (55Ma) lat H14']))
        cbar_orientation = 'vertical'
        cbar_pad = 0.05

    # plot global map
    fig, ax = plt.subplots(nrows=len(model_dict.keys()), ncols=2, figsize=(12.6, 32), subplot_kw=dict(projection=proj))

    # modify colors for shallow ocean and high orography slightly  
    cmap_mod = plt.cm.get_cmap(cmocean.cm.topo)
    # cmaplist = [cmap(i) for i in range(cmap.N)]
    # cmaplist[106] = cmaplist[122]
    # cmaplist[255] = cmaplist[245]
    # cmap_mod = colors.LinearSegmentedColormap.from_list('mcm',cmaplist, cmap.N)
    norm = colors.TwoSlopeNorm(vmin=-6000., vcenter=0, vmax=3500)
    # norm = colors.TwoSlopeNorm([-6000,-5000,-4000,-3000,-2000,-1000,0,500,1000,1500,2000,2500,3000,3500], ncolors=cmap_mod.N, clip=True )

    for model_count,model in enumerate(model_dict.keys()):


            cmap = plt.cm.get_cmap(cmocean.cm.topo)

            # get boundary conditions from first Eocene simulation
            exp = model_dict[model]['exps'][1]

            model_file_orog = 'data/data_for_DeepMIP_app/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                            '/' + model + '-' + exp + '-orog-' + model_dict[model]['versn'] + '.nc'    
            model_file_deptho = 'data/data_for_DeepMIP_app/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                            '/' + model + '-' + exp + '-deptho-' + model_dict[model]['versn'] + '.nc'    

            model_file_sftlf = 'data/data_for_DeepMIP_app/' + model_dict[model]['group'] + '/' + model + '/' + exp + '/' + model_dict[model]['versn'] + \
                            '/' + model + '-' + exp + '-sftlf-' + model_dict[model]['versn'] + '.nc'    

            # land color
            cmap_mod.set_under('DarkGray')

            plat = float(df['Eocene (55Ma) lat ' + model_dict[model]['rotation']])
            plon = float(df['Eocene (55Ma) lon ' + model_dict[model]['rotation']])

            #norm = BoundaryNorm(levels_mean, ncolors=cmap.N, clip=False)
            # norm = colors.TwoSlopeNorm(vmin=-5500., vcenter=0, vmax=3000)
                               
            # load data if file for model/experiment combination exists
            if Path(model_file_orog).exists():
                ds_orog = xr.open_dataset(model_file_orog, decode_times=False)
                ds_deptho = xr.open_dataset(model_file_deptho, decode_times=False)
                ds_sftlf = xr.open_dataset(model_file_sftlf, decode_times=False)

                # orog = 

                # get coordinate names
                for coord in ds_orog.coords:
                    if coord in ['lat', 'latitude', 'lat_2']:
                        lat_name_orog = coord
                    elif coord in ['lon', 'longitude']:
                        lon_name_orog = coord

                for coord in ds_deptho.coords:
                    if coord in ['lat', 'latitude', 'lat_2', 'nav_lat','TLAT','geolat_t']:
                        lat_name_deptho = coord
                    elif coord in ['lon', 'longitude', 'nav_lon','TLONG','geolon_t']:
                        lon_name_deptho = coord

                for coord in ds_sftlf.coords:
                    if coord in ['lat', 'latitude', 'lat_2', 'nav_lat','TLAT','geolat_t']:
                        lat_name_sftlf = coord
                    elif coord in ['lon', 'longitude', 'nav_lon','TLONG','geolon_t']:
                        lon_name_sftlf = coord
                
                sftlf, lonsc = add_cyclic_point(ds_sftlf.squeeze().sftlf, ds_sftlf[str(lon_name_orog)])

                if model_count == 0 or model_count == 1 or model_count == 3 or model_count == 4 or model_count == 5 or model_count == 6 or model_count == 7:
                    orog = ds_orog.squeeze().orog.where(ds_sftlf.squeeze().sftlf>0.5)
                else:
                    orog = ds_orog.squeeze().orog.where(ds_orog.squeeze().orog > 0)

                print(orog.shape)
                print(lat_name_orog)

                im_deptho=ax[model_count,0].pcolormesh(
                    ds_deptho[str(lon_name_deptho)], 
                    ds_deptho[str(lat_name_deptho)], 
                    ds_deptho.squeeze().where(ds_deptho.squeeze().deptho>0.).fillna(9999).deptho*-1., 
                    transform=ccrs.PlateCarree(), 
                    cmap=cmap_mod, 
                    norm=norm, 
                    # levels = [-6000,-5000,-4000,-3000,-2000,-1000,0,500,1000,1500,2000,2500,3000,3500],
                    edgecolors=(0, 0, 0, 0.1), 
                    linewidths=0.1)
                
                im_orog=ax[model_count,1].pcolormesh(
                    ds_orog[str(lon_name_orog)], 
                    ds_orog[str(lat_name_orog)], 
                    orog.fillna(-9999), 
                    transform=ccrs.PlateCarree(), 
                    cmap=cmap_mod, 
                    norm=norm, 
                    # levels = [-6000,-5000,-4000,-3000,-2000,-1000,0,500,1000,1500,2000,2500,3000,3500],
                    edgecolors=(0, 0, 0, 0.1), 
                    linewidths=0.1)

                ax[model_count,0].contour(lonsc, ds_orog[str(lat_name_orog)], sftlf, transform=ccrs.PlateCarree(), levels=[0.5], colors=[outline_colour])
                ax[model_count,1].contour(lonsc, ds_orog[str(lat_name_orog)], sftlf, transform=ccrs.PlateCarree(), levels=[0.5], colors=[outline_colour])

                # ax[model_count,0].coastlines(color="black")
                # ax[model_count,1].coastlines(color="black")

                ax[model_count,0].set_title(model_dict[model]['abbrv'] + ' bathymetry', fontsize=12)
                ax[model_count,1].set_title(model_dict[model]['abbrv'] + ' orography', fontsize=12)

                def clip(value, lower, upper):
                    return lower if value < lower else upper if value > upper else value

                
                ax[model_count,0].set_extent([clip(plon-30.,-180.,180.), clip(plon+30.,-180.,180.), clip(plat-25.,-90.,90.), clip(plat+25,-90.,90.)])
                ax[model_count,1].set_extent([clip(plon-30.,-180.,180.), clip(plon+30.,-180.,180.), clip(plat-25.,-90.,90.), clip(plat+25,-90.,90.)])

                ax[model_count,0].plot(plon, plat, 'ro', markersize=12, markeredgecolor='black', transform=ccrs.PlateCarree())
                ax[model_count,1].plot(plon, plat, 'ro', markersize=12, markeredgecolor='black', transform=ccrs.PlateCarree())

                # ax[model_count,0].gridlines(draw_labels = True)
                gl1 = ax[model_count,0].gridlines(draw_labels = labels_check, linewidth=1., color='darkgray', alpha=0.5, linestyle='--')
                gl1.top_labels = False
                gl1.right_labels = False
                gl1.xlines = grid_check
                gl1.ylines = grid_check
                # ax[model_count,1].gridlines(draw_labels = True)
                gl2 = ax[model_count,1].gridlines(draw_labels = labels_check, linewidth=1., color='darkgray', alpha=0.5, linestyle='--')
                gl2.top_labels = False
                gl2.xlines = grid_check
                gl2.ylines = grid_check

                if projection == "Robinson" or projection == "Orthographic":
                    gl1.bottom_labels = False
                    gl2.bottom_labels = False

                # plt.draw()

                # for ea in gl1.left_label_artists+gl1.right_label_artists:
                #     ea.set_visible(True)
                # ds.plot.contourf(
                #     ax=ax[model_count,0], 
                #     cmap='cmo.topo', 
                #     levels=21, 
                #     vmin=0, 
                #     vmax=5000, 
                #     transform=ccrs.PlateCarree(),
                #     extend='both')

    # add common colorbar
    cbar_ax1 = fig.add_axes([0.2, 0.03, 0.6, 0.01])
    cbar1 = fig.colorbar(im_deptho, cax=cbar_ax1, extend="neither", orientation='horizontal')
    cbar1.ax.tick_params(labelsize=14)
    cbar1.set_label('surface elevation [m]',size=18)

    fig.subplots_adjust(bottom=0.06, hspace=0.2, wspace=0.0)
            
    # plt.draw()

    
    # add modern coastlines for comparison
    # ax.coastlines(color=outline_colour)

    # gl = ax.gridlines(draw_labels = labels_check, linewidth=1., color='gray', alpha=0.5, linestyle='--')
    # gl.top_labels = False
    # gl.xlines = grid_check
    # gl.ylines = grid_check

    # if proxy_label != '':
    #     ax.set_title(label = '55 Ma paleolocation for ' + proxy_label +  ': LAT = ' + str(np.round(float(df['Eocene (55Ma) lat H14']), 1)) + ', LON = ' + str(np.round(float(df['Eocene (55Ma) lon H14']), 1)) , fontsize=10)
    # else:
    #     ax.set_title(label = '55 Ma paleolocation: LAT = ' + str(np.round(float(df['Eocene (55Ma) lat H14']), 1)) + ', LON = ' + str(np.round(float(df['Eocene (55Ma) lon H14']), 1)) , fontsize=10)

    # # add site marker at paleolocation
    # ax.plot(df['modern lon'], df['modern lat'], 'ro', markersize=9, markerfacecolor='none', markeredgecolor='r', transform=ccrs.PlateCarree())
    # ax.plot(df['Eocene (55Ma) lon H14'], df['Eocene (55Ma) lat H14'], 'ro', markersize=9, markeredgecolor='black', transform=ccrs.PlateCarree())
    # ax.set_global()
    # if proxy_label != '':
    #     if (float(df['Eocene (55Ma) lon H14']) > -100):
    #         labelLon = float(df['Eocene (55Ma) lon H14'])-5
    #         labelAlignment = 'right'
    #     else:
    #         labelLon = float(df['Eocene (55Ma) lon H14'])+5
    #         labelAlignment = 'left' 

    #     if projection == "Orthographic":      
    #         ax.text(labelLon, float(df['Eocene (55Ma) lat H14'])-7, proxy_label, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=10, transform=ccrs.PlateCarree())
    #     elif projection == "Robinson": 
    #         ax.text(labelLon, float(df['Eocene (55Ma) lat H14'])-15, proxy_label, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=10, transform=ccrs.PlateCarree())
    #     else:
    #         ax.text(labelLon, float(df['Eocene (55Ma) lat H14'])-18, proxy_label, horizontalalignment=labelAlignment, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), fontsize=10, transform=ccrs.PlateCarree())



    return fig

