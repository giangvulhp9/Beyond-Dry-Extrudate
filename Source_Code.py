import numpy as np
import streamlit as st

st.title('Dry Extrudate Calculator :computer:')


def hydrated_regular_extrudate_components(Regular_large, Regular_Medium, Regular_Fine, s1, s2, s3):
    """
    s1, s2 and s3 are ratio of dry large, medium and fine use in the final product

    """
    return s1*Regular_large + s2*Regular_Medium + s3*Regular_Fine
st.write("#")
st.header('**Input data**')
st.write("#")
st.subheader(':red[Hydrated PSD of regular extrudate]')

col1, empty1, col2, empty2, col3 = st.columns([3, 0.75, 3, 0.75 ,4.5])
with col1:

    st.write('Hydrated PSD ratio of regular medium is:')
    RM_large = st.slider('large',float (0),float(1),0.01, None, None, 1)
    RM_medium = st.slider('medium',float (0),float(1),0.01, None, None, 2)

with empty1:
    st.empty()

with col2:
    st.write('Hydrated PSD ratio of regular fine is:')
    RF_medium = st.slider('medium',float (0),float(1),0.01, None, None, 3)
    RF_fine = st.slider('fine',float (0),float(1),0.01, None, None, 4)

with empty2:
    st.empty()

with col3:
    Regular_large = np.array([1, 0, 0])
    Regular_Medium = np.array([RM_large, RM_medium, 0])
    Regular_Fine = np.array([0, RF_medium, RF_fine])
    s1 = st.number_input ('Amount of regular large used in grams is')
    s2 = st.number_input ('Amount of regular medium used in grams is')
    s3 = st.number_input ('Amount of regular fine used in grams is')

hydrated_regular_extrudate_components = hydrated_regular_extrudate_components(Regular_large, Regular_Medium, Regular_Fine, s1, s2, s3)
HRE = np.transpose(hydrated_regular_extrudate_components)
st.write('**Hydrated PSD (Large: Meidum: Fine) of control regular extrudate is:**')
st.write(HRE)

def optimization_dry_extrudate_needed (HDE, HRE):
    HDE_tp = np.transpose(HDE)
    product = np.dot(HDE_tp, HDE)
    product_inv = np.linalg.inv (product)
    product_2 = np.dot(product_inv, HDE_tp)
    dry_extrudate_needed = np.dot(product_2, HRE)
    return dry_extrudate_needed

st.write("####")
st.subheader(':red[Hydrated PSD of Dry extrudate]')

col4, col5 = st.columns(2)

with col4:
    st.write('From hydrated PSD ratio of Dry_medium is:')
    DM_large = st.slider('large',float (0),float(1),0.01, None, None, 5)
    DM_medium = st.slider('medium',float (0),float(1),0.01, None, None, 6)

with col5:
    st.write('From hydrated PSD ratio of Dry_fine is:')
    DF_medium = st.slider('medium',float (0),float(1),0.01, None, None, 7)
    DF_fine = st.slider('fine',float (0),float(1),0.01, None, None, 8)



HDE = np.array ([[DM_large, 0],[DM_medium, DF_medium],[0, DF_fine]])
result = optimization_dry_extrudate_needed (HDE, HRE)
final_ratio = np.dot(HDE, result)

st.write("####")
st.header('Result')
st.write("#")
st.write('Amount of Dry extrudate needed is (Medium : Fine) ')
st.write(result)
st.write('From that, the PSD of the Dry extrudate after hydration will be (Large: Medium: Fine)')
st.write(final_ratio)
