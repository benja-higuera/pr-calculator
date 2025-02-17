import streamlit as st
import pandas as pd
import numpy as np

st.write("# PR Calculator")

# Group multiple widgets:
with st.form(key='my_form'):
    peso = st.number_input('Peso (kg) : ', min_value=1,value=1)
    numero_repeticiones = st.number_input('Numero de repeticiones', min_value=1,value=1)
    st.form_submit_button('Calcular')
    
peso = float(peso)
numero_repeticiones = float(numero_repeticiones)

rm_Brzyck = peso /(1.0278-(0.0278*numero_repeticiones ))
rm_Brzyck_2 = (peso * 36) / (37 - numero_repeticiones)

if numero_repeticiones > 12 : 
    st.write('Para numeros sobre 12 los calculos pueden ser erroneos')
if numero_repeticiones > 20 and numero_repeticiones < 100 :
    st.write('El numero de repeticiones es demasiado alto, los calculos probablemente no tengan sentido')
if numero_repeticiones > 100 :
    st.write('vo so tonto como vas a hacer ', numero_repeticiones, ' repeticiones?')

if peso > 100 :
    st.write('que buen peso skibidi')

st.write( "RM según formula deBrzyck : ", rm_Brzyck_2)