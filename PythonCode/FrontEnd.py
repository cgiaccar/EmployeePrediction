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
# EverBenched : Ever kept out of project for more than one month ;
#   trasformo [No, Yes] in [0, 1]
# ExperienceInCurrentDomain : Experience in current field ; [0, ..., 7]

import streamlit as st
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# tkinter serve per listbox

import BackEnd as b

# default values to avoid program crashing
# education = 1
# joining_year = 2012
# city = 1
# payment_tier = 1
# age = 18
# gender = 0
# ever_benched = 0
# experience = 0

st.title("EmployeePrediction!!!")

if 'progress' not in st.session_state:
    # progress indica a quale domanda stai rispondendo.
    # 0 significa che il test non è ancora iniziato.
    # 9 significa che è stato completato.
    # ordine delle domande —
    # 1. Age
    # 2. Gender
    # 3. City
    # 4. Education
    # 5. JoiningYear
    # 6. ExperienceInCurrentDomain
    # 7. PaymentTier
    # 8. EverBenched
    st.session_state['progress'] = 0
    st.session_state['education'] = 1
    st.session_state['joining_year'] = 2012
    st.session_state['city'] = 1
    st.session_state['payment_tier'] = 1
    st.session_state['age'] = 18
    st.session_state['gender'] = 0
    st.session_state['ever_benched'] = 0
    st.session_state['experience'] = 0

if st.session_state['progress'] == 0:
    begin = st.button("Begin!")
    if begin:
        if st.session_state['progress'] < 1:
            st.session_state['progress'] = 1

if st.session_state['progress'] == 1:
    possible_ages = []
    for i in range(0, 83):
        possible_ages.append(i+18)
    st.text('Qual''è la tua età?')
    select_age = st.selectbox('Seleziona Età', possible_ages)
    st.write('Hai selezionato ', select_age)
    result = select_age
    confirm = st.button('Next', 1) #1 è la key del bottone, che altrimenti
    #verrebbe generata in base al contenuto.
    if confirm and result >= 18:
        st.session_state['age'] = result
        st.session_state['progress'] += 1

if st.session_state['progress'] == 2:
    select_gender = st.selectbox('Seleziona Genere', ('Male', 'Female'))
    st.write('Hai selezionato ', select_gender)
    result = select_gender
    confirm = st.button('Next', 2)
    if confirm:
        st.session_state['gender'] = b.transform_gender(result)
        st.session_state['progress'] += 1

if st.session_state['progress'] == 3:
    select_city = st.selectbox('Seleziona Città', ('Bangalore', 'New Delhi', 'Pune'))
    st.write('Hai selezionato ', select_city)
    result = select_city
    confirm = st.button('Next', 3)
    if confirm:
        st.session_state['city'] = b.transform_city(result)
        st.session_state['progress'] += 1

if st.session_state['progress'] == 4:
    select_education = st.selectbox('Seleziona Educazione', ('Bachelor', 'Master', 'PHD'))
    st.write('Hai selezionato ', select_education)
    result = select_education
    confirm = st.button('Next', 4)
    if confirm:
        st.session_state['education'] = b.transform_education(result)
        st.session_state['progress'] += 1

if st.session_state['progress'] == 5:
    possible_years = []
    for i in range(0, 14):
        possible_years.append(i+2010)
    st.text('In che anno sei entrato a far parte dell''azienda?')
    select_joining_year = st.selectbox('Seleziona Anno', possible_years)
    st.write('Hai selezionato ', select_joining_year)
    result = select_joining_year
    confirm = st.button('Next', 5)
    if confirm:
        st.session_state['joining_year'] = result
        st.session_state['progress'] += 1    

if st.session_state['progress'] == 6:
    possible_experience = []
    for i in range(0, 8):
        possible_experience.append(i)
    st.text('Qual''è il tuo livello di esperienza?')
    select_experience = st.selectbox('Seleziona Esperienza', possible_experience)
    st.write('Hai selezionato ', select_experience)
    result = select_experience
    confirm = st.button('Next', 6)
    if confirm:
        st.session_state['experience'] = result
        st.session_state['progress'] += 1

if st.session_state['progress'] == 7:
    select_payment_tier = st.selectbox('Seleziona Tier di Pagamento', (1, 2, 3))
    st.write('Hai selezionato ', select_payment_tier)
    result = select_payment_tier
    confirm = st.button('Next', 7)
    if confirm:
        st.session_state['payment_tier'] = b.transform_payment_tier(result)
        st.session_state['progress'] += 1

if st.session_state['progress'] == 8:
    st.text('Sei mai stato messo in panchina da un progetto per più di un mese?')
    select_ever_benched = st.selectbox('Seleziona Risposta', ('No', 'Yes'))
    st.write('Hai selezionato ', select_ever_benched)
    result = select_ever_benched
    confirm = st.button('Next', 8)
    if confirm:
        st.session_state['ever_benched'] = b.transform_ever_benched(result)
        st.session_state['progress'] += 1

if st.session_state['progress'] == 9:
    st.write(st.session_state['education'], st.session_state['joining_year'], st.session_state['city'], st.session_state['payment_tier'],
                        st.session_state['age'], st.session_state['gender'], st.session_state['ever_benched'], st.session_state['experience']) #debug
    leave_or_not = b.predict(st.session_state['education'], st.session_state['joining_year'], st.session_state['city'], st.session_state['payment_tier'],
                        st.session_state['age'], st.session_state['gender'], st.session_state['ever_benched'], st.session_state['experience'])
    if leave_or_not:
        st.text('Entro due anni, l''impiegato lascerà l''azienda!!!')
    else:
        st.text('Probabilmente, l''impiegato non lascerà l''azienda nei prossimi due anni.')
    back_button = st.button("Back to Homepage")
    if back_button:
        st.session_state['progress'] = 0
