import streamlit as st
import pandas as pd
import io
import matplotlib as plt

from deepmip_dicts import variable_dict

from app_modules import (
    init_widgets_single_site,
    init_widgets_multi_site,
    init_sidebar,
    sites_to_list,
)
from deepmip_modules import get_paleo_locations, get_model_point_data

st.set_page_config(
    page_title="Get model data",
    layout="wide",
)

init_sidebar()

st.title("Get model point data")

st.markdown(
    """
**Get all available model data for a variable of your choice anywhere on the globe.**
The app calculates the respective early Eocene (~55 Ma) paleolocation consistent with the 
model geographies and then extracts the data from the closest grid point for all available 
models and simulations. Results are listed in the interactive table below, which can also 
be downloaded in different data formats. You can also create interactive charts of your 
extracted data on the <a href='Plot_site_comparison' target='_self'>analysis page</a>.

The full database with the global netCDF output (size: TBC) can be downloaded from the CEDA Archive (link
to follow).
    """,
    unsafe_allow_html=True,
)

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-GET MODEL DATA":
        st.session_state[k] = v

st.subheader("User input")

analysis_options = ["Single site", "Multiple sites"]
if "analysis_type" in st.session_state:
    var_index = analysis_options.index(st.session_state["analysis_type"])
else:
    var_index = 0

analysis_type = st.radio(
    "Number of sites to extract data for:",
    analysis_options,
    horizontal=True,
    index=var_index,
    key="analysis_type",
)

# create user inputs for single site
if analysis_type == "Single site":
    modern_lat, modern_lon, user_variable, user_site_name = init_widgets_single_site()

    for v in [modern_lat, modern_lon, user_variable, user_site_name, analysis_type]:
        st.session_state.v = v

# create user inputs for multiple sites (i.e. CSV input)
elif analysis_type == "Multiple sites":
    csv_choice, csv_input, user_variable = init_widgets_multi_site()
    modern_lats, modern_lons, names, proxy_means, proxy_stds = sites_to_list(csv_input)

    for v in [csv_input, csv_choice, user_variable, analysis_type]:
        st.session_state.v = v

if user_variable == "sea surface temperature":
    st.warning(
        """
        ⚠️ Warning: Land points for sea surface temperatures (SSTs) are filled
        by a nearest-neighbour lookup to facilitate the intermodel
        comparison in coastal regions. Please make sure that you selected
        a marine/coastal location by checking the model land-sea masks
        on the **Paleogeography** page.
        """
    )

if analysis_type == "Single site":
    # convert single site to list for consistency with multi-site analysis
    modern_lats = [modern_lat]
    modern_lons = [modern_lon]
    names = [user_site_name]

## step 1: get paleo position(s) consistent with DeepMIP model geographies
df_paleo_locations = get_paleo_locations(modern_lats, modern_lons, names)

# step 2: convert user variable to DeepMIP variable name
for key, value in variable_dict.items():
    if value["longname"] == user_variable:
        deepmip_var = key

## step 3: get model data for paleo position(s) and chosen variable
df_model = get_model_point_data(df_paleo_locations, deepmip_var)

# add donwload buttons for CSV and XLSX
# from https://stackoverflow.com/a/75334543
buffer = io.BytesIO()

@st.cache_data
def convert_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode("utf-8")


@st.cache_data
def convert_to_json(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_json().encode("utf-8")


tab = st.container()
st.subheader("Extracted model data")

# display the dataframe on streamlit app
st.write(df_model)

col1, col2, col3 = st.columns(3)

# replace missing values with fill value of -999.9 for data export
# df_model = df_model.fillna(-999.9)

with col1:
    csv = convert_to_csv(df_model)
    # download button 1 to download dataframe as csv
    download1 = st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="deepmip_model_point_data.csv",
        mime="text/csv",
        use_container_width=True,
    )

with col2:
    # download button 2 to download dataframe as xlsx
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        # Write each dataframe to a different worksheet.
        df_model.to_excel(writer, sheet_name="Sheet1", index=False)
        # Close the Pandas Excel writer and output the Excel file to the buffer
        writer.save()

        download2 = st.download_button(
            label="Download data for Excel",
            data=buffer,
            file_name="deepmip_model_point_data.xlsx",
            mime="application/vnd.ms-excel",
            use_container_width=True,
        )

with col3:
    json = convert_to_json(df_model)
    # download button 1 to download dataframe as csv
    download1 = st.download_button(
        label="Download data as JSON",
        data=json,
        file_name="deepmip_model_point_data.json",
        mime="text/csv",
        use_container_width=True,
    )
