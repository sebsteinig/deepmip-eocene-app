# app/Dockerfile

FROM python:3.9-slim

WORKDIR /deepmip_database_app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    python3-dev \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip setuptools wheel

RUN pip3 install "shapely<2" --no-binary shapely

RUN git clone https://github.com/sebsteinig/deepmip_database_app.git .

#RUN pip3 install -r requirements.txt
ADD requirements.txt .
RUN python3 -m pip install --no-cache-dir --compile -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "0_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
