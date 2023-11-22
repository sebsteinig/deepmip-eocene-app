import os
import streamlit as st

from app_modules import (
    init_sidebar,
)

st.set_page_config(
    page_title="View validation tables",
    layout="wide",
)

# Create a header row for types
st.title("Validation tables")

st.markdown(
    """
    This page presents an overview of all available model fields for each simulation and 
    validates the internal consistency of the database (i.e. the spread between model results).
    To do this, we automatically parse all `mean` and `time_series` files in the database for 
    any given experiment, interpolate them to a common grid, calculate the global mean, 
    minimum and maximum values and compare these values across all models. We use annual mean fields 
    for the validation of `mean` files and the last 12 available months of the `time_series` 
    files. For variables with multiple vertical levels, we select the vertical index 
    nearest to the 500 hPa pressure level or 1000 m depth for atmospheric and ocean data,
    respectively. See the [database paper]() for a definition and 
    dicussion of the z-score metric.
    """
)

st.markdown(
    """
    Results are grouped by atmospheric and ocean variables, as well as by `mean` and `time_series`
    files. Hovering over Individual tables reveals a "View fullscreen" button at the top right 
    of the respective image. All tables can be downloaded as a single ZIP file at the bottom of the page.
    """
)
init_sidebar()

# Define the directory where your images are located
image_directory = "img/validation_tables"
zip_file = "DeepMIP-Eocene-p1_validation-tables.zip"
zip_path = os.path.join(image_directory, zip_file)

# Experiment names and types for rows and columns
experiments = [
    "deepmip-eocene-p1-PI",
    "deepmip-eocene-p1-x1",
    "deepmip-eocene-p1-x1.5",
    "deepmip-eocene-p1-x2",
    "deepmip-eocene-p1-x3",
    "deepmip-eocene-p1-x4",
    "deepmip-eocene-p1-x6",
    "deepmip-eocene-p1-x9",
]

experiments_short = [
    "PI",
    "DeepMIP_1x",
    "DeepMIP_1.5x",
    "DeepMIP_2x",
    "DeepMIP_3x",
    "DeepMIP_4x",
    "DeepMIP_6x",
    "DeepMIP_9x",
]
types = ["atmos mean", "ocean mean", "atmos time_series", "ocean time_series"]

header_cols = st.columns([3, 4, 4, 4, 4])  # Adjust column widths as needed
header_cols[0].write("")  # Empty for the corner
for i, image_type in enumerate(types):
    header_cols[i + 1].markdown(f"**{image_type}**")

# Display images with row and column headers
for index, experiment in enumerate(experiments):
    cols = st.columns([3, 4, 4, 4, 4])  # Adjust column widths as needed
    cols[0].markdown(f"**{experiments_short[index]}**")
    for i, image_type in enumerate(types):
        # Construct the image filename
        filename = f"{experiment} {image_type}_validation_table-1.png"
        full_path = os.path.join(image_directory, filename)

        if os.path.exists(full_path):
            # Display full-size image
            cols[i + 1].image(full_path, use_column_width=True)

# Add a download button for the ZIP file
if os.path.exists(zip_path):
    with open(zip_path, "rb") as file:
        st.download_button(
            label="Download all Tables",
            data=file,
            file_name=zip_file,
            type="primary",
            mime="application/zip",
            use_container_width=True,
        )
else:
    st.write("ZIP file not found.")
