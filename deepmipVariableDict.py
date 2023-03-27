#!/usr/bin/env python
import numpy as np

deepmipVariableDict    = dict()
deepmipVariableDict['tas']    = { \
        'longname' : 'near-surface air temperature',
        'label' : 'temperature [$^\circ$C]',
        'unit' : 'degC',
        }

deepmipVariableDict['pr']    = { \
        'longname' : 'precipitation',
        'label' : 'total precipitation [mm/day]',
        'unit' : 'mm/day',
        }
        
deepmipVariableDict['tos']    = { \
        'longname' : 'sea surface temperature',
        'label' : 'temperature [$^\circ$C]',
        'unit' : 'degC',
        }
