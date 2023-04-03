import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import holoviews as hv

from deepmip_dicts import variable_dict

from app_modules import init_widgets, init_sidebar

from deepmip_modules import get_paleo_location_herold, get_model_point_data, box_whisker_plot

st.title('Analyse model point data')

init_sidebar()

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-Get Data":
        st.session_state[k] = v

modern_lat, modern_lon, user_variable, proxy_check, proxy_mean, proxy_std, proxy_label = init_widgets()

for v in [modern_lat, modern_lon, user_variable, proxy_check, proxy_mean, proxy_std, proxy_label]:
    st.session_state.v = v

## step 1: get paleo position consistent with DeepMIP model geography   

df_locations = get_paleo_location_herold(modern_lat, modern_lon)

## step 2: get model data for paleo position(s) and chosen variable

# convert user variable to DeepMIP variable name
for variable in variable_dict.keys():
    if variable_dict[variable]['longname'] == user_variable:
        deepmip_var = variable

df_model = get_model_point_data(
            float(df_locations['modern lat']), 
            float(df_locations['modern lon']),
            float(df_locations['Eocene (55Ma) lat']),
            float(df_locations['Eocene (55Ma) lon']),
            deepmip_var)




var_y   = st.selectbox(
                label       = "y-axis variable", 
                options     = ["annual_mean", "monthly_min", "monthly_max", "DJF", "MAM", "JJA", "SON", "Jan", "Feb", "Mar", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                key         = "y_axis")
    
bokeh_composition1 = box_whisker_plot(df_model, var_y, 'experiment', proxy_check, proxy_mean, proxy_std, proxy_label)
st.bokeh_chart(hv.render(bokeh_composition1, backend='bokeh'))

    
bokeh_composition2 = box_whisker_plot(df_model, var_y, 'CO2', proxy_check, proxy_mean, proxy_std, proxy_label)
st.bokeh_chart(hv.render(bokeh_composition2, backend='bokeh'))
    
bokeh_composition3 = box_whisker_plot(df_model, var_y, 'GMST', proxy_check, proxy_mean, proxy_std, proxy_label)
st.bokeh_chart(hv.render(bokeh_composition3, backend='bokeh'))



