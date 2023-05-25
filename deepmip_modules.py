import numpy as np
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cmocean
import seaborn as sns
import holoviews as hv
from holoviews import opts
import streamlit as st
import matplotlib.colors as colors
from cartopy.util import add_cyclic_point
from pathlib import Path

from deepmip_dicts import exp_dict, model_dict, variable_dict

hv.extension("bokeh")


def model_table():
    df = pd.DataFrame(
        columns=[
            "Model",
            "Short Name",
            "CMIP generation",
            "Paleogeography",
        ]
    )

    for model in model_dict.keys():
        df.loc[len(df)] = [
            model,
            model_dict[model]["abbrv"],
            model_dict[model]["CMIP generation"],
            "Herold et al. (2014)"
            if model_dict[model]["rotation"] == "H14"
            else "Baatsen et al. (2016)",
        ]

    for exp in exp_dict.keys():
        ticks = []
        for model in model_dict.keys():
            if exp in model_dict[model]["exps"]:
                ticks.append(True)
            else:
                ticks.append(False)

        df[exp_dict[exp]["short_name"]] = ticks

    return df


def get_csv_data(csv_template, proxy_flag):
    if csv_template == "Enter your own data":
        csv_data = ""
    else:
        proxy_db = pd.read_csv(
            "data/Hollis 2019 DeepMIP compilation.csv", encoding="unicode_escape"
        )
        # get locations with proxy data estimates
        if proxy_flag:
            proxy_db_reduced = proxy_db[["site", "lat", "lon", "50", "sd"]]
            proxy_db_reduced["site"] = proxy_db[["site", "timeslice", "proxy"]].agg(
                "-".join, axis=1
            )
        # get locations without proxy data estimates
        else:
            proxy_db_reduced = proxy_db[["site", "lat", "lon"]]

        if csv_template == "DeepMIP marine proxies (latest Paleocene)":
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "lp"]
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "sst"]
        elif (
            csv_template == "DeepMIP marine proxies (Paleocene–Eocene Thermal Maximum)"
        ):
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "petm"]
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "sst"]
        elif csv_template == "DeepMIP marine proxies (early Eocene Climatic Optimum)":
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "eeco"]
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "sst"]
        elif csv_template == "DeepMIP terrestrial proxies (latest Paleocene)":
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "lp"]
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "lat"]
        elif (
            csv_template
            == "DeepMIP terrestrial proxies (Paleocene–Eocene Thermal Maximum)"
        ):
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "petm"]
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "lat"]
        elif (
            csv_template
            == "DeepMIP terrestrial proxies (early Eocene Climatic Optimum)"
        ):
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "eeco"]
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "lat"]
        elif csv_template == "DeepMIP marine+terrestrial proxies (latest Paleocene)":
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "lp"]
        elif (
            csv_template
            == "DeepMIP marine+terrestrial proxies (Paleocene–Eocene Thermal Maximum)"
        ):
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "petm"]
        elif (
            csv_template
            == "DeepMIP marine+terrestrial proxies (early Eocene Climatic Optimum)"
        ):
            proxy_db_reduced = proxy_db_reduced[proxy_db.timeslice == "eeco"]
        elif csv_template == "DeepMIP land (all time periods)":
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "lat"]
        elif csv_template == "DeepMIP marine proxies (all time periods)":
            proxy_db_reduced = proxy_db_reduced[proxy_db.temperature == "sst"]
        proxy_db_reduced = proxy_db_reduced.drop_duplicates(subset="site", keep="first")

        csv_data = proxy_db_reduced.to_csv(index=False, header=False)

    return csv_data


@st.cache_data
def get_paleo_locations(modern_lats, modern_lons, names):
    # models use two different paleogeographic reconstructions:
    # 1. most model use the Herold et al. (2014) reconstruction, hereafter "H14"
    # 2. NorESM1_F uses the Baatsen et al. (2016) reconstruction, hereafter "B16"

    # open both rotation files used by the models
    rotation_file_H14 = xr.open_dataset("data/LatLon_PD_55Ma_Herold2014.nc")
    rotation_file_B16 = xr.open_dataset("data/LatLon_PD_55Ma_Baatsen2016.nc")

    # initialize empty list to store results
    d = []
    skipped_sites = []

    # loop over all sites
    for count, modern_lat in enumerate(modern_lats):
        modern_lon = modern_lons[count]

        # 1. coarse approximation: look up paleolocation for modern coordinates
        # in rotation file
        paleo_lat_H14 = rotation_file_H14.LAT.sel(
            latitude=modern_lat, longitude=modern_lon, method="nearest"
        ).values
        paleo_lon_H14 = rotation_file_H14.LON.sel(
            latitude=modern_lat, longitude=modern_lon, method="nearest"
        ).values

        paleo_lat_B16 = rotation_file_B16.LAT.sel(
            latitude=modern_lat, longitude=modern_lon, method="nearest"
        ).values
        paleo_lon_B16 = rotation_file_B16.LON.sel(
            latitude=modern_lat, longitude=modern_lon, method="nearest"
        ).values

        # check if paleo location is found
        if np.isfinite(paleo_lat_H14) and np.isfinite(paleo_lat_B16):
            # 2. fine approximation: add delta between modern selected and
            # rotation grid coordinates back to paleolocation
            delta_lat_H14 = (
                modern_lat
                - rotation_file_H14.latitude.sel(
                    latitude=modern_lat, method="nearest"
                ).values
            )
            delta_lon_H14 = (
                modern_lon
                - rotation_file_H14.longitude.sel(
                    longitude=modern_lon, method="nearest"
                ).values
            )
            paleo_lat_H14 += delta_lat_H14
            paleo_lon_H14 += delta_lon_H14

            delta_lat_B16 = (
                modern_lat
                - rotation_file_H14.latitude.sel(
                    latitude=modern_lat, method="nearest"
                ).values
            )
            delta_lon_B16 = (
                modern_lon
                - rotation_file_H14.longitude.sel(
                    longitude=modern_lon, method="nearest"
                ).values
            )
            paleo_lat_B16 += delta_lat_B16
            paleo_lon_B16 += delta_lon_B16

            # build iteratively to allow for multiple sites
            d.append(
                {
                    "modern lat": modern_lat,
                    "modern lon": modern_lon,
                    "Eocene (55Ma) lat H14": paleo_lat_H14,
                    "Eocene (55Ma) lon H14": paleo_lon_H14,
                    "Eocene (55Ma) lat B16": paleo_lat_B16,
                    "Eocene (55Ma) lon B16": paleo_lon_B16,
                    "name": names[count],
                }
            )
        else:
            # if no paleo location is found, raise an exception in single-site mode
            if len(modern_lats) == 1:
                st.exception(
                    ValueError(
                        "No paleo location found for modern coordinates. Please try "
                        "again with a different location."
                    )
                )
                st.stop()
            else:
                # check whether we can get a location from Hollis et al. (2019)
                proxy_db = pd.read_csv(
                    "data/Hollis 2019 DeepMIP compilation.csv",
                    encoding="unicode_escape",
                )

                # if proxy is in Hollis et al. (2019) compilation, use that location
                if (proxy_db["site"] == names[count]).any():
                    mlat = proxy_db.loc[proxy_db.site == names[count]].iloc[0].mlat
                    mlon = proxy_db.loc[proxy_db.site == names[count]].iloc[0].mlon
                    plat = proxy_db.loc[proxy_db.site == names[count]].iloc[0].plat
                    plon = proxy_db.loc[proxy_db.site == names[count]].iloc[0].plon

                    d.append(
                        {
                            "modern lat": modern_lat,
                            "modern lon": modern_lon,
                            "Eocene (55Ma) lat H14": mlat,
                            "Eocene (55Ma) lon H14": mlon,
                            "Eocene (55Ma) lat B16": plat,
                            "Eocene (55Ma) lon B16": plon,
                            "name": names[count],
                        }
                    )
                else:
                    skipped_sites.append(names[count])

                continue

    if len(skipped_sites) > 0:
        st.warning(
            "No paleo location found for modern coordinates of the following sites: "
            + ", ".join(skipped_sites)
            + " ("
            + str(len(skipped_sites))
            + "/"
            + str(len(modern_lats))
            + " sites skipped)."
        )
    # convert to dataframe
    df = pd.DataFrame(d)
    # return DataFrame
    return df


# def get_model_point_data(modern_lat, modern_lon, paleo_lat, paleo_lon, variable):
@st.cache_data
def get_model_point_data(df, variable):
    # allocate empty list to store results for all models
    data_list = []

    progress_bar = st.progress(0)

    # loop over all models and experiments
    for exp_count, exp in enumerate(exp_dict.keys()):
        for model in model_dict.keys():
            progress_bar.progress(
                ((exp_count + 1) / (len(exp_dict.keys()))),
                text="Extracting data data for experiment " + exp,
            )

            # construct filename following the DeepMIP convention
            if variable == "tos":
                model_file = (
                    "data/data_for_DeepMIP_app/"
                    + model_dict[model]["group"]
                    + "/"
                    + model
                    + "/"
                    + exp
                    + "/"
                    + model_dict[model]["versn"]
                    + "/"
                    + model
                    + "-"
                    + exp
                    + "-"
                    + variable
                    + "-"
                    + model_dict[model]["versn"]
                    + ".mean.r180x90.filled.nc"
                )
            else:
                model_file = (
                    "data/data_for_DeepMIP_app/"
                    + model_dict[model]["group"]
                    + "/"
                    + model
                    + "/"
                    + exp
                    + "/"
                    + model_dict[model]["versn"]
                    + "/"
                    + model
                    + "-"
                    + exp
                    + "-"
                    + variable
                    + "-"
                    + model_dict[model]["versn"]
                    + ".mean.r180x90.nc"
                )

            # load data if file for model/experiment combination exists
            if Path(model_file).exists():
                ds_model = xr.open_dataset(model_file, decode_times=False)

                # get coordinate names
                for coord in ds_model.coords:
                    if coord in ["lat", "latitude"]:
                        lat_name = coord
                    elif coord in ["lon", "longitude"]:
                        lon_name = coord

                # loop over all locations
                for index, row in df.iterrows():
                    if exp == "piControl":
                        lookup_lat = float(row["modern lat"])
                        lookup_lon = float(row["modern lon"])
                    else:
                        lookup_lat = float(
                            row["Eocene (55Ma) lat " + model_dict[model]["rotation"]]
                        )
                        lookup_lon = float(
                            row["Eocene (55Ma) lon " + model_dict[model]["rotation"]]
                        )

                    # check for minimum model longitude
                    min_model_lon = np.amin(ds_model.coords[lon_name].values)
                    if min_model_lon >= 0.0 and lookup_lon < 0.0:
                        # convert lookup_lon from [-180:180] to [0:360]
                        lookup_lon_model = lookup_lon + 360.0
                    else:
                        lookup_lon_model = lookup_lon

                    var_data = getattr(ds_model, variable)
                    if variable == "tas":
                        # convert from Kelvin to Celsius
                        site_data = (
                            var_data.sel(
                                **{lat_name: lookup_lat},
                                **{lon_name: lookup_lon_model},
                                method="nearest",
                            ).values
                            - 273.15
                        )
                        unit = "°C"
                    elif variable == "pr":
                        # convert from kg m-2 s-1 to mm/day
                        site_data = (
                            var_data.sel(
                                **{lat_name: lookup_lat},
                                **{lon_name: lookup_lon_model},
                                method="nearest",
                            ).values
                            * 86400.0
                        )
                        unit = "mm/day"
                    else:
                        site_data = (
                            var_data.sel(
                                **{lat_name: lookup_lat},
                                **{lon_name: lookup_lon_model},
                                method="nearest",
                            ).values
                            * 1.0
                        )
                        unit = variable_dict[variable]["unit"]

                    # get GMST
                    exp_list = model_dict[model]["exps"]
                    gmst_list = model_dict[model]["gmst"]

                    # check vailable model experiments against full list
                    for count, model_exp in enumerate(exp_list):
                        if model_exp == exp:
                            gmst = gmst_list[count]

                    # store results for individual metrics in a dictionary

                    # monthly data available
                    if len(site_data) == 12:
                        data_list.append(
                            dict(
                                model_short=model_dict[model]["abbrv"],
                                model=model,
                                experiment=exp_dict[exp]["medium_name"],
                                CO2=float(exp_dict[exp]["CO2"]),
                                GMST=gmst,
                                site_name=row["name"],
                                lat=np.round(lookup_lat, 2),
                                lon=np.round(lookup_lon, 2),
                                var=variable,
                                long_name=variable_dict[variable]["longname"],
                                unit=unit,
                                annual_mean=np.mean(site_data),
                                monthly_min=np.min(site_data),
                                monthly_max=np.max(site_data),
                                DJF=np.mean(site_data[[11, 0, 1]]),
                                MAM=np.mean(site_data[[2, 3, 4]]),
                                JJA=np.mean(site_data[[5, 6, 7]]),
                                SON=np.mean(site_data[[8, 9, 10]]),
                                Jan=float(site_data[0]),
                                Feb=float(site_data[1]),
                                Mar=float(site_data[2]),
                                Apr=float(site_data[3]),
                                May=float(site_data[4]),
                                Jun=float(site_data[5]),
                                Jul=float(site_data[6]),
                                Aug=float(site_data[7]),
                                Sep=float(site_data[8]),
                                Oct=float(site_data[9]),
                                Nov=float(site_data[10]),
                                Dec=float(site_data[11]),
                            )
                        )
                    # only annual data available
                    elif len(site_data) == 1:
                        data_list.append(
                            dict(
                                model_short=model_dict[model]["abbrv"],
                                model=model,
                                experiment=exp_dict[exp]["medium_name"],
                                CO2=float(exp_dict[exp]["CO2"]),
                                GMST=gmst,
                                site_name=row["name"],
                                lat=np.round(lookup_lat, 2),
                                lon=np.round(lookup_lon, 2),
                                var=variable,
                                long_name=variable_dict[variable]["longname"],
                                unit=unit,
                                annual_mean=float(site_data[0]),
                            )
                        )

    # convert dictionary to Pandas dataframe for easier handling and plotting
    df_out = pd.DataFrame(data_list).round(1)

    # calculate ensemble mean for each site and experiment
    for exp in exp_dict.keys():
        for index, row in df.iterrows():
            df_out.loc[len(df_out)] = df_out.loc[
                (df_out["experiment"] == exp_dict[exp]["medium_name"])
                & (df_out["site_name"] == row["name"])
            ].mean(numeric_only=True)
            # set ensemble mean metadata
            df_out.loc[len(df_out) - 1, "model"] = "ensemble_mean"
            df_out.loc[len(df_out) - 1, "model_short"] = "mean"
            df_out.loc[len(df_out) - 1, "experiment"] = exp_dict[exp]["medium_name"]
            df_out.loc[len(df_out) - 1, "var"] = variable
            df_out.loc[len(df_out) - 1, "long_name"] = variable_dict[variable][
                "longname"
            ]
            df_out.loc[len(df_out) - 1, "unit"] = unit
            df_out.loc[len(df_out) - 1, "site_name"] = row["name"]

    progress_bar.empty()

    return df_out.round(1)


@st.cache_data
def location_data_boxplot(df, proxy_flag, proxy_mean, proxy_std, proxy_label):
    df_plot = df[(df.model != "ensemble_mean")]

    # get paleolocation
    df_Eocene = df_plot.loc[df_plot["experiment"] != "piControl"]
    plat = df_Eocene.iloc[0]["lat"]
    plon = df_Eocene.iloc[0]["lon"]

    variable = df_plot.iloc[0]["var"]

    # change dataframe from wide (9 columns) to long (3 columns) format to use
    # hue method in seaborn boxplot
    dfMelt = pd.melt(
        df_plot,
        id_vars=["experiment"],
        value_vars=[
            "annual_mean",
            "monthly_min",
            "monthly_min",
            "monthly_max",
            "DJF",
            "MAM",
            "JJA",
            "SON",
        ],
    )

    # define figure layout first
    fig, axes = plt.subplots(2, 1, figsize=(13, 16))

    # generate list of medium-length experiment anmes for plot ordering
    list_medium_names = []
    for key, value in exp_dict.items():
        list_medium_names.append(value["medium_name"])

    # boxplot with seaborn
    # (https://seaborn.pydata.org/generated/seaborn.boxplot.html)
    ax3 = sns.boxplot(
        data=dfMelt,
        x="experiment",
        y="value",
        hue="variable",
        hue_order=["annual_mean", "monthly_min", "monthly_max"],
        order=list_medium_names,
        palette=["tab:green", "tab:blue", "tab:red"],
        linewidth=2.0,
        ax=axes[0],
    )
    ax3 = sns.swarmplot(
        data=dfMelt,
        x="experiment",
        y="value",
        hue="variable",
        hue_order=["annual_mean", "monthly_min", "monthly_max"],
        order=list_medium_names,
        palette=["tab:green", "tab:blue", "tab:red"],
        linewidth=1.5,
        edgecolor="black",
        size=5,
        dodge=True,
        ax=axes[0],
    )

    ax4 = sns.boxplot(
        data=dfMelt,
        x="experiment",
        y="value",
        hue="variable",
        hue_order=["DJF", "MAM", "JJA", "SON"],
        palette=["tab:blue", "tab:orange", "tab:green", "tab:red"],
        linewidth=2.0,
        ax=axes[1],
    )
    ax4 = sns.swarmplot(
        data=dfMelt,
        x="experiment",
        y="value",
        hue="variable",
        hue_order=["DJF", "MAM", "JJA", "SON"],
        palette=["tab:blue", "tab:orange", "tab:green", "tab:red"],
        linewidth=1.5,
        edgecolor="black",
        size=5,
        dodge=True,
        ax=axes[1],
    )

    # add optional proxy estimates as reference
    if proxy_flag:
        if proxy_std != "":
            ax3.axhspan(
                proxy_mean - proxy_std,
                proxy_mean + proxy_std,
                facecolor="lightcoral",
                alpha=0.4,
                zorder=0.0,
            )
            ax4.axhspan(
                proxy_mean - proxy_std,
                proxy_mean + proxy_std,
                facecolor="lightcoral",
                alpha=0.4,
                zorder=0.0,
            )
            ax3.text(
                1.5,
                proxy_mean + proxy_std,
                proxy_label,
                fontsize=20,
                color="lightcoral",
                verticalalignment="bottom",
            )
            ax4.text(
                1.5,
                proxy_mean + proxy_std,
                proxy_label,
                fontsize=20,
                color="lightcoral",
                verticalalignment="bottom",
            )

    titleString = (
        "DeepMIP "
        + variable_dict[variable]["longname"]
        + " (LAT = "
        + str(np.round(plat, 1))
        + " / LON = "
        + str(np.round(plon, 1))
        + ")"
    )

    yLabel = variable_dict[variable]["longname"] + " [" + df.iloc[0]["unit"] + "]"

    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles[0:3], labels[0:3], fontsize="16")
    ax3.set(title=titleString, xlabel="", ylabel=yLabel)
    [
        ax3.axvline(x, color="gray", linestyle="-", linewidth=0.5, zorder=0.0)
        for x in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    ]

    handles2, labels2 = ax4.get_legend_handles_labels()
    ax4.legend(handles2[0:4], labels2[0:4], fontsize="16")
    ax4.set(title=titleString, xlabel="", ylabel=yLabel)
    [
        ax4.axvline(x, color="gray", linestyle="-", linewidth=0.5, zorder=0.0)
        for x in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    ]

    return fig


def scatter_line_plot(
    df, var_y, var_x, proxy_check, proxy_mean, proxy_std, proxy_label
):
    df_plot = df[(df.model != "ensemble_mean")]

    if var_x == "experiment":
        df_redcued = df_plot
        log_x = False
    elif var_x == "CO2":
        log_x = True
        df_redcued = df_plot.loc[df_plot["experiment"] != "piControl"]
    elif var_x == "GMST":
        log_x = False
        df_redcued = df_plot.loc[df_plot["experiment"] != "piControl"]

    unit = df_plot.iloc[0]["unit"]
    ylabel = var_y + " [" + unit + "]"
    # yLabel = variable_dict[variable]["longname"] + " [" + df.iloc[0]["unit"] + "]"
    ylabel = df.iloc[0]["long_name"] + " [" + unit + "]"

    # generate list of medium-length experiment anmes for plot ordering
    list_medium_names = []
    for key, value in exp_dict.items():
        list_medium_names.append(value["medium_name"])

    # add proxy reference annotations
    if proxy_check:
        hline = hv.HLine(proxy_mean).opts(opts.HLine(color="coral", alpha=1.0))
        if proxy_std >= 0.0:
            hspan = hv.HSpan(proxy_mean - proxy_std, proxy_mean + proxy_std).opts(
                opts.HSpan(color="lightcoral", alpha=0.4)
            )
            label_offset = 0.7 * proxy_std
        else:
            label_offset = 0.1 * proxy_mean

        if var_x == "experiment":
            text_x = "DeepMIP_1x"
        elif var_x == "CO2":
            text_x = 500
        elif var_x == "GMST":
            text_x = 20

        htext = hv.Text(text_x, proxy_mean + label_offset, proxy_label).opts(
            opts.Text(color="lightcoral", align="start")
        )

    # generate plot labels
    if var_x == "experiment":
        xlabel = "DeepMIP experiment"
    elif var_x == "CO2":
        xlabel = "atmospheric CO₂ [ppmv]"
    elif var_x == "GMST":
        xlabel = "GMST [°C]"

    variable = df_plot.iloc[0]["var"]
    titleString = (
        "DeepMIP "
        + variable_dict[variable]["longname"]
        + " ("
        + var_y.replace("_", " ")
        + ")"
    )

    scatter = (
        hv.Scatter(
            df_redcued,
            kdims=[var_x],
            vdims=[var_y, "model_short", "experiment"],
        )
        .redim.values(**{"experiment": list_medium_names})
        .groupby("model_short")
        .overlay()
        .opts(
            opts.Scatter(
                logx=log_x,
                xlabel=xlabel,
                ylabel=ylabel,
                jitter=0.0,
                title=titleString,
                height=500,
                width=600,
                # responsive=True,
                color_index="customer",
                cmap=[
                    "blue",
                    "orange",
                    "blue",
                    "orange",
                    "blue",
                    "orange",
                    "blue",
                    "orange",
                    "blue",
                    "orange",
                ],
                show_legend=True,
                legend_position="top",
                size=12,
                tools=["hover", "wheel_zoom"],
                line_color="black",
                fontsize={
                    "legend": 8,
                    "title": 14,
                    "labels": 14,
                    "xticks": 11,
                    "yticks": 11,
                },
            )
        )
    )

    if var_x == "experiment":
        box = hv.BoxWhisker(df_redcued, kdims=[var_x], vdims=[var_y]).opts(
            opts.BoxWhisker(
                logx=log_x,
                box_color="white",
                width=600,
                height=500,
                responsive=True,
                show_legend=False,
                whisker_color="black",
                box_fill_color="#63c5da",
            )
        )

        if proxy_check:
            if proxy_std >= 0.0:
                composition = hspan * hline * box * scatter * htext
            else:
                composition = hline * box * scatter * htext
        else:
            composition = box * scatter

    else:
        line = (
            hv.Curve(df_redcued, kdims=[var_x], vdims=[var_y, "model_short"])
            .redim.values(**{"experiment": list_medium_names})
            .groupby("model_short")
            .overlay()
            .opts(opts.Scatter(size=12))
        )

        # text  = (
        #     hv.Text(
        # )

        if proxy_check:
            if proxy_std >= 0.0:
                composition = hspan * hline * line * scatter * htext
            else:
                composition = hline * line * scatter * htext
        else:
            composition = scatter * line

    return composition


def annual_cycle_plot(df, proxy_check, proxy_mean, proxy_std, proxy_label):
    # df["monthly"] = df["Jan"] + df["Feb"]
    # df_ensemble = df[(df.model != "ensemble_mean")]

    months = [
        "model_short",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    # df_monthly = df_exp[months].transpose().rename(columns={35:'model'})

    # # generate list of medium-length experiment anmes for plot ordering
    # short_names = []
    # for key, value in model_dict.items():
    #     short_names.append(value["abbrv"])

    lines = []
    spreads = []

    # loop over all models and experiments
    for exp_count, exp in enumerate(exp_dict.keys()):
        if exp == "piControl":
            continue
        df_exp = df[(df.experiment == exp_dict[exp]["medium_name"])]
        # df_monthly = df_exp[months].transpose().rename(columns={'mean':'ensemble mean'}, inplace=True)
        df_monthly = df_exp[months].transpose()
        df_monthly.columns = df_monthly.iloc[0]
        df_monthly = df_monthly[1:].rename(columns={"mean": "ensemble mean"})
        df_monthly["month"] = months[1:13]
        df_monthly["experiment"] = exp_dict[exp]["medium_name"]

        print(exp)
        print(df_monthly)

        for model in model_dict.keys():
            # individual models
            if exp in model_dict[model]["exps"]:
                line = hv.Curve(
                    df_monthly,
                    "month",
                    vdims=[model_dict[model]["abbrv"], "experiment"],
                    label=exp_dict[exp]["short_name"],
                ).opts(
                    line_color=exp_dict[exp]["color"],
                    alpha=1.0,
                    line_width=1.0,
                    line_dash="dashed",
                )
                lines.append(line)

        # ensemble mean
        line = hv.Curve(
            df_monthly,
            "month",
            vdims=["ensemble mean", "experiment"],
            label=exp_dict[exp]["short_name"],
        ).opts(line_color=exp_dict[exp]["color"], alpha=1.0, line_width=5.0)
        lines.append(line)

        # ensemble spread
        # ens_std = df_monthly.loc[:, df_monthly.columns != 'month'].std(axis=1)

        # # only plot spread if it is not zero
        # if (any(ens_std!=0)):
        #     # if exp == "deepmip_sens_1xCO2":
        #     spread = (hv.Spread((df_monthly["month"], df_monthly["ensemble mean"], ens_std))
        #         .opts(
        #             fill_color= exp_dict[exp]["color"],
        #             fill_alpha=0.2)
        #         )
        #     spreads.append(spread)

    # generate plot labels
    xlabel = "calendar month"
    unit = df.iloc[0]["unit"]
    ylabel = df.iloc[0]["long_name"] + " [" + unit + "]"

    variable = df.iloc[0]["var"]
    titleString = "DeepMIP " + variable_dict[variable]["longname"] + " (annual cycle)"

    # add proxy reference annotations
    if proxy_check:
        hline = hv.HLine(proxy_mean).opts(opts.HLine(color="coral", alpha=1.0))
        if proxy_std >= 0.0:
            hspan = hv.HSpan(proxy_mean - proxy_std, proxy_mean + proxy_std).opts(
                opts.HSpan(color="lightcoral", alpha=0.4)
            )
            label_offset = 0.7 * proxy_std
        else:
            label_offset = 0.1 * proxy_mean

        text_x = "Feb"

        htext = hv.Text(text_x, proxy_mean + label_offset, proxy_label).opts(
            opts.Text(color="lightcoral", align="start")
        )
    overlay_lines = hv.Overlay(lines).opts(
        opts.Curve(
            xlabel=xlabel,
            ylabel=ylabel,
            title=titleString,
            height=500,
            width=600,
            # responsive=True,
            show_legend=True,
            tools=["hover", "wheel_zoom"],
            fontsize={
                "legend": 8,
                "title": 14,
                "labels": 14,
                "xticks": 11,
                "yticks": 11,
            },
        ),
    )

    if proxy_check:
        if proxy_std >= 0.0:
            composition = hspan * hline * overlay_lines
        else:
            composition = hline * overlay_lines
    else:
        composition = overlay_lines

    composition.opts(legend_position="top")

    # overlay_spread = (hv.Overlay(lines)
    #                 .opts(
    #                     opts.Curve(
    #                         # logx=log_x,
    #                         # xlabel=xlabel,
    #                         # ylabel=ylabel,
    #                         # title=titleString,
    #                         height=500,
    #                         responsive=True,
    #                         show_legend=True,
    #                         tools=["hover", "wheel_zoom"],
    #                         fontsize={
    #                             "legend": 10.8,
    #                             "title": 14,
    #                             "labels": 14,
    #                             "xticks": 11,
    #                             "yticks": 11,
    #                         },
    #                     )
    #                 )
    #             ) * (hv.Overlay(spreads)
    #                 .opts(
    #                     opts.Spread(
    #                         height=500,
    #                         responsive=True,
    #                         show_legend=True,
    #                         tools=["hover", "wheel_zoom"],
    #                         fontsize={
    #                             "legend": 10.8,
    #                             "title": 14,
    #                             "labels": 14,
    #                             "xticks": 11,
    #                             "yticks": 11,
    #                         },
    #                     )
    #                 )
    #             )

    return composition


def plot_global_paleogeography(
    df,
    projection,
    proxy_label,
    outline_colour,
    grid_check,
    labels_check,
    central_lon,
    central_lat,
    sites_check,
):
    ### plot Eocene paleogeography with rotated site(s)

    # open Herold et al. (2014) paleogeography
    # cyclic longitude for contourf plot was added with cdo (cdo sethalo,1,0)
    # for better performance, but can also be added in Python with:
    # geography, lonsc = add_cyclic_point(ds_herold.topo, ds_herold.lon)
    ds_herold = xr.open_dataset("data/herold_etal_eocene_topo_1x1.halo.nc")

    if projection == "Equirectangular":
        proj = ccrs.PlateCarree(central_longitude=central_lon)
        cbar_orientation = "horizontal"
        cbar_pad = 0.1
    elif projection == "Robinson":
        proj = ccrs.Robinson(central_longitude=central_lon)
        cbar_orientation = "horizontal"
        cbar_pad = 0.1
    elif projection == "Orthographic":
        proj = ccrs.Orthographic(
            central_longitude=central_lon,
            central_latitude=central_lat,
        )
        cbar_orientation = "vertical"
        cbar_pad = 0.05

    # plot global map
    fig, ax = plt.subplots(1, subplot_kw=dict(projection=proj))

    # modify colors for shallow ocean and high orography slightly
    cmap = plt.cm.get_cmap(cmocean.cm.topo)
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmaplist[106] = cmaplist[122]
    cmaplist[255] = cmaplist[245]
    cmap_mod = colors.LinearSegmentedColormap.from_list("mcm", cmaplist, cmap.N)
    norm = colors.TwoSlopeNorm(vmin=-6000.0, vcenter=0, vmax=3500)

    ds_herold.topo.plot.contourf(
        ax=ax,
        # cmap='cmo.topo',
        cmap=cmap_mod,
        norm=norm,
        levels=[
            -6000,
            -5000,
            -4000,
            -3000,
            -2000,
            -1000,
            0,
            500,
            1000,
            1500,
            2000,
            2500,
            3000,
            3500,
        ],
        transform=ccrs.PlateCarree(),
        extend="neither",
        cbar_kwargs={
            "orientation": cbar_orientation,
            "label": "surface elevation [m]",
            "pad": cbar_pad,
        },
    )
    # add modern coastlines for comparison
    ax.coastlines(color=outline_colour)

    gl = ax.gridlines(
        draw_labels=labels_check,
        linewidth=1.0,
        color="darkgray",
        alpha=0.5,
        linestyle="--",
    )
    gl.top_labels = False
    gl.xlines = grid_check
    gl.ylines = grid_check

    if projection == "Robinson" or projection == "Orthographic":
        gl.bottom_labels = False

    if len(proxy_label) == 1:
        if proxy_label[0] != "":
            ax.set_title(
                label="55 Ma paleolocation for "
                + proxy_label[0]
                + ": LAT = "
                + str(np.round(float(df["Eocene (55Ma) lat H14"]), 1))
                + ", LON = "
                + str(np.round(float(df["Eocene (55Ma) lon H14"]), 1)),
                fontsize=10,
            )
        else:
            ax.set_title(
                label="55 Ma paleolocation: LAT = "
                + str(np.round(float(df["Eocene (55Ma) lat H14"]), 1))
                + ", LON = "
                + str(np.round(float(df["Eocene (55Ma) lon H14"]), 1)),
                fontsize=10,
            )
    else:
        ax.set_title(
            label="55 Ma paleolocations (Herold et al. 2014)",
            fontsize=10,
        )

    # add site markers at paleolocation
    # loop over all locations
    for index, row in df.iterrows():
        # ax.plot(
        #     row["modern lon"],
        #     row["modern lat"],
        #     "ro",
        #     markersize=9,
        #     markerfacecolor="none",
        #     markeredgecolor="r",
        #     transform=ccrs.PlateCarree(),
        # )
        ax.plot(
            row["Eocene (55Ma) lon H14"],
            row["Eocene (55Ma) lat H14"],
            "ro",
            markersize=9,
            markeredgecolor="black",
            transform=ccrs.PlateCarree(),
        )
    ax.set_global()

    if sites_check:
        for index, row in df.iterrows():
            if proxy_label[index] != "":
                if float(row["Eocene (55Ma) lon H14"]) > -100:
                    labelLon = float(row["Eocene (55Ma) lon H14"]) - 5
                    labelAlignment = "right"
                else:
                    labelLon = float(row["Eocene (55Ma) lon H14"]) + 5
                    labelAlignment = "left"

                if projection == "Orthographic":
                    ax.text(
                        labelLon,
                        float(row["Eocene (55Ma) lat H14"]) - 7,
                        proxy_label[index],
                        horizontalalignment=labelAlignment,
                        bbox=dict(
                            facecolor="white", edgecolor="black", boxstyle="round"
                        ),
                        fontsize=10,
                        transform=ccrs.PlateCarree(),
                    )
                elif projection == "Robinson":
                    ax.text(
                        labelLon,
                        float(row["Eocene (55Ma) lat H14"]) - 15,
                        proxy_label[index],
                        horizontalalignment=labelAlignment,
                        bbox=dict(
                            facecolor="white", edgecolor="black", boxstyle="round"
                        ),
                        fontsize=10,
                        transform=ccrs.PlateCarree(),
                    )
                else:
                    ax.text(
                        labelLon,
                        float(row["Eocene (55Ma) lat H14"]) - 18,
                        proxy_label[index],
                        horizontalalignment=labelAlignment,
                        bbox=dict(
                            facecolor="white", edgecolor="black", boxstyle="round"
                        ),
                        fontsize=10,
                        transform=ccrs.PlateCarree(),
                    )

    return fig


@st.cache_data
def plot_model_geographies(
    df, projection, proxy_label, outline_colour, grid_check, labels_check
):
    ### plot Eocene paleogeography around rotated site for each DeepMIP model

    if projection == "Equirectangular":
        proj = ccrs.PlateCarree()
        cbar_orientation = "horizontal"
        cbar_pad = 0.1
    elif projection == "Robinson":
        proj = ccrs.Robinson(central_longitude=0)
        cbar_orientation = "horizontal"
        cbar_pad = 0.1
    elif projection == "Orthographic":
        if len(proxy_label) == 1:
            proj = ccrs.Orthographic(
                central_longitude=float(df["Eocene (55Ma) lon H14"]),
                central_latitude=float(df["Eocene (55Ma) lat H14"]),
            )
            cbar_orientation = "vertical"
            cbar_pad = 0.05
        else:
            proj = ccrs.Orthographic(
                central_longitude=0.0,
                central_latitude=0.0,
            )
            cbar_orientation = "vertical"
            cbar_pad = 0.05
    # plot global map
    fig, ax = plt.subplots(
        nrows=len(model_dict.keys()),
        ncols=3,
        figsize=(14, 32),
        subplot_kw=dict(projection=proj),
    )

    # from https://stackoverflow.com/a/40930194
    import matplotlib.colors as mcolors

    def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
        if n == -1:
            n = cmap.N
        new_cmap = mcolors.LinearSegmentedColormap.from_list(
            "trunc({name},{a:.2f},{b:.2f})".format(name=cmap.name, a=minval, b=maxval),
            cmap(np.linspace(minval, maxval, n)),
        )
        return new_cmap

    cmap_bathy = plt.cm.get_cmap(cmocean.cm.deep_r)
    norm_bathy = colors.BoundaryNorm(np.arange(-6000, 500, 500), cmap_bathy.N)
    cmap_bathy.set_under("DarkGray")

    cmap_orog = truncate_colormap(plt.cm.get_cmap("terrain"), 0.15, 1.0)
    norm_orog = colors.BoundaryNorm(np.arange(-250, 3000, 250), cmap_orog.N)

    cmap_slftf = plt.cm.get_cmap("PiYG")
    norm_slftf = colors.BoundaryNorm(
        [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], cmap_slftf.N
    )

    progress_bar = st.progress(0)

    for model_count, model in enumerate(model_dict.keys()):
        progress_bar.progress(
            ((model_count + 1) / (len(model_dict.keys()) + 1)),
            text="Processing data for " + model,
        )

        # get boundary conditions from first Eocene simulation
        exp = model_dict[model]["exps"][1]

        model_file_orog = (
            "data/data_for_DeepMIP_app/"
            + model_dict[model]["group"]
            + "/"
            + model
            + "/"
            + exp
            + "/"
            + model_dict[model]["versn"]
            + "/"
            + model
            + "-"
            + exp
            + "-orog-"
            + model_dict[model]["versn"]
            + ".nc"
        )
        model_file_deptho = (
            "data/data_for_DeepMIP_app/"
            + model_dict[model]["group"]
            + "/"
            + model
            + "/"
            + exp
            + "/"
            + model_dict[model]["versn"]
            + "/"
            + model
            + "-"
            + exp
            + "-deptho-"
            + model_dict[model]["versn"]
            + ".nc"
        )

        model_file_sftlf = (
            "data/data_for_DeepMIP_app/"
            + model_dict[model]["group"]
            + "/"
            + model
            + "/"
            + exp
            + "/"
            + model_dict[model]["versn"]
            + "/"
            + model
            + "-"
            + exp
            + "-sftlf-"
            + model_dict[model]["versn"]
            + ".nc"
        )

        plat = float(df["Eocene (55Ma) lat " + model_dict[model]["rotation"]])
        plon = float(df["Eocene (55Ma) lon " + model_dict[model]["rotation"]])

        # load data if file for model/experiment combination exists
        if Path(model_file_orog).exists():
            ds_orog = xr.open_dataset(model_file_orog, decode_times=False)
            ds_deptho = xr.open_dataset(model_file_deptho, decode_times=False)
            ds_sftlf = xr.open_dataset(model_file_sftlf, decode_times=False)

            # get coordinate names
            for coord in ds_orog.coords:
                if coord in ["lat", "latitude", "lat_2"]:
                    lat_name_orog = coord
                elif coord in ["lon", "longitude"]:
                    lon_name_orog = coord

            for coord in ds_deptho.coords:
                if coord in [
                    "lat",
                    "latitude",
                    "lat_2",
                    "nav_lat",
                    "TLAT",
                    "geolat_t",
                ]:
                    lat_name_deptho = coord
                elif coord in [
                    "lon",
                    "longitude",
                    "nav_lon",
                    "TLONG",
                    "geolon_t",
                ]:
                    lon_name_deptho = coord

            for coord in ds_sftlf.coords:
                if coord in [
                    "lat",
                    "latitude",
                    "lat_2",
                    "nav_lat",
                    "TLAT",
                    "geolat_t",
                ]:
                    lat_name_sftlf = coord
                elif coord in [
                    "lon",
                    "longitude",
                    "nav_lon",
                    "TLONG",
                    "geolon_t",
                ]:
                    lon_name_sftlf = coord

            sftlf, lonsc = add_cyclic_point(
                ds_sftlf.squeeze().sftlf, ds_sftlf[str(lon_name_orog)]
            )

            orog = ds_orog.squeeze().orog

            im_deptho = ax[model_count, 0].pcolormesh(
                ds_deptho[str(lon_name_deptho)],
                ds_deptho[str(lat_name_deptho)],
                ds_deptho.squeeze()
                .where(ds_deptho.squeeze().deptho > 0.0)
                .fillna(9999)
                .deptho
                * -1.0,
                transform=ccrs.PlateCarree(),
                cmap=cmap_bathy,
                norm=norm_bathy,
                edgecolors=(0, 0, 0, 0.1),
                linewidths=0.1,
            )

            im_orog = ax[model_count, 1].pcolormesh(
                ds_orog[str(lon_name_orog)],
                ds_orog[str(lat_name_orog)],
                orog.fillna(-9999),
                transform=ccrs.PlateCarree(),
                cmap=cmap_orog,
                norm=norm_orog,
                edgecolors=(0, 0, 0, 0.1),
                linewidths=0.1,
            )

            im_sftlf = ax[model_count, 2].pcolormesh(
                ds_sftlf[str(lon_name_orog)],
                ds_sftlf[str(lat_name_orog)],
                ds_sftlf.squeeze().sftlf,
                transform=ccrs.PlateCarree(),
                cmap=cmap_slftf,
                norm=norm_slftf,
                edgecolors=(0, 0, 0, 0.1),
                linewidths=0.1,
            )

            ax[model_count, 0].set_title(
                model_dict[model]["abbrv"] + " bathymetry", fontsize=12
            )
            ax[model_count, 1].set_title(
                model_dict[model]["abbrv"] + " orography", fontsize=12
            )
            ax[model_count, 2].set_title(
                model_dict[model]["abbrv"] + " land-sea mask", fontsize=12
            )

            def clip(value, lower, upper):
                return lower if value < lower else upper if value > upper else value

            for count in range(3):
                ax[model_count, count].set_extent(
                    [
                        clip(plon - 30.0, -180.0, 180.0),
                        clip(plon + 30.0, -180.0, 180.0),
                        clip(plat - 25.0, -90.0, 90.0),
                        clip(plat + 25, -90.0, 90.0),
                    ]
                )

                ax[model_count, count].contour(
                    lonsc,
                    ds_orog[str(lat_name_orog)],
                    sftlf,
                    transform=ccrs.PlateCarree(),
                    levels=[0.5],
                    colors=[outline_colour],
                )

                ax[model_count, count].plot(
                    plon,
                    plat,
                    "ro",
                    markersize=12,
                    markeredgecolor="black",
                    transform=ccrs.PlateCarree(),
                )

            # ax[model_count,0].gridlines(draw_labels = True)
            gl1 = ax[model_count, 0].gridlines(
                draw_labels=labels_check,
                linewidth=1.0,
                color="darkgray",
                alpha=0.5,
                linestyle="--",
            )
            gl1.top_labels = False
            gl1.right_labels = False
            gl1.xlines = grid_check
            gl1.ylines = grid_check
            # ax[model_count,1].gridlines(draw_labels = True)
            gl2 = ax[model_count, 1].gridlines(
                draw_labels=labels_check,
                linewidth=1.0,
                color="darkgray",
                alpha=0.5,
                linestyle="--",
            )
            gl2.top_labels = False
            gl2.right_labels = False
            gl2.xlines = grid_check
            gl2.ylines = grid_check

            gl3 = ax[model_count, 2].gridlines(
                draw_labels=labels_check,
                linewidth=1.0,
                color="darkgray",
                alpha=0.5,
                linestyle="--",
            )
            gl3.top_labels = False
            gl3.xlines = grid_check
            gl3.ylines = grid_check

            if projection == "Robinson" or projection == "Orthographic":
                gl1.bottom_labels = False
                gl2.bottom_labels = False
                gl3.bottom_labels = False

    progress_bar.progress(
        ((model_count + 2) / (len(model_dict.keys()) + 1)),
        text="Creating Figure ... ",
    )

    # add common colorbars

    cbar_ax1 = fig.add_axes([0.155, 0.035, 0.2, 0.01])
    cbar1 = fig.colorbar(
        im_deptho, cax=cbar_ax1, extend="neither", orientation="horizontal"
    )
    cbar1.ax.tick_params(labelsize=10)
    cbar1.set_label("bathymetry [m]", size=14)

    cbar_ax2 = fig.add_axes([0.413, 0.035, 0.2, 0.01])
    cbar2 = fig.colorbar(
        im_orog, cax=cbar_ax2, extend="neither", orientation="horizontal"
    )
    cbar2.ax.tick_params(labelsize=10)
    cbar2.set_label("orography [m]", size=14)

    cbar_ax3 = fig.add_axes([0.671, 0.035, 0.2, 0.01])
    cbar3 = fig.colorbar(
        im_sftlf, cax=cbar_ax3, extend="neither", orientation="horizontal"
    )
    cbar3.ax.tick_params(labelsize=10)
    cbar3.set_label("land fraction [m]", size=14)

    fig.subplots_adjust(bottom=0.06, hspace=0.2, wspace=0.0)

    return fig, progress_bar
