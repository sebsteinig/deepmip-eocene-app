import streamlit as st
import base64

from deepmip_modules import get_csv_data 

def init_widgets_single_site():
    # check whether user input is already in session state
    # if yes, use the previous selection from the session state
    # if not, use default values

    # initialise user input widgets
    with st.form(key="my_form"):
        st.info(
            """
                Select the present-day location of your site and the variable 
                you are interested in.
                """
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            # check whether input has been defined before
            if "modern_lat" in st.session_state:
                # if yes, use previous value
                modern_lat = st.number_input(
                    label="modern latitude of site",
                    min_value=-90.0,
                    max_value=90.0,
                    step=1.0,
                    format="%.1f",
                    key="modern_lat",
                )
            else:
                # if not, use default value
                modern_lat = st.number_input(
                    label="modern latitude of site",
                    min_value=-90.0,
                    max_value=90.0,
                    value=51.5,
                    step=1.0,
                    format="%.1f",
                    key="modern_lat",
                )

        with col2:
            # check whether input has been defined before
            if "modern_lon" in st.session_state:
                # if yes, use previous value
                modern_lon = st.number_input(
                    label="modern longitude of site",
                    min_value=-180.0,
                    max_value=180.0,
                    step=1.0,
                    format="%.1f",
                    key="modern_lon",
                )
            else:
                # if not, use default value
                modern_lon = st.number_input(
                    label="modern longitude of site",
                    min_value=-180.0,
                    max_value=180.0,
                    value=-2.6,
                    step=1.0,
                    format="%.1f",
                    key="modern_lon",
                )

        with col3:
            variable_list = [
                "near-surface air temperature",
                "sea surface temperature",
                "precipitation",
            ]
            if "user_variable" in st.session_state:
                var_index = variable_list.index(st.session_state["user_variable"])
            else:
                var_index = 0

            user_variable = st.selectbox(
                label="variable",
                options=[
                    "near-surface air temperature",
                    "sea surface temperature",
                    "precipitation",
                ],
                index=var_index,
                key="user_variable",
            )

        submit_button = st.form_submit_button(
            label="GET MODEL DATA", use_container_width=True, type="primary"
        )

    return (modern_lat, modern_lon, user_variable)


def reset_csv_data():
    # delete previous input from session state
    if "csv_input" in st.session_state:
        del st.session_state["csv_input"]

def init_widgets_multi_site():
    # check whether user input is already in session state
    # if yes, use the previous selection from the session state
    # if not, use default values

    # st.markdown("")
    template_list = ["custom data",
                     "DeepMIP ocean (all)", 
                     "DeepMIP ocean (latest Paleocene)", 
                     "DeepMIP ocean (Paleocene–Eocene Thermal Maximum)", 
                     "DeepMIP ocean (early Eocene Climatic Optimum)", 
                     "DeepMIP land (all)", 
                     "DeepMIP land (latest Paleocene)", 
                     "DeepMIP land (Paleocene–Eocene Thermal Maximum)", 
                     "DeepMIP land (early Eocene Climatic Optimum)", 
                     "DeepMIP land+ocean (all)", 
                     "DeepMIP land+ocean (latest Paleocene)", 
                     "DeepMIP land+ocean (Paleocene–Eocene Thermal Maximum)", 
                     "DeepMIP land+ocean (early Eocene Climatic Optimum)", 
                     ]
    if "csv_choice" in st.session_state:
        var_index = template_list.index(st.session_state["csv_choice"])
    else:
        var_index = 4

    csv_choice = st.selectbox(
        label="Select from a list of example CSV files from the DeepMIP proxy compilation or enter your own data:",
        options=template_list,
        index=var_index,
        key="csv_choice",
        on_change=reset_csv_data,
    )
    
    csv_data = get_csv_data(csv_choice, False)

    # initialise user input widgets
    with st.form(key="my_form"):

        csv_input = st.text_area(
            label="CSV input of site locations (one per line)",
            value=csv_data,
            placeholder="name, modern latitude, modern longitude",
            height=200, 
            key="csv_input",
        )

        variable_list = [
            "near-surface air temperature",
            "sea surface temperature",
            "precipitation",
        ]
        if "user_variable" in st.session_state:
            var_index = variable_list.index(st.session_state["user_variable"])
        else:
            var_index = 0

        user_variable = st.selectbox(
            label="variable",
            options=[
                "near-surface air temperature",
                "sea surface temperature",
                "precipitation",
            ],
            index=var_index,
            key="user_variable",
        )

        submit_button = st.form_submit_button(
            label="GET MODEL DATA", use_container_width=True, type="primary"
        )

    return (csv_choice, csv_input, user_variable)


# convert locations of single or multiple sites from user input to lists to easily \\
# loop analysis over all chosen sites
def sites_to_list(csv_input):
    modern_lats = []
    modern_lons = []
    names = []
    lines = csv_input.split("\n")  # A list of lines
    for line in lines:
        if line != "":
            name, lat, lon = line.split(",")
            modern_lats.append(float(lat))
            modern_lons.append(float(lon))
            names.append(name)

    return modern_lats, modern_lons, names


def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def add_logo():
    bin_str = get_base64("deepmip_logo.png")
    # bin_str = get_base64('deepmip_banner2.jpg')

    page_bg_img = (
        """
    <style>
        [data-testid="stSidebarNav"] {
            background-image: url("data:image/png;base64,%s");
            background-repeat: no-repeat;
            padding-top: 115px;
            background-position: 70px 30px;
            background-size: 150px 150px;
        }
        [data-testid="stSidebarNav"]::before {
            content: "DeepMIP Eocene Database";
            margin-left: 22px;
            margin-top: 20px;
            font-size:22px;
            position: relative;
            top: 90px;
        }
    </style>
    """
        % bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)


def init_sidebar():
    add_logo()

    st.sidebar.success("How to Get Started")
    st.sidebar.markdown(
        """
        1. ☝️ Use the navigation above to select the analysis of your choice. 
        2. Select the present-day location of your site and the variable you are 
        interested in.
        3. Optionally, you can add a proxy estimate for quick comparison with 
        the model data. 
        4. Click 'Get Data' and wait for the results to update.
        """
    )

    st.sidebar.subheader("Links")
    st.sidebar.markdown(
        "Get the code: [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/sebsteinig/deepmip_database_app)",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        "Get in touch: [![Repo](https://badgen.net/badge/icon/sebsteinig?icon=twitter&label)](https://twitter.com/sebsteinig)",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        # "Get more info: [www.deepmip.org](https://www.deepmip.org)",
        "Get more info: [![Repo](https://badgen.net/badge/icon/deepmip.org?icon=chrome&label)](https://www.deepmip.org)",
        unsafe_allow_html=True,
    )

    # fix sidebar width
    # css = """
    # <style>
    #     [data-testid="stSidebar"]{
    #         min-width: 300px;
    #         max-width: 300px;
    #     }
    # </style>
    # """
    # st.markdown(css, unsafe_allow_html=True)
