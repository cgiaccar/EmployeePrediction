"""
The questions are changed using the session_state variable 'progress'

BackEnd.py is called to transform the user inputs (when necessary)
 and to predict the final result
"""

import streamlit as st
import os
import base64
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

st.title("EmployeePrediction")

if 'progress' not in st.session_state:
    # progress stores which question is being answered.
    # 0 means the test has not been started yet.
    # 9 means the test has been completed.
    # questions order —
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

# st.write('progress = ', st.session_state['progress']) #debug


# Background image loading:
path = os.path.dirname(os.path.dirname(__file__))
image_file = path+'/Assets/crystalball_semitransparent.png'
# image comes from https://commons.wikimedia.org/wiki/File:744-crystal-ball-2.svg
# license: creative commons 4.0


def add_bg_from_local(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(191, 141, 242, 0.4);
        background-size: auto
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local(image_file)


if st.session_state['progress'] == 0:
    st.subheader(
        'Hello! With this tool you will be able to see if you or an employee working for your company will leave in 2 years or less.')
    st.write('**Just take our quiz and let the magic begin!**')
    begin = st.button("Begin!")
    if begin:
        if st.session_state['progress'] < 1:
            st.session_state['progress'] = 1
            # experimental_rerun reruns the script from the top
            # using the updated session_state
            st.experimental_rerun()

if st.session_state['progress'] == 1:
    possible_ages = []
    for i in range(0, 83):
        possible_ages.append(i+18)
    st.write('**How old are you?**')
    select_age = st.selectbox('Select age', possible_ages)
    st.write('You selected ', select_age)
    result = select_age
    # 1 is the button key, otherwise generated based on the content
    confirm = st.button('Next', 1)
    if confirm and result >= 18:
        st.session_state['age'] = result
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 2:
    select_gender = st.selectbox('Select Gender', ('Male', 'Female'))
    st.write('You selected ', select_gender)
    result = select_gender
    confirm = st.button('Next', 2)
    if confirm:
        st.session_state['gender'] = b.transform_gender(result)
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 3:
    select_city = st.selectbox(
        'Select City', ('Bangalore', 'New Delhi', 'Pune'))
    st.write('You selected ', select_city)
    result = select_city
    confirm = st.button('Next', 3)
    if confirm:
        st.session_state['city'] = b.transform_city(result)
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 4:
    select_education = st.selectbox(
        'Select Education', ('Bachelor', 'Master', 'PHD'))
    st.write('You selected ', select_education)
    result = select_education
    confirm = st.button('Next', 4)
    if confirm:
        st.session_state['education'] = b.transform_education(result)
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 5:
    possible_years = []
    for i in range(0, 14):
        possible_years.append(i+2010)
    st.write('**In what year did you join the company?**')
    select_joining_year = st.selectbox('Select Year', possible_years)
    st.write('You selected ', select_joining_year)
    result = select_joining_year
    confirm = st.button('Next', 5)
    if confirm:
        st.session_state['joining_year'] = result
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 6:
    possible_experience = []
    for i in range(0, 8):
        possible_experience.append(i)
    st.write('**What is your experience level?**')
    st.write('**Make your best guess on a scale from 0 to 7.**')
    select_experience = st.selectbox('Select experience', possible_experience)
    st.write('You selected ', select_experience)
    result = select_experience
    confirm = st.button('Next', 6)
    if confirm:
        st.session_state['experience'] = result
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 7:
    st.write('**What payment tier are you in?**')
    st.write('**1 means high payment, 2 means medium payment, 3 means low payment.**')
    st.write('**Please make your best estimate.**')
    select_payment_tier = st.selectbox('Select payment tier', (1, 2, 3))
    st.write('You selected ', select_payment_tier)
    result = select_payment_tier
    confirm = st.button('Next', 7)
    if confirm:
        st.session_state['payment_tier'] = b.transform_payment_tier(result)
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 8:
    st.write('**Have you ever been benched from a project for more than a month?**')
    select_ever_benched = st.selectbox('Select answer', ('No', 'Yes'))
    st.write('You selected ', select_ever_benched)
    result = select_ever_benched
    confirm = st.button('See Results!', 8)
    if confirm:
        st.session_state['ever_benched'] = b.transform_ever_benched(result)
        st.session_state['progress'] += 1
        st.experimental_rerun()

if st.session_state['progress'] == 9:
    # st.write(st.session_state['education'], st.session_state['joining_year'], st.session_state['city'], st.session_state['payment_tier'],
    #                    st.session_state['age'], st.session_state['gender'], st.session_state['ever_benched'], st.session_state['experience']) #debug
    will_leave = b.predict(st.session_state['education'], st.session_state['joining_year'], st.session_state['city'], st.session_state['payment_tier'],
                           st.session_state['age'], st.session_state['gender'], st.session_state['ever_benched'], st.session_state['experience'])
    if will_leave:
        st.subheader(
            '**WATCH OUT! Our prediction says that, in two years, the employee WILL LEAVE the company!!!**')
    else:
        st.subheader(
            '**Our prediction says that, probably, the employee will NOT leave the company for the next two years.**')
    back_button = st.button("Retake the Quiz!")
    if back_button:
        st.session_state['progress'] = 0
        st.experimental_rerun()
