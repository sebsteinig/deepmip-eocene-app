import streamlit as st
import pandas as pd
import matplotlib as plt

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
    directory structure can be accessed via the link below and files can be downloaded via HTTP, 
    Wget, FTP or OPeNDAP. This allows easy access to the data via the browser, as well as 
    scriptable interfaces for bulk downloading. The OPeNDAP (Open-source Project for a 
    Network Data Access Protocol) protocol allows the remote subsetting and exploration of 
    datasets directly in Python, R, IDL, and Matlab. The 
    [CEDA Archive website](https://help.ceda.ac.uk/article/99-download-data-from-ceda-archives) 
    gives an up to date overview of all available access options.    
    """,
    unsafe_allow_html=True,
)
url_ceda = "https://catalogue.ceda.ac.uk/uuid/95aa41439d564756950f89921b6ef215"

st.image("img/ceda_archive_logo_transp_white_3_h80.png")

st.link_button(
    "Download global netCDF data from CEDA Archive",
    url_ceda,
    type="primary",
    disabled=False,
)

st.subheader("Batch downloading with Wget")

st.markdown(
    """
            [wget](https://www.gnu.org/software/wget/) is the easiest option to download large parts 
            or the whole database (168.0 GB). The following command will download the entire data 
            set to the current directory on your local machine:
            """
)
code1 = """
    wget -e robots=off --mirror --no-parent -r -c https://dap.ceda.ac.uk/badc/cmip6/data/CMIP6Plus/DeepMIP/deepmip-eocene-p1/
    """
st.code(code1, language="bash")

st.markdown("Or only download the climatological mean files:")
code2 = """
    wget -e robots=off --mirror --no-parent -r --reject "*.time_series.nc,*.std.nc" https://dap.ceda.ac.uk/badc/cmip6/data/CMIP6Plus/DeepMIP/deepmip-eocene-p1/
    """
st.code(code2, language="bash")

st.markdown("Or you can only download specific variables with:")
code3 = """
    wget -e robots=off --mirror --no-parent -r --accept "tas_*mean.nc,pr_*mean.nc" https://dap.ceda.ac.uk/badc/cmip6/data/CMIP6Plus/DeepMIP/deepmip-eocene-p1/    
    """
st.code(code3, language="bash")
