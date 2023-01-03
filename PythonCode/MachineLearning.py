#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:49:45 2022

@author: lollo
"""

# import pandas as pd
import numpy as np
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
import pickle
# from xgboost import XGBClassifier


filename = 'model_xgb.pkl'

rf_model = pickle.load(open(filename, 'rb'))


def predict(education, joining_year, city, payment_tier, age, gender,
            ever_benched, experience):
    leave_or_not = None
    input_values = np.array([education, joining_year, city, payment_tier, age,
                             gender, ever_benched, experience], ndmin=2)
    # input values non è un vettore, ma una matrice con una riga;
    # è una distinzione importante per predict
    output_value = rf_model.predict(input_values)
    if output_value[0] == 1:
        leave_or_not = True
    else:
        leave_or_not = False
    # print(leave_or_not) #debug
    return leave_or_not

# predict(1, 2014, 3, 2, 37, 1, 0, 5) #debug
