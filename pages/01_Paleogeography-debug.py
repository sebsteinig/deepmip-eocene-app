import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import io

from app_modules import init_widgets
from deepmip_modules import get_paleo_location_herold, plot_paleogeography

st.title('DeepMIP database point data')

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-Update":
        st.session_state[k] = v

modern_lat, modern_lon, user_user_variable = init_widgets()

for v in [modern_lat, modern_lon, user_user_variable]:
    st.session_state.v = v

# step 1: get paleo position consistent with DeepMIP model geography   

df_locations = get_paleo_location_herold(modern_lat, modern_lon)
st.dataframe(df_locations.style.format("{:.1f}"))

# fig_geo = plot_paleogeography(df_locations, "global")

# fig, ax = plt.subplots(subplot_kw=dict(projection=ccrs.Robinson()))

# rotationFile.LAT.plot(ax=ax, transform=ccrs.PlateCarree())

# st.pyplot(fig_geo)

# fn = 'scatter.png'
# img = io.BytesIO()
# plt.savefig(img, format='png')

# btn = st.download_button(
#    label="Download image",
#    data=img,
#    file_name=fn,
#    mime="image/png"
# )
