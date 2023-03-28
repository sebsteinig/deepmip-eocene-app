import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from app_modules import init_widgets
from deepmip_modules import get_paleo_location_herold

st.title('DeepMIP database point data')

# for k, v in st.session_state.items():
#     st.session_state[k] = v

# modern_lat = st.sidebar.number_input('site modern latitude', -90, 90, value=st.session_state['modern_lat'], key="modern_lat")
# modern_lon = st.sidebar.number_input('site modern longitude', -180, 180, value=st.session_state['modern_lon'], key="modern_lon")
# values = ["near-surface air temperature", "sea surface temperature", "precipitation"]
# default_ix = values.index(st.session_state['user_variable'])
# user_variable  = st.sidebar.selectbox("user_variable", values, index=default_ix, key="user_variable")

modern_lat, modern_lon, user_user_variable = init_widgets()

# for v in [modern_lat, modern_lon, user_user_variable]:
#     st.session_state.v = v

## step 1: find paleoposition for DeepMIP model geography   
# paleoLat, paleoLon = get_paleo_location_herold(modern_lat, modern_lon)


# st.write("PLAT: " + str(paleoLat))
# st.write("PLON: " + str(paleoLon))

# fig, ax = plt.subplots(subplot_kw=dict(projection=ccrs.Robinson()))

# rotationFile.LAT.plot(ax=ax, transform=ccrs.PlateCarree())

# st.pyplot(fig)
