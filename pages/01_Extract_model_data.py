import streamlit as st
import pandas as pd
import io

from deepmip_dicts import variable_dict

from app_modules import init_widgets, init_sidebar
from deepmip_modules import get_paleo_location_herold, get_model_point_data, location_data_boxplot

st.title('Extract model point data')

st.markdown('''
            **Get all available model data for a variable of your choice anywhere on the globe.**
            The app calculates the respective early Eocene (~55 Ma) paleolocation consistent with the 
            model geographies and then extracts the data from the closest grid point for all available 
            models and simulations. Results are listed in the interactive table below, which can also 
            be downloaded in different data formats. Basic ensemble statistics of the extracted data 
            are shwon at the bottom.
            ''')

st.markdown("<a href='Extract_model_data' target='_self'>subpage</a>", unsafe_allow_html=True)
st.write('sda')

init_sidebar()

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-Get Data":
        st.session_state[k] = v

modern_lat, modern_lon, user_variable = init_widgets()

for v in [modern_lat, modern_lon, user_variable]:
    st.session_state.v = v

## step 1: get paleo position consistent with DeepMIP model geography   

df_locations = get_paleo_location_herold(modern_lat, modern_lon)

## step 2: get model data for paleo position(s) and chosen variable

# convert user variable to DeepMIP variable name
for key, value in variable_dict.items():
    if value['longname'] == user_variable:
        deepmip_var = key

df_model = get_model_point_data(
            float(df_locations['modern lat']), 
            float(df_locations['modern lon']),
            float(df_locations['Eocene (55Ma) lat']),
            float(df_locations['Eocene (55Ma) lon']),
            deepmip_var)

# add donwload buttons for CSV and XLSX
# from https://stackoverflow.com/a/75334543
buffer = io.BytesIO()

@st.cache_data
def convert_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

@st.cache_data
def convert_to_json(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_json().encode('utf-8')

tab = st.container()
st.subheader('Extracted model data')

# display the dataframe on streamlit app
st.write(df_model)

col1, col2, col3 = st.columns(3)

with col1:
    csv = convert_to_csv(df_model)
    # download button 1 to download dataframe as csv
    download1 = st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='deepmip_model_point_data.csv',
        mime='text/csv',
        use_container_width=True
    )

with col2:
    # download button 2 to download dataframe as xlsx
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet.
        df_model.to_excel(writer, sheet_name='Sheet1', index=False)
        # Close the Pandas Excel writer and output the Excel file to the buffer
        writer.save()

        download2 = st.download_button(
            label="Download data as Excel",
            data=buffer,
            file_name='deepmip_model_point_data.xlsx',
            mime='application/vnd.ms-excel',
            use_container_width=True
        )

with col3:
    json = convert_to_json(df_model)
    # download button 1 to download dataframe as csv
    download1 = st.download_button(
        label="Download data as JSON",
        data=json,
        file_name='deepmip_model_point_data.json',
        mime='text/csv',
        use_container_width=True
    )


st.subheader('Overview statistics of extracted data')

fig = location_data_boxplot(df_model, deepmip_var)

st.pyplot(fig) 