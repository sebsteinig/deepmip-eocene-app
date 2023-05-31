
import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import io

from app_modules import (
    init_widgets_single_site_map,
    init_widgets_multi_site_map,
    init_sidebar,
    sites_to_list,
    customDownloadButton_JPG_PNG,
    customDownloadButton_JPG_PNG_PDF
)
from deepmip_modules import (
    get_paleo_locations,
    plot_global_paleogeography,
    plot_model_geographies,
)

st.set_page_config(
    page_title="Plot Maps",
    layout="wide",
)

st.title("Paleogeographic reconstruction")

init_sidebar()

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-UPDATE MAPS":
        st.session_state[k] = v

st.subheader("User input")

analysis_options = ["Single site", "Multiple sites"]
if "analysis_type" in st.session_state:
    var_index = analysis_options.index(st.session_state["analysis_type"])
else:
    var_index = 0


def reset_central_location():
    # delete previous input from session state
    if "central_lon" in st.session_state:
        del st.session_state["central_lon"]
    if "central_lat" in st.session_state:
        del st.session_state["central_lat"]


analysis_type = st.radio(
    "Number of sites to plot:",
    analysis_options,
    horizontal=True,
    index=var_index,
    key="analysis_type",
    on_change=reset_central_location,
)

# create user inputs for single site
if analysis_type == "Single site":
    modern_lat, modern_lon, user_site_name = init_widgets_single_site_map()

    for v in [modern_lat, modern_lon, user_site_name, analysis_type]:
        st.session_state.v = v

# create user inputs for multiple sites (i.e. CSV input)
elif analysis_type == "Multiple sites":
    csv_choice, csv_input = init_widgets_multi_site_map()
    modern_lats, modern_lons, names, proxy_means, proxy_stds = sites_to_list(csv_input, 5)

    for v in [csv_input, csv_choice, analysis_type]:
        st.session_state.v = v

if analysis_type == "Single site":
    # convert single site to list for consistency with multi-site analysis
    modern_lats = [modern_lat]
    modern_lons = [modern_lon]
    names = [user_site_name]

## step 1: get paleo position(s) consistent with DeepMIP model geographies
df_paleo_locations = get_paleo_locations(modern_lats, modern_lons, names)
# st.dataframe(df_locations.style.format("{:.1f}"))

st.subheader(" DeepMIP geography (Herold et al., 2014)")
st.markdown(
    """
        Reconstruction of the chosen site's paleolocation at ~55 Ma using the 
        original DeepMIP paleogeography from 
        [Herold et al. (2014)](https://doi.org/10.5194/gmd-7-2077-2014).
    """
)
col1a, col1b, col1c = st.columns(3)


with col1a:
    projection = st.selectbox(
        label="projection",
        options=["Equirectangular", "Robinson", "Orthographic"],
        index=0,
        key="user_projection",
        on_change=reset_central_location,
    )
with col1b:
    # if "central_lon" in st.session_state:
    #     del st.session_state["central_lon"]

    if analysis_type == "Single site":
        central_lon_default = float(df_paleo_locations["Eocene (55Ma) lon H14"])
    else:
        central_lon_default = 0.0

    central_lon = st.number_input(
        label="central longitude",
        min_value=-180.0,
        max_value=180.0,
        value=central_lon_default,
        step=1.0,
        format="%.1f",
        key="central_lon",
    )
with col1c:
    # if "central_lat" in st.session_state:
    #     del st.session_state["central_lat"]

    if analysis_type == "Single site" and projection == "Orthographic":
        central_lat_default = float(df_paleo_locations["Eocene (55Ma) lat H14"])
    else:
        central_lat_default = 0.0

    central_lat = st.number_input(
        label="central latitude",
        min_value=-90.0,
        max_value=90.0,
        value=central_lat_default,
        step=1.0,
        format="%.1f",
        key="central_lat",
        disabled=False if projection == "Orthographic" else True,
    )


col2a, col2b, col2c, col2d = st.columns(4)
with col2a:
    outline_colour = st.selectbox(
        label="modern coastline colour",
        options=["none", "gray", "red", "black", "white"],
        index=1,
        key="outline_colour",
    )
with col2b:
    st.write("grid lines")
    grid_check = st.checkbox(label="", key="grid_check", value=True)
with col2c:
    st.write("grid line labels")
    labels_check = st.checkbox(label="", key="labels_check", value=True)
with col2d:
    st.write("site labels")
    sites_check = st.checkbox(label="", key="sites_check", value=False)


fig = plot_global_paleogeography(
    df_paleo_locations,
    projection,
    names,
    outline_colour,
    grid_check,
    labels_check,
    central_lon,
    central_lat,
    sites_check,
)

st.pyplot(fig)

# create Download Buttons for JPG, PNG and PDF
if st.button("Download Map", type="primary", use_container_width=True):

    filename = "deepmip_paleogeography_herold"

    progress_bar = st.progress(0)

    progress_bar.progress(1 / 3, "Creating JPG")
    fn3 =filename + ".jpg"
    img3 = io.BytesIO()
    fig.savefig(img3, format="jpg", dpi=200)


    progress_bar.progress(2 / 3, "Creating PNG")
    fn = filename + ".png"
    img = io.BytesIO()
    fig.savefig(img, format="png", dpi=300)


    progress_bar.progress(3 / 3, "Creating PDF")
    fn2 = filename + ".pdf"
    img2 = io.BytesIO()
    fig.savefig(img2, format="pdf")

    progress_bar.empty()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            label="Download JPG",
            data=img3,
            file_name=fn3,
            mime="image/jpg",
            use_container_width=True,
        )

    with col2:
        st.download_button(
            label="Download PNG",
            data=img,
            file_name=fn,
            mime="image/png",
            use_container_width=True,
        )

    with col3:
        st.download_button(
            label="Download PDF",
            data=img2,
            file_name=fn2,
            mime="image/pdf",
            use_container_width=True,
        )

st.subheader("Individual model geographies")
st.markdown(
    """
        Each model interpolates the original DeepMIP paleogeography from 
        [Herold et al. (2014)](https://doi.org/10.5194/gmd-7-2077-2014)
        onto different grids in the atmosphere and ocean ...
    """
)

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

print(df_paleo_locations)

# fig_models, progress_bar = plot_model_geographies(
fig_models = plot_model_geographies(
    df_paleo_locations[df_paleo_locations.name == site_name],
    projection,
    site_name,
    outline_colour,
    grid_check,
    labels_check,
)

st.pyplot(fig_models)

# create Download Buttons for JPG, PNG and PDF
if st.button("Download Model Maps", type="primary", use_container_width=True):

    filename = "deepmip_model_geographies_herold_" + site_name.replace(" ", "_")

    progress_bar = st.progress(0)

    progress_bar.progress(1 / 2, "Creating JPG")
    fn4 =filename + ".jpg"
    img4 = io.BytesIO()
    fig_models.savefig(img4, format="jpg", dpi=200)

    progress_bar.progress(2 / 2, "Creating PNG")
    fn5 = filename + ".png"
    img5 = io.BytesIO()
    fig_models.savefig(img5, format="png", dpi=300)

    progress_bar.empty()

    col1, col2= st.columns(2)
    with col1:
        st.download_button(
            label="Download JPG",
            data=img4,
            file_name=fn4,
            mime="image/jpg",
            use_container_width=True,
        )

    with col2:
        st.download_button(
            label="Download PNG",
            data=img5,
            file_name=fn5,
            mime="image/png",
            use_container_width=True,
        )
