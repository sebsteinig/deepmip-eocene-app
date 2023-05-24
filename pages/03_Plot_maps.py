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

analysis_type = st.radio(
    "Number of sites to plot:",
    analysis_options,
    horizontal=True,
    index=var_index,
    key="analysis_type",
)

# create user inputs for single site
if analysis_type == "Single site":
    modern_lat, modern_lon, user_site_name = init_widgets_single_site_map()

    for v in [modern_lat, modern_lon, user_site_name, analysis_type]:
        st.session_state.v = v

# create user inputs for multiple sites (i.e. CSV input)
elif analysis_type == "Multiple sites":
    csv_choice, csv_input = init_widgets_multi_site_map()
    modern_lats, modern_lons, names, proxy_means, proxy_stds = sites_to_list(csv_input)

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
col1, col2, col3, col4 = st.columns(4)

with col1:
    projection = st.selectbox(
        label="projection",
        options=["Equirectangular", "Robinson", "Orthographic"],
        index=0,
        key="user_projection",
    )
with col2:
    outline_colour = st.selectbox(
        label="modern coastline colour",
        options=["none", "gray", "red", "black", "white"],
        index=1,
        key="outline_colour",
    )
with col3:
    st.write("grid lines")
    grid_check = st.checkbox(label="", key="grid_check", value=True)
with col4:
    st.write("grid line labels")
    labels_check = st.checkbox(label="", key="labels_check", value=True)

print(df_paleo_locations)
fig = plot_global_paleogeography(
    df_paleo_locations,
    projection,
    names,
    outline_colour,
    grid_check,
    labels_check,
)

# Create an in-memory buffer
buffer = io.BytesIO()

fn = "deepmip_paleogeography_herold.png"
img = io.BytesIO()
fig.savefig(img, format="png", dpi=200)

fn2 = "deepmip_paleogeography_herold.pdf"
img2 = io.BytesIO()
fig.savefig(img2, format="pdf")

fn3 = "deepmip_paleogeography_herold.jpg"
img3 = io.BytesIO()
fig.savefig(img3, format="jpg", dpi=200)

st.pyplot(fig)

col4, col5, col6 = st.columns(3)

with col4:
    st.download_button(
        label="Download JPG",
        data=img3,
        file_name=fn3,
        mime="image/jpg",
        use_container_width=True,
    )

with col5:
    st.download_button(
        label="Download PNG",
        data=img,
        file_name=fn,
        mime="image/png",
        use_container_width=True,
    )

with col6:
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

fig_models, progress_bar = plot_model_geographies(
    df_paleo_locations[df_paleo_locations.name == site_name],
    projection,
    site_name,
    outline_colour,
    grid_check,
    labels_check,
)

st.pyplot(fig_models)

progress_bar.empty()


# Create an in-memory buffer
# buffer = io.BytesIO()

# fn4 = 'deepmip_paleogeography_herold.png'
# img4 = io.BytesIO()
# fig_models.savefig(img4, format='png')

# fn5 = 'deepmip_paleogeography_herold.pdf'
# img5 = io.BytesIO()
# fig_models.savefig(img5, format='pdf')

# fn6 = 'deepmip_paleogeography_herold.jpg'
# img6 = io.BytesIO()
# fig_models.savefig(img6, format='jpg')

# # st.pyplot(fig_models)

# col7, col8, col9 = st.columns(3)

# with col7:
#     st.download_button(
#     label="Download JPG",
#     data=img6,
#     file_name=fn6,
#     mime="image/jpg",
#     use_container_width=True
#     )

# with col8:
#     st.download_button(
#     label="Download PNG",
#     data=img4,
#     file_name=fn4,
#     mime="image/png",
#     use_container_width=True
#     )

# with col9:
#     st.download_button(
#     label="Download PDF",
#     data=img6,
#     file_name=fn6,
#     mime="image/pdf",
#     use_container_width=True
#     )
