#!/usr/bin/env python

#################################################################################
# DeepMIP experiments
#################################################################################

exp_dict = dict()

exp_dict["piControl"] = {
    "long_name": "piControl",
    "medium_name": "piControl",
    "short_name": "PI",
    "CO2": "280",
    "color": "#BAB0AC",
}

exp_dict["deepmip_sens_1xCO2"] = {
    "long_name": "deepmip_sens_1xCO2",
    "medium_name": "DeepMIP_1x",
    "short_name": "1xCO2",
    "CO2": "280",
    "color": "black",
}

exp_dict["deepmip_sens_1.5xCO2"] = {
    "long_name": "deepmip_sens_1.5xCO2",
    "medium_name": "DeepMIP_1.5x",
    "short_name": "1.5xCO2",
    "CO2": "420",
    "color": "gray",
}

exp_dict["deepmip_sens_2xCO2"] = {
    "long_name": "deepmip_sens_2xCO2",
    "medium_name": "DeepMIP_2x",
    "short_name": "2xCO2",
    "CO2": "560",
    "color": "#4E79A7",
}

exp_dict["deepmip_stand_3xCO2"] = {
    "long_name": "deepmip_stand_3xCO2.5xCO2",
    "medium_name": "DeepMIP_3x",
    "short_name": "3xCO2",
    "CO2": "840",
    "color": "#59A14F",
}

exp_dict["deepmip_sens_4xCO2"] = {
    "long_name": "deepmip_sens_4xCO2",
    "medium_name": "DeepMIP_4x",
    "short_name": "4xCO2",
    "CO2": "1120",
    "color": "#F28E2B",
}

exp_dict["deepmip_stand_6xCO2"] = {
    "long_name": "deepmip_sens_6xCO2",
    "medium_name": "DeepMIP_6x",
    "short_name": "6xCO2",
    "CO2": "1680",
    "color": "#E15759",
}

exp_dict["deepmip_sens_9xCO2"] = {
    "long_name": "deepmip_sens_9xCO2",
    "medium_name": "DeepMIP_9x",
    "short_name": "9xCO2",
    "CO2": "2520",
    "color": "#B07AA1",
}

#################################################################################
# DeepMIP models
#################################################################################

model_dict = dict()

model_dict["CESM1.2_CAM5"] = {
    "versn": "v1.0",
    "group": "CESM",
    "abbrv": "CESM",
    "color": "#1f77b4",  # tab:blue
    "exps": [
        "piControl",
        "deepmip_sens_1xCO2",
        "deepmip_stand_3xCO2",
        "deepmip_stand_6xCO2",
        "deepmip_sens_9xCO2",
    ],
    "gmst": [13.2, 18.4, 25.0, 29.8, 35.5],
    "rotation": "H14",
    "CMIP generation": "CMIP5",
}

model_dict["COSMOS-landveg_r2413"] = {
    "versn": "v1.0",
    "group": "COSMOS",
    "abbrv": "COSMOS",
    "color": "#2ca02c",  # tab:green
    "exps": [
        "piControl",
        "deepmip_sens_1xCO2",
        "deepmip_stand_3xCO2",
        "deepmip_sens_4xCO2",
    ],
    "gmst": [13.9, 17.0, 25.2, 26.9],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["GFDL_CM2.1"] = {
    "versn": "v1.0",
    "group": "GFDL",
    "abbrv": "GFDL",
    "color": "#ff7f0e",  # tab:orange
    "exps": [
        "piControl",
        "deepmip_sens_1xCO2",
        "deepmip_sens_2xCO2",
        "deepmip_stand_3xCO2",
        "deepmip_sens_4xCO2",
        "deepmip_stand_6xCO2",
    ],
    "gmst": [15.6, 19.2, 22.9, 25.4, 27.5, 30.2],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["HadCM3B_M2.1aN"] = {
    "versn": "v1.0",
    "group": "HadCM3",
    "abbrv": "HadCM3",
    "color": "#d62728",  # tab:red
    "exps": [
        "piControl",
        "deepmip_sens_1xCO2",
        "deepmip_sens_2xCO2",
        "deepmip_stand_3xCO2",
    ],
    "gmst": [13.9, 17.4, 21.2, 25.0],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["HadCM3BL_M2.1aN"] = {
    "versn": "v1.0",
    "group": "HadCM3",
    "abbrv": "HadCM3L",
    "color": "#e377c2",  # tab:pink
    "exps": [
        "piControl",
        "deepmip_sens_1xCO2",
        "deepmip_sens_2xCO2",
        "deepmip_stand_3xCO2",
    ],
    "gmst": [13.2, 16.9, 21.1, 26.0],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["INM-CM4-8"] = {
    "versn": "v1.0",
    "group": "INMCM",
    "abbrv": "INM",
    "color": "#9467bd",  # tab:purple
    "exps": ["piControl", "deepmip_stand_6xCO2"],
    "gmst": [13.2, 23.4],
    "rotation": "H14",
    "CMIP generation": "CMIP6",
}

model_dict["IPSLCM5A2"] = {
    "versn": "v1.0",
    "group": "IPSL",
    "abbrv": "IPSL",
    "color": "#8c564b",  # tab:brown
    "exps": ["piControl", "deepmip_sens_1.5xCO2", "deepmip_stand_3xCO2"],
    "gmst": [13.2, 19.4, 25.0],
    "rotation": "H14",
    "CMIP generation": "CMIP5",
}

model_dict["MIROC4m"] = {
    "versn": "v1.0",
    "group": "MIROC",
    "abbrv": "MIROC",
    "color": "#bcbd22",  # tab:olive
    "exps": [
        "piControl",
        "deepmip_sens_1xCO2",
        "deepmip_sens_2xCO2",
        "deepmip_stand_3xCO2",
    ],
    "gmst": [12.9, 16.6, 20.4, 23.5],
    "rotation": "H14",
    "CMIP generation": "CMIP3",
}

model_dict["NorESM1_F"] = {
    "versn": "v1.0",
    "group": "NorESM",
    "abbrv": "NorESM",
    "color": "#17becf",  # tab:cyan
    "exps": ["piControl", "deepmip_sens_2xCO2", "deepmip_sens_4xCO2"],
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
    "longname": "Near-surface air temperature",
    "label": "temperature",
    "unit": "K",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["pr"] = {
    "longname": "Precipitation",
    "label": "precipitation",
    "unit": "kgm^{-2}s^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["ts"] = {
    "longname": "Surface skin temperature",
    "unit": "K",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["evspsbl"] = {
    "longname": "Total evaporation",
    "unit": "kgm^{-2}s^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["clt"] = {
    "longname": "Total cloud cover fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlds"] = {
    "longname": "Surface downwelling longwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlus"] = {
    "longname": "Surface upwelling longwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsds"] = {
    "longname": "Surface downwelling shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsus"] = {
    "longname": "Surface upwelling shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsdt"] = {
    "longname": "TOA incident shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsut"] = {
    "longname": "TOA outgoing shortwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlut"] = {
    "longname": "TOA outgoing longwave radiation",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rldscs"] = {
    "longname": "Surface downwelling longwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsdscs"] = {
    "longname": "Surface downwelling shortwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsuscs"] = {
    "longname": "Surface upwelling shortwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rsutcs"] = {
    "longname": "TOA outgoing shortwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["rlutcs"] = {
    "longname": "TOA outgoing longwave radiation (clear sky)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["hfss"] = {
    "longname": "Sensible heat flux (upward)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["hfls"] = {
    "longname": "Latent heat flux (upward)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["uas"] = {
    "longname": "Near-surface eastward wind",
    "unit": "ms^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["vas"] = {
    "longname": "Near-surface northward wind",
    "unit": "ms^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["uas"] = {
    "longname": "Near-surface eastward wind",
    "unit": "ms^{-1}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["tauu"] = {
    "longname": "Surface eastward wind stress",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["tauv"] = {
    "longname": "Surface northward wind stress",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["psl"] = {
    "longname": "Mean sea level pressure",
    "unit": "Pa",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["ps"] = {
    "longname": "Surface pressure",
    "unit": "Pa",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["ua"] = {
    "longname": "Eastward wind on model levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["va"] = {
    "longname": "Northward wind on model levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["wa"] = {
    "longname": "Vertical wind on model levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["uap"] = {
    "longname": "Eastward wind on pressure levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["vap"] = {
    "longname": "Northward wind on pressure levels",
    "unit": "ms^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["wap"] = {
    "longname": "Vertical wind on pressure levels",
    "unit": "Pas^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["zg"] = {
    "longname": "Geopotential height on pressure levels",
    "unit": "m",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["ta"] = {
    "longname": "Temperature on pressure levels",
    "unit": "K",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["hus"] = {
    "longname": "Specific humidity on pressure levels",
    "unit": "kgkg^{-1}",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["cl"] = {
    "longname": "Cloud fraction on pressure levels",
    "unit": "[0,1]",
    "dimensions": 4,
    "realm": "atmos",
}

variable_dict["cll"] = {
    "longname": "Low-level cloud fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["clm"] = {
    "longname": "Medium-level cloud fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

variable_dict["clh"] = {
    "longname": "High-level cloud fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "atmos",
}

#### Ocean variables

variable_dict["tos"] = {
    "longname": "Sea surface temperature",
    "label": "temperature",
    "unit": "°C",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["siconc"] = {
    "longname": "Sea-ice fraction",
    "unit": "[0,1]",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["uo"] = {
    "longname": "Eastward velocity on model levels",
    "unit": "cms^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["vo"] = {
    "longname": "Northward velocity on model levels",
    "unit": "cms^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["wo"] = {
    "longname": "Vertical velocity on model levels",
    "unit": "cms^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["thetao"] = {
    "longname": "Potential temperature on model levels",
    "unit": "°C",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["so"] = {
    "longname": "Salinity on model levels",
    "unit": "psu",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["mlotst"] = {
    "longname": "Mixed-layer depth",
    "unit": "m",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["zos"] = {
    "longname": "Sea surface height",
    "unit": "m",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["tauuo"] = {
    "longname": "Surface eastward wind stress (on ocean grid)",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["tauvo"] = {
    "longname": "Surface northward wind stress (on ocean grid)",
    "unit": "Nm^{-2}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["hfno"] = {
    "longname": "Net surface heat flux (on ocean grid)",
    "unit": "Wm^{-2}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["wfno"] = {
    "longname": "Net surface freshwater flux (on ocean grid)",
    "unit": "kgm^{-2}s^{-1}",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["difvto"] = {
    "longname": "Vertical ocean tracer diffusivity",
    "unit": "m^{-2}s^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["difvmo"] = {
    "longname": "Vertical ocean momentum diffusivity",
    "unit": "m^{-2}s^{-1}",
    "dimensions": 4,
    "realm": "ocean",
}

variable_dict["sftbarot"] = {
    "longname": "Barotropic streamfunction",
    "unit": "Sv",
    "dimensions": 3,
    "realm": "ocean",
}

variable_dict["sftmyz"] = {
    "longname": "Global overturning streamfunction",
    "unit": "Sv",
    "dimensions": 3,
    "realm": "ocean",
}

#### Boundary conditions

variable_dict["sftlf"] = {
    "longname": "Land-sea mask (on atmospheric grid)",
    "unit": "[0,1]",
    "dimensions": 2,
    "realm": "atmos",
}

variable_dict["orog"] = {
    "longname": "Topography (on atmospheric grid)",
    "unit": "[0,1]",
    "dimensions": 2,
    "realm": "atmos",
}

variable_dict["deptho"] = {
    "longname": "Bathymetry (on ocean grid)",
    "unit": "[0,1]",
    "dimensions": 2,
    "realm": "ocean",
}

variable_dict["lai"] = {
    "longname": "Leaf area index",
    "unit": "1",
    "dimensions": 2,
    "realm": "atmos",
}
