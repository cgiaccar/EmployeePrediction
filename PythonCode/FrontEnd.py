#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:23:18 2022

@author: lollo
"""

# Elenco delle features

# Education : The highest level of formal education obtained by the employee ;
#   trasformo [Bachelor, Master, PHD] in [1, 2, 3]
# JoiningYear : Year of joining the company ; [2012, ..., 2018]
# City : Job Location ; trasformo [Bangalore, New Delhi, Pune] in [1, 2, 3]
# PaymentTier : [1:3] -> 1 means better payment ; trasformo [1,2,3] in [3,2,1]
# Age : Age of the employee ; [22, ..., 41]
# Gender : Gender of the employee ; trasformo [Male, Female] in [0, 1]
# EverBenched : Ever kept out of project for more than one month ; trasformo [No, Yes] in [0, 1]
# ExperienceInCurrentDomain : Experience in current field ; [0, ..., 7]

import streamlit as st
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#tkinter serve per listbox

import BackEnd as b

education = 1
joining_year = 2012
city = 1
payment_tier = 1
age = 18
gender = 0
ever_benched = 0
experience = 0

st.title("EmployeePrediction!!!")

if 'progress' not in st.session_state:
    #progress indica a quale domanda stai rispondendo.
    #0 significa che il test non è ancora iniziato.
    #9 significa che è stato completato.
    #ordine delle domande —
    #1. Age
    #2. Gender
    #3. City
    #4. Education
    #5. JoiningYear
    #6. ExperienceInCurrentDomain
    #7. PaymentTier
    #8. EverBenched
    st.session_state['progress'] = 0

if st.session_state['progress'] == 0:
    begin = st.button("Begin!")
    if begin:
        if st.session_state['progress'] < 1:
            st.session_state['progress'] = 1

if st.session_state['progress'] == 1:
    #age question
    #age = result
    pass

if st.session_state['progress'] == 2:
    #gender question
    #gender = b.transform_gender(result)
    pass

if st.session_state['progress'] == 3:
    #city question
    #city = b.transform_city(result)
    pass

if st.session_state['progress'] == 4:
    #education question
    #education = b.transform_education(result)
    pass

if st.session_state['progress'] == 5:
    #joiningyear question
    #joining_year = result
    pass

if st.session_state['progress'] == 6:
    #experience question
    #experience = result
    pass

if st.session_state['progress'] == 7:
    #payment question
    #payment_tier = b.transform_payment_tier(result)
    pass

if st.session_state['progress'] == 8:
    #everbenched question
    #ever_benched = b.transform_ever_benched(result)
    pass

if st.session_state['progress'] == 9:
    #leave_or_not = b.predict(education, joining_year, city, payment_tier, age, gender, ever_benched, experience)
    #if leave_or_not:
        #...
    #else:
        #...
    #modo per tornare a session_state['progress'] = 0
    pass










