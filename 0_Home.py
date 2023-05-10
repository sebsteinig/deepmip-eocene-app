import streamlit as st

from app_modules import init_sidebar
from deepmip_modules import model_table
from bibliography import init_bibliography

st.set_page_config(
    page_title="Home",
    layout="wide",
)

init_sidebar()

st.write("# Welcome to the DeepMIP-Eocene model database! 👋")

st.markdown(
    """
    The **D**eep **T**ime **M**odel **I**ntercomparison **P**roject (DeepMIP)-Eocene
    is a collaboration of eight climate modelling groups from around the world, 
    each carrying out standardised simulations of the early Eocene climate optimum 
    (EECO, ∼ 50 million years ago). All generated data is freely available to
    everyone. There are two main ways to access the data:
    1. This website provides an interface to extract point data from all available 
    simulations for quick and easy and comparison with local proxy data.
    2. The full database (size: TBC) can be downloaded from the CEDA Archive (link)
    to follow.

    ###  How to Get Started
    Select any of the following pages to start your analysis:

    - <a href='Extract_model_data' target='_self'>Extract model data</a> for any location, ready to be imported into your spreadsheet.
    - <a href='Plot_model_data' target='_self'>Plot model data</a> (monthly, seasonal, annual) and it's relation to CO$_2$ and global mean temperature.
    - <a href='Paleogeography' target='_self'>Create paleogeographic maps </a> for your site and see how it is represented in different models.

    """,
    unsafe_allow_html=True,
)

st.subheader("DeepMIP Models")
st.markdown(
    """
    An overview of all participating models and their available simulations is given below.

    """
)
st.dataframe(model_table(), use_container_width=False)


st.markdown(
    """
    ### Want to learn more?
    - DeepMIP experimental design paper: 
    [Lunt et al. (2017)](https://doi.org/10.5194/gmd-10-889-2017)
    - Large-scale climate features in the simulations: 
    [Lunt et al. (2021)](https://doi.org/10.5194/cp-17-203-2021)
    - Overview of the DeepMIP database 
    [in prep.](https://doi.org/10.5194/cp-17-203-2021)
    - Official [DeepMIP website](https://www.deepmip.org)
    - Model description papers:
        - CESM1.2_CAM5: [Zhu et al., (2019)](https://doi.org/10.1126/sciadv.aax1874)
        - IPSLCM5A2: [Zhang et al., (2020)](https://doi.org/10.5194/cp-16-1263-2020)
        - all other: [Lunt et al. (2021)](https://doi.org/10.5194/cp-17-203-2021)

    ### Publications
    The DeepMIP model data from this database have been used in the following publications: 

    """
)

init_bibliography()
