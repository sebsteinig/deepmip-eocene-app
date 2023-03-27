import streamlit as st

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import io

from app_modules import init_widgets

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-Update":
        st.session_state[k] = v

# modernLat = st.sidebar.number_input('site modern latitude', min_value=-90.0, max_value=90.0, value = 51.5, step=1.0, format="%.1f", key="modernLat")
# modernLon = st.sidebar.number_input('site modern longitude', min_value=-180.0, max_value=180.0, value = -2.6, step=1.0, format="%.1f", key="modernLon")
# variable  = st.sidebar.selectbox("variable", ["near-surface air temperature", "sea surface temperature", "precipitation"], key="variable")

modern_lat, modern_lon, user_variable = init_widgets()

for v in [modern_lat, modern_lon, user_variable]:
    st.session_state.v = v


# st.session_state['modernLat'] = modernLat
# st.session_state['modernLon'] = modernLon
# st.session_state['variable'] = variable

st.write("# Welcome to the DeepMIP model databse! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    The **D**eep **T**ime **M**odel **I**ntercomparison **P**roject (DeepMIP)
    model database contains an ensemble of eight climate models, each carrying
    out standardised simulations of the early Eocene climate optimum 
    (EECO, ∼ 50 million years ago). This website provides an interface to 
    extract point data from all available simulations for easy comparison with 
    local proxy data.

    ###  How to Get Started
    1. 👈 Use the sidebar on the left for all user input (you might have to 
    click the 'less than symbol' on the top left to expand it).
    2. Select the present-day location of your site and the variable you are 
    interested in.
    3. Click on the analysis of your choice.

    ### Want to learn more?
    - DeepMIP experimental design paper: [Lunt et al. (2017)](https://doi.org/10.5194/gmd-10-889-2017)
    - Large-scale climate features in the simulations: [Lunt et al. (2021)](https://doi.org/10.5194/cp-17-203-2021)
    - Overview of the DeepMIP database [in prep.](https://doi.org/10.5194/cp-17-203-2021)
    - Official [DeepMIP website](https://www.deepmip.org)

    ### DeepMIP publications
    - 

    ### Get in contact
    - 
"""
)
