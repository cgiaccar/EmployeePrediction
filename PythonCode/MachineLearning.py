"""
Loading and use of the machine learning model
"""

import numpy as np
import pickle
import os


path = os.path.dirname(os.path.dirname(__file__))
filename = path+'/Models/model_xgb.pkl'

rf_model = pickle.load(open(filename, 'rb'))


def predict(education, joining_year, city, payment_tier, age, gender,
            ever_benched, experience):
    will_leave = None
    input_values = np.array([education, joining_year, city, payment_tier, age,
                             gender, ever_benched, experience], ndmin=2)
    # input values non è un vettore, ma una matrice con una riga;
    # è una distinzione importante per predict
    output_value = rf_model.predict(input_values)
    if output_value[0] == 1:
        will_leave = True
    else:
        will_leave = False
    return will_leave
