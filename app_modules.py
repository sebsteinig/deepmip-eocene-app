import streamlit as st

def init_widgets():

    # check whether user input is already in session state
    # if yes, use the previous selection from the session state
    # if not, use default values 
    if 'modern_lat' in st.session_state:
        lat_value = st.session_state['modern_lat']
    else:
        lat_value = 54.5

    if 'modern_lon' in st.session_state:
        lon_value = st.session_state['modern_lon']
    else:
        lon_value = -2.6

    variable_list = ["near-surface air temperature", "sea surface temperature", "precipitation"]
    if 'user_variable' in st.session_state:
        var_index = variable_list.index(st.session_state['user_variable'])
    else:
        var_index = 0

    with st.sidebar.form(key='my_form'):

        # initialise input widgets in sidebar
        modern_lat  = st.number_input(
                    label       = 'modern latitude of site', 
                    min_value   = -90.0,
                    max_value   = 90.0, 
                    value       = lat_value, 
                    step        = 1.0, 
                    format      = "%.1f", 
                    key         = "modern_lat")
                    
        modern_lon  = st.number_input(
                    label       = 'modern longitude of site', 
                    min_value   = -180.0, 
                    max_value   = 180.0, 
                    value       = lon_value, 
                    step        = 1.0, 
                    format      = "%.1f", 
                    key         = "modern_lon")

        user_variable   = st.selectbox(
                        label       = "variable", 
                        options     = ["near-surface air temperature", "sea surface temperature", "precipitation"],
                        index       =  var_index,
                        key         = "user_variable")

        submit_button   = st.form_submit_button(label       = 'Update')



    return modern_lat, modern_lon, user_variable
