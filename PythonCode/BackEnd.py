"""
 Elenco delle features

Education : The highest level of formal education obtained by the employee ;
   trasformo [Bachelor, Master, PHD] in [1, 2, 3]
 JoiningYear : Year of joining the company ; [2012, ..., 2018]
 City : Job Location ; trasformo [Bangalore, New Delhi, Pune] in [1, 2, 3]
 PaymentTier : [1:3] -> 1 means better payment ; trasformo [1,2,3] in [3,2,1]
 Age : Age of the employee ; [22, ..., 41]
 Gender : Gender of the employee ; trasformo [Male, Female] in [0, 1]
 EverBenched : Ever kept out of project for more than one month ;
   trasformo [No, Yes] in [0, 1]
 ExperienceInCurrentDomain : Experience in current field ; [0, ..., 7]
"""

# import pandas as pd
# import numpy as np
import MachineLearning as ml


def transform_city(city):
    if city == "Bangalore":
        return 1
    elif city == "New Delhi":
        return 2
    elif city == "Pune":
        return 3
    else:
        return 1


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
    if ever_benched == "No":
        return 0
    elif ever_benched == "Yes":
        return 1
    else:
        return 0


def transform_gender(gender):
    if gender == "Male":
        return 0
    elif gender == "Female":
        return 1
    else:
        return 0


def transform_payment_tier(payment_tier):
    if payment_tier == 3:
        return 1
    elif payment_tier == 2:
        return 2
    elif payment_tier == 1:
        return 3
    else:
        return 1


def predict(education, joining_year, city, payment_tier, age, gender,
            ever_benched, experience):
    leave_or_not = ml.predict(education, joining_year, city, payment_tier,
                              age, gender, ever_benched, experience)
    return leave_or_not


# roba per connettività col server?
