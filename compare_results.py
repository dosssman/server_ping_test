import sys
import pickle
import numpy as np
import pandas as pd

def load_res_from_pkl(filename):
    with open( filename, 'rb') as f:
        return pickle.load( f)

### Parametererization
doss_results = "benchresults.2022-05-13_11_15_21.pkl"
draz_results = "benchresults.2022-05-13_11_15_04.pkl"

savefiles = [doss_results, draz_results]
ress = {}

for savefilename in savefiles:
    ress[savefilename] = load_res_from_pkl(savefilename)

processed0 = dict()

assert len( ress[doss_results]) == len( ress[draz_results])

for hostname in ress[doss_results].keys():
    processed0[hostname] = { 
        "Doss": ress[doss_results][hostname],
        "Draz": ress[draz_results][hostname], 
        "Sum": (ress[doss_results][hostname] + ress[draz_results][hostname])}

pd0 = pd.DataFrame.from_dict(processed0, orient='index', columns=[ 'Doss', 'Draz', 'Sum'])
pd0.to_excel( "Doss_Draz_Compare.xlsx")