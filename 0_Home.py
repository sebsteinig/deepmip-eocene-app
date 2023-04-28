import streamlit as st

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import io

from app_modules import init_sidebar

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
)

init_sidebar()

st.write("# Welcome to the DeepMIP model database! 👋")


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

    ### Get in touch
    - 
    """
)

st.markdown("<a href='Extract_model_data' target='_self'>subpage</a>", unsafe_allow_html=True)
