#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:21:20 2022

@author: lollo
"""

import pandas as pd
import numpy as np
import MachineLearning as ml

def transform_city(city):
    pass

def transform_education(education):
    if education == "Bachelor":
        return 1
    elif education == "Master":
        return 2
    elif education == "PHD":
        return 3
    else:
        return 1

def transform_ever_benched(ever_benched):
    pass

def transform_gender(gender):
    pass

def transform_payment_tier(payment_tier):
    pass

def predict(education, joining_year, city, payment_tier, age, gender, ever_benched, experience):
    leave_or_not = ml.predict(education, joining_year, city, payment_tier, age, gender, ever_benched, experience)
    return leave_or_not

#roba per connettività col server?