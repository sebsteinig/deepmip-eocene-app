#!/usr/bin/env python

#################################################################################
# DeepMIP experiments
#################################################################################

exp_dict = dict()

exp_dict["deepmip-eocene-p1-PI"] = {
    "long_name": "deepmip-eocene-p1-PI",
    "medium_name": "PI",
    "short_name": "PI",
    "CO2": "280",
    "color": "#BAB0AC",
}

exp_dict["deepmip-eocene-p1-x1"] = {
    "long_name": "deepmip-eocene-p1-x1",
    "medium_name": "DeepMIP_1x",
    "short_name": "1xCO2",
    "CO2": "280",
    "color": "black",
}

exp_dict["deepmip-eocene-p1-x1.5"] = {
    "long_name": "deepmip-eocene-p1-x1.5",
    "medium_name": "DeepMIP_1.5x",
    "short_name": "1.5xCO2",
    "CO2": "420",
    "color": "gray",
}

exp_dict["deepmip-eocene-p1-x2"] = {
    "long_name": "deepmip-eocene-p1-x2",
    "medium_name": "DeepMIP_2x",
    "short_name": "2xCO2",
    "CO2": "560",
    "color": "#4E79A7",
}

exp_dict["deepmip-eocene-p1-x3"] = {
    "long_name": "deepmip-eocene-p1-x3",
    "medium_name": "DeepMIP_3x",
    "short_name": "3xCO2",
    "CO2": "840",
    "color": "#59A14F",
}

exp_dict["deepmip-eocene-p1-x4"] = {
    "long_name": "deepmip-eocene-p1-x4",
    "medium_name": "DeepMIP_4x",
    "short_name": "4xCO2",
    "CO2": "1120",
    "color": "#F28E2B",
}

exp_dict["deepmip-eocene-p1-x6"] = {
    "long_name": "deepmip-eocene-p1-x6",
    "medium_name": "DeepMIP_6x",
    "short_name": "6xCO2",
    "CO2": "1680",
    "color": "#E15759",
}

exp_dict["deepmip-eocene-p1-x9"] = {
    "long_name": "deepmip-eocene-p1-x9",
    "medium_name": "DeepMIP_9x",
    "short_name": "9xCO2",
    "CO2": "2520",
    "color": "#B07AA1",
}

#################################################################################
# DeepMIP models
#################################################################################

model_dict = dict()

model_dict["CESM1.2-CAM5"] = {
    "versn": "v1.0",
    "family": "CESM",
    "abbrv": "CESM",
    "color": "#1f77b4",  # tab:blue
    "exps": [
        "deepmip-eocene-p1-PI",
        "deepmip-eocene-p1-x1",
        "deepmip-eocene-p1-x3",
        "deepmip-eocene-p1-x6",
        "deepmip-eocene-p1-x9",
    ],
    "gmst": [13.2, 18.4, 25.0, 29.8, 35.5],
    "rotation": "H14",
    "CMIP generation": "CMIP5",
}

model_dict["COSMOS-landveg-r2413"] = {
    "versn": "v1.0",
    "family": "COSMOS",
    "abbrv": "COSMOS",
    "color": "#2ca02c",  # tab:green
    "exps": [
        "deepmip-eocene-p1-PI",
        "deepmip-eocene-p1-x1",
        "deepmip-eocene-p1-x3",
        "deepmip-eocene-p1-x4",
    ],
    "gmst": [13.9, 17.0, 25.2, 26.9],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["GFDL-CM2.1"] = {
    "versn": "v1.0",
    "family": "GFDL",
    "abbrv": "GFDL",
    "color": "#ff7f0e",  # tab:orange
    "exps": [
        "deepmip-eocene-p1-PI",
        "deepmip-eocene-p1-x1",
        "deepmip-eocene-p1-x2",
        "deepmip-eocene-p1-x3",
        "deepmip-eocene-p1-x4",
        "deepmip-eocene-p1-x6",
    ],
    "gmst": [15.6, 19.2, 22.9, 25.4, 27.5, 30.2],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["HadCM3B-M2.1aN"] = {
    "versn": "v1.0",
    "family": "HadCM3",
    "abbrv": "HadCM3",
    "color": "#d62728",  # tab:red
    "exps": [
        "deepmip-eocene-p1-PI",
        "deepmip-eocene-p1-x1",
        "deepmip-eocene-p1-x2",
        "deepmip-eocene-p1-x3",
    ],
    "gmst": [13.9, 17.4, 21.2, 25.0],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["HadCM3BL-M2.1aN"] = {
    "versn": "v1.0",
    "family": "HadCM3",
    "abbrv": "HadCM3L",
    "color": "#e377c2",  # tab:pink
    "exps": [
        "deepmip-eocene-p1-PI",
        "deepmip-eocene-p1-x1",
        "deepmip-eocene-p1-x2",
        "deepmip-eocene-p1-x3",
    ],
    "gmst": [13.2, 16.9, 21.1, 26.0],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["INM-CM4-8"] = {
    "versn": "v1.0",
    "family": "INMCM",
    "abbrv": "INM",
    "color": "#9467bd",  # tab:purple
    "exps": ["deepmip-eocene-p1-PI", "deepmip-eocene-p1-x6"],
    "gmst": [13.2, 23.4],
    "rotation": "H14",
    "CMIP generation": "CMIP6",
}

model_dict["IPSLCM5A2"] = {
    "versn": "v1.0",
    "family": "IPSL",
    "abbrv": "IPSL",
    "color": "#8c564b",  # tab:brown
    "exps": ["deepmip-eocene-p1-PI", "deepmip-eocene-p1-x1.5", "deepmip-eocene-p1-x3"],
    "gmst": [13.2, 19.4, 25.0],
    "rotation": "H14",
    "CMIP generation": "CMIP5",
}

model_dict["MIROC4m"] = {
    "versn": "v1.0",
    "family": "MIROC",
    "abbrv": "MIROC",
    "color": "#bcbd22",  # tab:olive
    "exps": [
        "deepmip-eocene-p1-PI",
        "deepmip-eocene-p1-x1",
        "deepmip-eocene-p1-x2",
        "deepmip-eocene-p1-x3",
    ],
    "gmst": [12.9, 16.6, 20.4, 23.5],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["NorESM1-F"] = {
    "versn": "v1.0",
    "family": "NorESM",
    "abbrv": "NorESM",
    "color": "#17becf",  # tab:cyan
    "exps": ["deepmip-eocene-p1-PI", "deepmip-eocene-p1-x2", "deepmip-eocene-p1-x4"],
    "gmst": [14.5, 21.2, 24.1],
    "rotation": "B16",
    "CMIP generation": "CMIP5-6",
}

#################################################################################
# DeepMIP variables
#################################################################################


#### Atmosphere variables

variable_dict = dict()
variable_dict["tas"] = {
    "long_name": "Near-surface air temperature",
    "label": "temperature",
    "unit": "K",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["pr"] = {
    "long_name": "Precipitation",
    "label": "precipitation",
    "unit": "kgm^{-2}s^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["ts"] = {
    "long_name": "Surface skin temperature",
    "unit": "K",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["evspsbl"] = {
    "long_name": "Total evaporation",
    "unit": "kgm^{-2}s^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["clt"] = {
    "long_name": "Total cloud cover fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlds"] = {
    "long_name": "Surface downwelling longwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlus"] = {
    "long_name": "Surface upwelling longwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsds"] = {
    "long_name": "Surface downwelling shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsus"] = {
    "long_name": "Surface upwelling shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsdt"] = {
    "long_name": "TOA incident shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsut"] = {
    "long_name": "TOA outgoing shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlut"] = {
    "long_name": "TOA outgoing longwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rldscs"] = {
    "long_name": "Surface downwelling longwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsdscs"] = {
    "long_name": "Surface downwelling shortwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsuscs"] = {
    "long_name": "Surface upwelling shortwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsutcs"] = {
    "long_name": "TOA outgoing shortwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlutcs"] = {
    "long_name": "TOA outgoing longwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["hfss"] = {
    "long_name": "Sensible heat flux (upward)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["hfls"] = {
    "long_name": "Latent heat flux (upward)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["uas"] = {
    "long_name": "Near-surface eastward wind",
    "unit": "ms^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["vas"] = {
    "long_name": "Near-surface northward wind",
    "unit": "ms^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["uas"] = {
    "long_name": "Near-surface eastward wind",
    "unit": "ms^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["tauu"] = {
    "long_name": "Surface eastward wind stress",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["tauv"] = {
    "long_name": "Surface northward wind stress",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["psl"] = {
    "long_name": "Mean sea level pressure",
    "unit": "Pa",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["ps"] = {
    "long_name": "Surface pressure",
    "unit": "Pa",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["ua"] = {
    "long_name": "Eastward wind on model levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["va"] = {
    "long_name": "Northward wind on model levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["wa"] = {
    "long_name": "Vertical wind on model levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["uap"] = {
    "long_name": "Eastward wind on pressure levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["vap"] = {
    "long_name": "Northward wind on pressure levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["wap"] = {
    "long_name": "Vertical wind on pressure levels",
    "unit": "Pas^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["zg"] = {
    "long_name": "Geopotential height on pressure levels",
    "unit": "m",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["ta"] = {
    "long_name": "Temperature on pressure levels",
    "unit": "K",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["hus"] = {
    "long_name": "Specific humidity on pressure levels",
    "unit": "kgkg^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["cl"] = {
    "long_name": "Cloud fraction on pressure levels",
    "unit": "[0,1]",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["cll"] = {
    "long_name": "Low-level cloud fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["clm"] = {
    "long_name": "Medium-level cloud fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["clh"] = {
    "long_name": "High-level cloud fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

#### Ocean variables

variable_dict["tos"] = {
    "long_name": "Sea surface temperature",
    "label": "temperature",
    "unit": "°C",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["siconc"] = {
    "long_name": "Sea-ice fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["uo"] = {
    "long_name": "Eastward velocity on model levels",
    "unit": "cms^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["vo"] = {
    "long_name": "Northward velocity on model levels",
    "unit": "cms^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["wo"] = {
    "long_name": "Vertical velocity on model levels",
    "unit": "cms^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["thetao"] = {
    "long_name": "Potential temperature on model levels",
    "unit": "°C",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["so"] = {
    "long_name": "Salinity on model levels",
    "unit": "psu",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["mlotst"] = {
    "long_name": "Mixed-layer depth",
    "unit": "m",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["zos"] = {
    "long_name": "Sea surface height",
    "unit": "m",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["tauuo"] = {
    "long_name": "Surface eastward wind stress (on ocean grid)",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["tauvo"] = {
    "long_name": "Surface northward wind stress (on ocean grid)",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["hfno"] = {
    "long_name": "Net surface heat flux (on ocean grid)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["wfno"] = {
    "long_name": "Net surface freshwater flux (on ocean grid)",
    "unit": "kgm^{-2}s^{-1}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["difvto"] = {
    "long_name": "Vertical ocean tracer diffusivity",
    "unit": "m^{-2}s^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["difvmo"] = {
    "long_name": "Vertical ocean momentum diffusivity",
    "unit": "m^{-2}s^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["sftbarot"] = {
    "long_name": "Barotropic streamfunction",
    "unit": "Sv",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["sftmyz"] = {
    "long_name": "Global overturning streamfunction",
    "unit": "Sv",
    "dimensions": 3,
    "realm": "ocean",
}

#### Boundary conditions

variable_dict["sftlf"] = {
    "long_name": "Land-sea mask (on atmospheric grid)",
    "unit": "[0,1]",
    "dimensions": 2,
    "realm": "atmos",
}

variable_dict["orog"] = {
    "long_name": "Topography (on atmospheric grid)",
    "unit": "[0,1]",
    "dimensions": 2,
    "realm": "atmos",
}

variable_dict["deptho"] = {
    "long_name": "Bathymetry (on ocean grid)",
    "unit": "[0,1]",
    "dimensions": 2,
    "realm": "ocean",
}

variable_dict["lai"] = {
    "long_name": "Leaf area index",
    "unit": "1",
    "dimensions": 2,
    "realm": "atmos",
}
