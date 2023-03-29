import streamlit as st

def init_widgets():

    st.subheader('User input')

    # check whether user input is already in session state
    # if yes, use the previous selection from the session state
    # if not, use default values 

    # initialise input widgets in sidebar
    with st.form(key='my_form'):

        st.info("Select the present-day location of your site and the variable you are interested in.")

        col1, col2, col3 = st.columns(3)

        with col1:
            # check whether input has been defined before
            if 'modern_lat' in st.session_state:
                # if yes, use previous value
                modern_lat  = st.number_input(
                            label       = 'modern latitude of site', 
                            min_value   = -90.0,
                            max_value   = 90.0, 
                            step        = 1.0, 
                            format      = "%.1f", 
                            key         = "modern_lat")
            else:
                # if not, use default value
                modern_lat  = st.number_input(
                            label       = 'modern latitude of site', 
                            min_value   = -90.0,
                            max_value   = 90.0, 
                            value       = 54.5, 
                            step        = 1.0, 
                            format      = "%.1f", 
                            key         = "modern_lat")

        with col2:
            # check whether input has been defined before
            if 'modern_lon' in st.session_state:
            # if yes, use previous value                  
                modern_lon  = st.number_input(
                            label       = 'modern longitude of site', 
                            min_value   = -180.0, 
                            max_value   = 180.0, 
                            step        = 1.0, 
                            format      = "%.1f", 
                            key         = "modern_lon")
            else:
                # if not, use default value
                modern_lon  = st.number_input(
                            label       = 'modern longitude of site', 
                            min_value   = -180.0, 
                            max_value   = 180.0, 
                            value       = -2.6, 
                            step        = 1.0, 
                            format      = "%.1f", 
                            key         = "modern_lon")
            

        with col3:
            variable_list = ["near-surface air temperature", "sea surface temperature", "precipitation"]
            if 'user_variable' in st.session_state:
                var_index = variable_list.index(st.session_state['user_variable'])
            else:
                var_index = 0

            user_variable   = st.selectbox(
                            label       = "variable", 
                            options     = ["near-surface air temperature", "sea surface temperature", "precipitation"],
                            index       =  var_index,
                            key         = "user_variable")
        submit_button   = st.form_submit_button(
                        label               = 'Get Data',
                        use_container_width = True)



    return modern_lat, modern_lon, user_variable

def init_sidebar():
    st.sidebar.success("Select analysis above.")
    st.sidebar.image("deepmip_logo.png", use_column_width=True)