#!/usr/bin/env python

#################################################################################
# DeepMIP experiments
#################################################################################

exp_dict = dict()
exp_dict['piControl']    = { \
        'long_name' : 'piControl',
        'medium_name' : 'piControl',
        'short_name' : 'PI',
        'CO2' : '280',
        }

exp_dict['deepmip_sens_1xCO2']    = { \
        'long_name' : 'deepmip_sens_1xCO2',
        'medium_name' : 'DeepMIP_1x',
        'short_name' : '1xCO2',
        'CO2' : '280',
        }

exp_dict['deepmip_sens_1.5xCO2']    = { \
        'long_name' : 'deepmip_sens_1.5xCO2',
        'medium_name' : 'DeepMIP_1.5x',
        'short_name' : '1.5xCO2',
        'CO2' : '420',
        }

exp_dict['deepmip_sens_2xCO2']    = { \
        'long_name' : 'deepmip_sens_2xCO2',
        'medium_name' : 'DeepMIP_2x',
        'short_name' : '2xCO2',
        'CO2' : '560',
        }

exp_dict['deepmip_stand_3xCO2']    = { \
        'long_name' : 'deepmip_stand_3xCO2.5xCO2',
        'medium_name' : 'DeepMIP_3x',
        'short_name' : '3xCO2',
        'CO2' : '840',
        }

exp_dict['deepmip_sens_4xCO2']    = { \
        'long_name' : 'deepmip_sens_4xCO2',
        'medium_name' : 'DeepMIP_4x',
        'short_name' : '4xCO2',
        'CO2' : '1120',
        }

exp_dict['deepmip_stand_6xCO2']    = { \
        'long_name' : 'deepmip_sens_6xCO2',
        'medium_name' : 'DeepMIP_6x',
        'short_name' : '6xCO2',
        'CO2' : '1680',
        }

exp_dict['deepmip_sens_9xCO2']    = { \
        'long_name' : 'deepmip_sens_9xCO2',
        'medium_name' : 'DeepMIP_9x',
        'short_name' : '9xCO2',
        'CO2' : '2520',
        }

#################################################################################
# DeepMIP models
#################################################################################

model_dict    = dict()
model_dict['CESM1.2_CAM5']    = { \
        'versn' : 'v1.0',
        'group' : 'CESM',
        'abbrv' : 'CESM',
        'pcolor': 'red',
        'exps'  : ['piControl', 'deepmip_sens_1xCO2', 'deepmip_stand_3xCO2', 'deepmip_stand_6xCO2', 'deepmip_sens_9xCO2'],
        'gmst'  : [13.2, 18.4, 25.0, 29.8, 35.5]
        }

model_dict['COSMOS-landveg_r2413']  = { \
        'versn' : 'v1.0',
        'group' : 'COSMOS',
        'abbrv' : 'COSMOS',
        'pcolor': 'magenta',
        'exps'  : ['piControl', 'deepmip_sens_1xCO2', 'deepmip_stand_3xCO2', 'deepmip_sens_4xCO2'],
        'gmst'  : [13.9, 17.0, 25.2, 26.9]
        }

model_dict['GFDL_CM2.1']      = { \
        'versn' : 'v1.0',
        'group' : 'GFDL',
        'abbrv' : 'GFDL',
        'pcolor': 'orange',
        'exps'  : ['piControl', 'deepmip_sens_1xCO2', 'deepmip_sens_2xCO2', 'deepmip_stand_3xCO2', 'deepmip_sens_4xCO2', 'deepmip_stand_6xCO2'],
        'gmst'  : [15.6, 19.2, 22.9, 25.4, 27.5, 30.2]
        }

model_dict['HadCM3B_M2.1aN']  = { \
        'versn' : 'v1.0',
        'group' : 'HadCM3',
        'abbrv' : 'HadCM3',
        'pcolor': 'maroon',
        'exps'  : ['piControl', 'deepmip_sens_1xCO2', 'deepmip_sens_2xCO2', 'deepmip_stand_3xCO2'],
        'gmst'  : [13.9, 17.4, 21.2, 25.0]
        }

model_dict['HadCM3BL_M2.1aN'] = { \
        'versn' : 'v1.0',
        'group' : 'HadCM3',
        'abbrv' : 'HadCM3L',
        'pcolor': 'darkgoldenrod',
        'exps'  : ['piControl', 'deepmip_sens_1xCO2', 'deepmip_sens_2xCO2', 'deepmip_stand_3xCO2'],
        'gmst'  : [13.2, 16.9, 21.1, 26.0]
        }

model_dict['INM-CM4-8']    = { \
        'versn' : 'v1.0',
        'group' : 'INMCM',
        'abbrv' : 'INM',
        'pcolor': 'lime',
        'exps'  : ['piControl','deepmip_stand_6xCO2'],
        'gmst'  : [13.2, 23.4]
        }

model_dict['IPSLCM5A2']    = { \
        'versn' : 'v1.0',
        'group' : 'IPSL',
        'abbrv' : 'IPSL',
        'pcolor': 'blue',
        'exps'  : ['piControl', 'deepmip_sens_1.5xCO2', 'deepmip_stand_3xCO2'],
        'gmst'  : [13.2, 19.4, 25.0]
        }

model_dict['MIROC4m']   = { \
        'versn' : 'v1.0',
        'group' : 'MIROC',
        'abbrv' : 'MIROC',
        'pcolor': 'darkgreen',
        'exps'  : ['piControl', 'deepmip_sens_1xCO2', 'deepmip_sens_2xCO2', 'deepmip_stand_3xCO2'],
        'gmst'  : [12.9, 16.6, 20.4, 23.5]
        }

#################################################################################
# DeepMIP variables
#################################################################################

variable_dict    = dict()
variable_dict['tas']    = { \
        'longname' : 'near-surface air temperature',
        'label' : 'temperature',
        'unit' : 'K',
        }

variable_dict['pr']    = { \
        'longname' : 'precipitation',
        'label' : 'total precipitation',
        'unit' : 'kgm-2s-1',
        }
        
variable_dict['tos']    = { \
        'longname' : 'sea surface temperature',
        'label' : 'temperature',
        'unit' : '°C',
        }
