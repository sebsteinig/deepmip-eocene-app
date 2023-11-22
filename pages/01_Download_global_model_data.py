import streamlit as st
import pandas as pd
import matplotlib as plt

from deepmip_dicts import variable_dict

from app_modules import init_sidebar

st.set_page_config(
    page_title="Download global model data",
    layout="wide",
)

init_sidebar()

st.title("Download global model data")


st.markdown(
    """
    Processed netCDF files for all simulations are available from the CEDA Archive. The full 
    directory structure can be accessed via the browser and files can be downloaded via HTTP, 
    Wget, FTP or OPeNDAP. This allows easy access to the data via the browser, as well as 
    scriptable interfaces for bulk downloading. The OPeNDAP (Open-source Project for a 
    Network Data Access Protocol) protocol allows the remote subsetting and exploration of 
    datasets directly in Python, R, IDL, and Matlab. The 
    [CEDA Archive website](https://help.ceda.ac.uk/article/99-download-data-from-ceda-archives) 
    gives an up to date overview of all available access options.    
    """,
    unsafe_allow_html=True,
)
url_ceda = "https://www.streamlit.io/"
url_onedrive = "https://drive.google.com/drive/folders/1dH-OxAQi4eI0US6LlPrN8pfAYxNAEv0M?usp=share_link"

st.link_button(
    "Download global data from CEDA Archive (link to follow once approved)",
    url_ceda,
    type="primary",
    disabled=True,
)

st.image("img/ceda_archive_logo_transp_white_3_h80.png")

st.markdown(
    """
    The link to the CEDA archive will be available once the peer review of the associated 
    database paper has been completed. In the meantime, the data can be downloaded from
    the Google Drive link below. The data is organised in the same way as on the CEDA archive.
    """,
    unsafe_allow_html=True,
)
st.link_button(
    "Download global data from Google Drive",
    url_onedrive,
    type="primary",
)
