import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import holoviews as hv
import streamlit.components.v1 as components

from deepmip_dicts import variable_dict

from app_modules import (
    init_widgets_single_site_plot,
    init_widgets_multi_site_plot,
    init_sidebar,
    sites_to_list,
    customDownloadButton
)
from deepmip_modules import (
    get_paleo_locations,
    get_model_point_data,
    scatter_line_plot,
)

st.set_page_config(
    page_title="Plot model data",
    layout="wide",
)

st.title("Plot model point data")

st.markdown(
    """
        **Interactive overview of the extracted model data.**
        The app calculates the respective early Eocene (~55 Ma) paleolocation consistent with the 
        model geographies and then extracts the data from the closest grid point for all available 
        models and simulations. You can download the extracted data in different data formats 
        at the <a href='Extract_model_data' target='_self'>extraction page</a>.
    """,
    unsafe_allow_html=True,
)

init_sidebar()

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-UPDATE FIGURE":
        st.session_state[k] = v

st.subheader("User input")

analysis_options = ["Single site", "Multiple sites"]
if "analysis_type" in st.session_state:
    var_index = analysis_options.index(st.session_state["analysis_type"])
else:
    var_index = 0


def reset_site_name():
    if "site_name" in st.session_state:
        del st.session_state["site_name"]


analysis_type = st.radio(
    "Number of sites to extract data for:",
    analysis_options,
    horizontal=True,
    index=var_index,
    key="analysis_type",
    on_change=reset_site_name,
)

# create user inputs for single site
if analysis_type == "Single site":
    (
        modern_lat,
        modern_lon,
        user_variable,
        user_site_name,
        proxy_check,
        proxy_mean,
        proxy_std,
    ) = init_widgets_single_site_plot()

    for v in [modern_lat, modern_lon, user_variable, user_site_name, analysis_type]:
        st.session_state.v = v

# create user inputs for multiple sites (i.e. CSV input)
elif analysis_type == "Multiple sites":
    csv_choice, csv_input, user_variable = init_widgets_multi_site_plot()
    modern_lats, modern_lons, names, proxy_means, proxy_stds = sites_to_list(csv_input)

    for v in [csv_input, csv_choice, user_variable]:
        st.session_state.v = v

if user_variable == "sea surface temperature":
    st.warning(
        """
        ⚠️ Warning: Land points for sea surface temperatures (SSTs) are filled
        by a nearest-neighbour lookup to facilitate the intermodel
        comparison in coastal regions. Please make sure that you selected
        a marine/coastal location by checking the model land-sea masks
        on the **Paleogeography** page.
        """
    )

if analysis_type == "Single site":
    # convert single site to list for consistency with multi-site analysis
    modern_lats = [modern_lat]
    modern_lons = [modern_lon]
    names = [user_site_name]

## step 1: get paleo position(s) consistent with DeepMIP model geographies
df_paleo_locations = get_paleo_locations(modern_lats, modern_lons, names)

# step 2: convert user variable to DeepMIP variable name
for key, value in variable_dict.items():
    if value["longname"] == user_variable:
        deepmip_var = key

## step 3: get model data for paleo position(s) and chosen variable
df_model = get_model_point_data(df_paleo_locations, deepmip_var)

col1, col2 = st.columns(2)

with col1:
    if analysis_type == "Single site":
        if "site_name" in st.session_state:
            del st.session_state["site_name"]

    site_name = st.selectbox(
        label="site to plot",
        options=df_paleo_locations.name,
        key="site_name",
    )
    for v in [site_name]:
        st.session_state.v = v

with col2:
    var_y = st.selectbox(
        label="y-axis variable",
        options=[
            "annual_mean",
            "monthly_min",
            "monthly_max",
            "DJF",
            "MAM",
            "JJA",
            "SON",
            "Jan",
            "Feb",
            "Mar",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        key="y_axis",
    )

options = [
            "annual_mean",
            "monthly_min",
            "monthly_max",
            "DJF",
            "MAM",
            "JJA",
            "SON",
            "Jan",
            "Feb",
            "Mar",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]

if analysis_type == "Multiple sites":
    site_index = list(df_paleo_locations.name).index(site_name)
    if proxy_means[site_index] != -999.9:
        proxy_check = True
    else:
        proxy_check = False
    proxy_mean = float(proxy_means[site_index])
    proxy_std = float(proxy_stds[site_index])
    proxy_label = float(proxy_stds[site_index])

st.subheader("Figure 1: " + var_y.replace("_", " ") + " vs. CO$_2$")

bokeh_composition1 = scatter_line_plot(
    df_model[df_model.site_name == site_name],
    var_y,
    "CO2",
    proxy_check,
    proxy_mean,
    proxy_std,
    "proxy estimate",
)

def get_plots():
    plots = {}
    for opt in options:
        plots[(opt)] =  scatter_line_plot(
            df_model[df_model.site_name == site_name],
            opt,
            "CO2",
            proxy_check,
            proxy_mean,
            proxy_std,
            "proxy estimate",
        )
    return plots

@st.cache_data
def get_html():
    plots = get_plots()
    hmap = hv.HoloMap(plots, kdims=["metric"]).opts(framewise=True) 
    renderer=hv.renderer('bokeh')
    html=renderer.static_html(hmap)
    return html

html = get_html()
components.html(html, height=600)
# from bokeh.models imposrt Title
# import numpy as np

# # get paleolocation
# plat = df_model.loc[(df_model["experiment"] != "piControl") & (df_model["site_name"] == site_name)].iloc[0]["lat"]
# plon = df_model.loc[(df_model["experiment"] != "piControl") & (df_model["site_name"] == site_name)].iloc[0]["lon"]

# print(plat)
# ct = datetime.datetime.now()
# ct = ct.strftime("%Y-%m-%d_%H-%M-%S")
# filename = f"figures/DeepMIP_{var_y}_vs_CO2_{site_name}_{ct}"

# p1 = hv.render(bokeh_composition1, backend="bokeh")
# p1.add_layout(
#     Title(
#         text=f"site: {site_name} (plat = {str(np.round(plat, 1))} / plon = {str(np.round(plon, 1))})",
#         text_font_size="12pt",
#         text_font_style="italic",
#     ),
#     "above",
# )

# st.bokeh_chart(p1)

# st.subheader("Figure 2: " + var_y.replace("_", " ") + " vs. GMST")

# bokeh_composition2 = scatter_line_plot(
#     df_model[df_model.site_name == site_name],
#     var_y,
#     "GMST",
#     proxy_check,
#     proxy_mean,
#     proxy_std,
#     "proxy estimate",
# )

# filename2 = f"figures/DeepMIP_{var_y}_vs_GMST_{site_name}_{ct}"

# p2 = hv.render(bokeh_composition2, backend="bokeh")
# st.bokeh_chart(p2)

# customDownloadButton(p1, p2, filename, filename2)

# customDownloadButton(p2, filename2)


