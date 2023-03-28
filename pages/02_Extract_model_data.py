import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from app_modules import init_widgets
from deepmip_modules import get_paleo_location_herold, get_model_point_data, location_data_boxplot

st.title('DeepMIP database point data')

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-Update":
        st.session_state[k] = v

modern_lat, modern_lon, user_variable = init_widgets()

for v in [modern_lat, modern_lon, user_variable]:
    st.session_state.v = v

## step 1: get paleo position consistent with DeepMIP model geography   

df_locations = get_paleo_location_herold(modern_lat, modern_lon)

## step 2: get model data for paleo position(s) and chosen variable

# convert user variable to DeepMIP variable name
if user_variable == 'near-surface air temperature':
    deepmip_var = 'tas'
elif user_variable == 'sea surface temperature':
    deepmip_var = 'tas'
elif user_variable == 'precipitation':
    deepmip_var = 'pr'

df_model = get_model_point_data(
            float(df_locations['modern lat']), 
            float(df_locations['modern lon']),
            float(df_locations['Eocene (55Ma) lat']),
            float(df_locations['Eocene (55Ma) lon']),
            deepmip_var)

# st.dataframe(df_model.style.format("{:.1f}"))
st.dataframe(df_model)

# plot results with seaborn

fig = location_data_boxplot(df_model, deepmip_var)

st.pyplot(fig)

