import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import holoviews as hv
import io

from deepmip_dicts import variable_dict

from app_modules import init_widgets, init_sidebar

from deepmip_modules import (
    get_paleo_locations,
    get_model_point_data,
    box_whisker_plot,
)

st.set_page_config(
    page_title="Plot model data",
    layout="wide",
)

st.title("Plot model point data")

st.markdown(
    """
        **Interactive overview of the extracted model data.**
        The app calculates the respective early Eocene (~55 Ma) paleolocation consistent with the 
        model geographies and then extracts the data from the closest grid point for all available 
        models and simulations. You can download the extracted data in different data formats 
        at the <a href='Extract_model_data' target='_self'>extraction page</a>.
    """,
    unsafe_allow_html=True,
)

init_sidebar()

for k, v in st.session_state.items():
    if k != "FormSubmitter:my_form-Get Data":
        st.session_state[k] = v

(
    modern_lat,
    modern_lon,
    user_variable,
    proxy_check,
    proxy_mean,
    proxy_std,
    proxy_label,
) = init_widgets()

for v in [
    modern_lat,
    modern_lon,
    user_variable,
    proxy_check,
    proxy_mean,
    proxy_std,
    proxy_label,
]:
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

## step 1: get paleo position consistent with DeepMIP model geography
df_locations = get_paleo_locations(modern_lat, modern_lon)

## step 2: get model data for paleo position(s) and chosen variable

# convert user variable to DeepMIP variable name
for variable in variable_dict.keys():
    if variable_dict[variable]["longname"] == user_variable:
        deepmip_var = variable

# df_model = get_model_point_data(
#             float(df_locations['modern lat']),
#             float(df_locations['modern lon']),
#             float(df_locations['Eocene (55Ma) lat H14']),
#             float(df_locations['Eocene (55Ma) lon H14']),
#             deepmip_var)


df_model = get_model_point_data(df_locations, deepmip_var)


var_y = st.selectbox(
    label="y-axis variable",
    options=[
        "annual_mean",
        "monthly_min",
        "monthly_max",
        "DJF",
        "MAM",
        "JJA",
        "SON",
        "Jan",
        "Feb",
        "Mar",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
    key="y_axis",
)

st.subheader(var_y + " vs. experiment")
bokeh_composition1 = box_whisker_plot(
    df_model,
    var_y,
    "experiment",
    proxy_check,
    proxy_mean,
    proxy_std,
    proxy_label,
)

from bokeh.io import export_svgs

p = hv.render(bokeh_composition1, backend="bokeh")
st.bokeh_chart(p)

p.output_backend = "svg"
export_svgs(p, filename="heatmap.svg")

# p.output_backend = "png"
# export_svgs(p, filename="heatmap.png")

hv.save(bokeh_composition1, "penguin_plot.png", fmt="png")

with open("heatmap.svg", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="heatmap.svg",
        mime="image/svg",
    )
# hv.save(p, "penguin_plot.png", fmt="png")
# @st.cache
# def export_svg(obj, filename):
#     plot_state = hv.renderer("bokeh").get_plot(obj).state
#     plot_state.output_backend = "svg"
#     export_svgs(plot_state, filename=filename)


# # Create an in-memory buffer
# # buffer = io.BytesIO()

# # fn = "deepmip_boxplot.png"
# # img = io.BytesIO()
# # fig.savefig(img, format="png")
# # hv.save(bokeh_composition1, "penguin_plot.png", fmt="png")

# fn = "overlay.svg"
# img = io.BytesIO()
# image = export_svg(bokeh_composition1, img)

# st.download_button(
#     label="Download SVG",
#     data=image,
#     file_name=fn,
#     mime="image/svg",
#     use_container_width=True,
# )
# fn2 = "deepmip_boxplot.pdf"
# img2 = io.BytesIO()
# fig.savefig(img2, format="pdf")

# fn3 = "deepmip_boxplot.jpg"
# img3 = io.BytesIO()
# fig.savefig(img3, format="jpg")
# st.pyplot(fig)


# col4, col5, col6 = st.columns(3)

# with col4:
#     st.download_button(
#         label="Download JPG",
#         data=img3,
#         file_name=fn3,
#         mime="image/jpg",
#         use_container_width=True,
#     )

# with col5:
#     st.download_button(
#         label="Download PNG",
#         data=img,
#         file_name=fn,
#         mime="image/png",
#         use_container_width=True,
#     )

# with col6:
#     st.download_button(
#         label="Download PDF",
#         data=img2,
#         file_name=fn2,
#         mime="image/pdf",
#         use_container_width=True,
#     )

st.subheader(var_y + " vs. CO$_2$")
bokeh_composition2 = box_whisker_plot(
    df_model, var_y, "CO2", proxy_check, proxy_mean, proxy_std, proxy_label
)
st.bokeh_chart(hv.render(bokeh_composition2, backend="bokeh"))

st.subheader(var_y + " vs. GMST")
bokeh_composition3 = box_whisker_plot(
    df_model, var_y, "GMST", proxy_check, proxy_mean, proxy_std, proxy_label
)
st.bokeh_chart(hv.render(bokeh_composition3, backend="bokeh"))
