import streamlit as st
import base64

def init_widgets():

    st.subheader('User input')

    # check whether user input is already in session state
    # if yes, use the previous selection from the session state
    # if not, use default values 

    # initialise input widgets in sidebar
    with st.form(key='my_form'):

        st.info('''
                Select the present-day location of your site, the variable 
                you are interested in and an optional proxy reference for 
                the plots.
                ''')

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
            
        col4, col5, col6, col7 = st.columns(4)

        with col4:
            st.write("compare to proxy?")
            if 'modern_lat' in st.session_state:
                proxy_check  = st.checkbox(
                        label       = ' ', 
                        key         = "proxy_check")
            else:
                proxy_check  = st.checkbox(
                        label       = ' ', 
                        key         = "proxy_check",
                        value       = True)
        with col5:
            proxy_mean  = st.number_input(
                    label       = 'proxy mean', 
                    value       = 24.0,
                    step        = 1.0, 
                    format      = "%.1f", 
                    key         = "proxy_mean")
                    
        with col6:
            proxy_std  = st.number_input(
                    label       = 'proxy uncertainty', 
                    value       = 5.0,
                    step        = 1.0, 
                    format      = "%.1f", 
                    key         = "proxy_std")

        with col7:
            proxy_label  = st.text_input(
                    label       = 'proxy label', 
                    value       = 'Bristol dummy',
                    key         = "proxy_label")
                                              
        submit_button   = st.form_submit_button(
                        label               = 'Get Data',
                        use_container_width = True)



    return modern_lat, modern_lon, user_variable, proxy_check, proxy_mean, proxy_std, proxy_label


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
def add_logo():
    bin_str = get_base64('deepmip_logo.png')
    # bin_str = get_base64('deepmip_banner2.jpg')

    page_bg_img = """
    <style>
        [data-testid="stSidebarNav"] {
            background-image: url("data:image/png;base64,%s");
            background-repeat: no-repeat;
            padding-top: 115px;
            background-position: 45px 30px;
            background-size: 150px 150px;
        }
        [data-testid="stSidebarNav"]::before {
            content: "DeepMIP database";
            margin-left: 23px;
            margin-top: 20px;
            font-size:22px;
            position: relative;
            top: 90px;
        }
    </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def init_sidebar():
    add_logo()
    # st.sidebar.success("Select analysis above.")
    # st.sidebar.image("deepmip_logo.png", use_column_width=True)

    # Add Link to your repo
    '''
    [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/AvratanuBiswas/PubLit) 

    '''
    st.sidebar.subheader('Links')
 
    st.sidebar.markdown("Get the code: [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/sebsteinig/deepmip_database_app)",unsafe_allow_html=True)
    st.sidebar.markdown("Get in touch: [![Repo](https://badgen.net/badge/icon/sebsteinig?icon=twitter&label)](https://twitter.com/sebsteinig)",unsafe_allow_html=True )
    st.sidebar.markdown("[www.deepmip.org](https://www.deepmip.org)",unsafe_allow_html=True)

   
