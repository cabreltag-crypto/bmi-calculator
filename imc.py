import streamlit as st 

st.title('welcome to my BMI calculator')
weight = st.number_input('enter you weight in Kg')
status = st.radio('select your height format: ',('cms','meters','feet'))

try:
    if status == 'cms':
        height = st.number_input('centimeters')
        bmi = weight /((height/100)**2)
    elif status == 'meters':
        height = st.number_input('meters')
        bmi = weight /((height)**2)
    else:
        height = st.number_input('feet')
        bmi = weight /((height/3.28)**2)
except:
    print('zero division error')

if(st.button('calculate BMI')):
    st.write('Your BMI index is {}'.format(round(bmi)))
    if bmi < 16:
        st.error('Your ARE EXTREMELY UNDERWEIGHT')
    elif 16 < bmi <18.5:
         st.warning('Your ARE UNDERWEIGHT')
    elif 18.5 <= bmi < 25:
         st.succes('Your ARE HEALTHY')   
    elif 25 <= bmi < 30:
         st.warning('Your ARE OVERWEIGHT')
    else:
         st.error('Your ARE EXTREMELY OVERWEIGHT')  
