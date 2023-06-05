# DeepMIP-Eocene web app

This repository houses a web application for interactive access to the DeepMIP-Eocene model database. 

> **Live version:** [https://data.deepmip.org](https://data.deepmip.org)

> **Note:** The application is currently under development. Please double-check any results before using them in your research.

This tool uses Python to extract data from the open-access DeepMIP-Eocene database. You can access the database [here](https://www.deepmip.org/data-eocene/). The app enables users without programming experience to extract common variables such as temperature, precipitation, etc., from all DeepMIP models at any specified location. Batch processing of sites is possible and example sets of locations from the DeepMIP-Eocene proxie database [(Hollis et al., 2019)](https://gmd.copernicus.org/articles/12/3149/2019/). The extracted data can be visualized and downloaded in CSV/Excel format for offline model-data comparison. The individual Python processing and analysis functions are saved in `deepmip_modules.py` and may also serve as a launchpad for more advanced analyses.

## About Streamlit

The web app was built with [Streamlit](https://streamlit.io), which is an open-source Python library that makes it easy to create custom web apps for machine learning and data science. In just a few minutes, you can build and deploy interactive apps without the need for frontend web development skills.

## About Docker

The code is bundled via [Docker](https://www.docker.com), which is an open platform for developers and sysadmins to build, ship, and run distributed applications. With Docker, you can separate your applications from your infrastructure and treat your infrastructure like a managed application.

## Docker Setup and Usage

A Docker container for this application is available at `sebsteinig/deepmip-eocene-app`. This is the same version that is running at [https://data.deepmip.org](https://data.deepmip.org). 

You can also run it locally on your computer. To download and run the Docker container, follow these steps:

1. Install Docker on your machine. You can download Docker from the [official website](https://www.docker.com/products/docker-desktop).

2. Open a terminal and pull the Docker image with the following command:
```bash
docker pull sebsteinig/deepmip-eocene-app
```

3. Once the image is downloaded, you can run the Docker container with this command:
```bash
docker run -p 8501:8501 sebsteinig/deepmip-eocene-app
```

This command maps the 8501 port in the Docker container to port 8501 on your machine. Streamlit, by default, runs on port 8501.

4. Open your web browser and visit `http://localhost:8501` to view the application.

> **Note:** Keep in mind that any changes you make inside the Docker container will be lost when the container is stopped. To save your changes, consider creating a Docker volume or changing the Docker image.

## Contribution

We appreciate contributions to the development of this application. Feel free to open a pull request with your changes or enhancements.

## Support

If you encounter any issues while setting up or using the application, feel free to open an issue on GitHub. We are happy to assist!

## License

This project is licensed under the terms of the MIT license. For more details, please see the LICENSE file.
