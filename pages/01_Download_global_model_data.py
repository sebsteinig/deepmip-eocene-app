import streamlit as st
import pandas as pd
import io
import matplotlib as plt
import webbrowser

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
    Global fields of model output are stored on the CEDA Archive. You can download the data by clicking the button below: 
    
    """,
    unsafe_allow_html=True,
)
url = 'https://www.streamlit.io/'

if st.button('Download global data from CEDA Archive (link to follow once approved)', type="primary"):
    webbrowser.open_new_tab(url)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("img/ceda_archive_logo_transp_white_3_h80.png", width=400)
with col2:
    st.image("img/core-trust-seal-px-300_height.jpeg", width=100)
