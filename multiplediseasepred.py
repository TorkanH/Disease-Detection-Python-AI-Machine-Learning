# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:54:00 2023

@author: Torkan Hesari 

disease prediction project with python machine learning for Innova bootcamp 

"""


#import the libraries:
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models of the disease using pickle:
diabetes_model = pickle.load(open("C:/Users/torka/OneDrive/Desktop/multiple disease prediction system/saved models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("C:/Users/torka/OneDrive/Desktop/multiple disease prediction system/saved models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("C:/Users/torka/OneDrive/Desktop/multiple disease prediction system/saved models/parkinsons_model.sav", "rb"))
breastcancer_model = pickle.load(open("C:/Users/torka/OneDrive/Desktop/multiple disease prediction system/saved models/breastcancer_model.sav", "rb"))

#create SIDEBAR for navigation using streamlit_option_menu:
#default_index = 0 -> means that the deafult id the first one in this page diabetes if =1 -> heart if =2 ->parkinson would be deafault disease
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System:",
                           
                           ["Diabetes Prediction",
                           "Heart Disease Prediction",
                           "Parkinsons Prediction",
                           "BreastCancer Prediction"],
                           
                           icons = ["droplet-fill", "activity", "person","gender-female"],
                           
                           default_index = 0)
    
    

    
#Diabetes Prediction Page:
if(selected == "Diabetes Prediction"):
    
    #page title
    st.markdown("<h1 style='color: #66bfbf;'>Diabetes Prediction using Machine Learning</h1>", unsafe_allow_html=True)

    
    # getting the input data from the user
    #create input fields with text_input st lib:
    #Number of Pregnancis : title of inputs
    #Pregnancies: variable that will store the input the user gives
    
    #make 2 columns for input fields in form:
    col1,col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
   
   
   
    # code for Prediction
    #empty string -> to save the End Result if the person has or does'nt have diabetes!
    diab_diagnosis = ""
   
   
    # creating a button for Prediction
    if st.button("Diabetes Test Result:"):
        #[[]] -> to show that we are predicting for one model
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
        #check if the person is diabetic or not and display the result.
        if (diab_prediction[0] == 1 ):
            diab_diagnosis = "The person is Diabetic!"
        else:#value is zero.
            diab_diagnosis = "The person is NOT Diabetic:)"
    
    #display the result
    st.success(diab_diagnosis)

       
       
       
#Heart Disease Prediction Page:     
if(selected == "Heart Disease Prediction"):
    
    #page title will be:
        
    st.markdown("<h1 style='color: #66bfbf;'>Heart Disease Prediction using Machine Learning</h1>", unsafe_allow_html=True)

    
    col1,col2 = st.columns(2)
    
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col1:
        cp = st.text_input("Chest Pain Types")
    with col2:
        trestbps = st.text_input("Resting Blood Pressure")
    with col1:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col2:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg =st.text_input("Resting Electrocardiagraphic result")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col1:
        exang = st.text_input("Exercise Induced Angina")
    with col2:
        oldpeak = st.text_input("ST Depression Included By Exercise")
    with col1:
        slope = st.text_input("Slope Of The Peak Exercise ST Segment")
    with col2:
        ca = st.text_input("Major Vessels Colored By Flourosopy")
    with col1:
        thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        
        
    #code for heart disease prediction:
    heart_disease_diagnosis = ""
    
    
    #craete button for heart prediction
    if st.button("Heart Disease Test Result"):
        input_data = [[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]]
        heart_disease_prediction = heart_disease_model.predict(input_data)
        
        if(heart_disease_prediction[0] == 1):
            heart_disease_diagnosis = "The Person has Heart Disease!"
        else:
            heart_disease_diagnosis = "The person does NOT have Heart Disease:)"
            
    #display person's health consition        
    st.success(heart_disease_diagnosis)
    
    
    
    
  
    
#Parkinsons Prediction Page:
if (selected =="Parkinsons Prediction"):
    
    #page title will be 
    st.markdown("<h1 style='color: #66bfbf;'>Parkinson's Disease Prediction using Machine Learning</h1>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    
    with col1:
        fo = st.text_input("MDVP: Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP: Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP: Flo(Hz)")
    with col1:
        Jitter_percent = st.text_input("MDVP: Jitter(%)")
    with col2:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        RAP = st.text_input("MDVP(RAP)")
    with col1:
        PPQ = st.text_input("MDVP(PPQ)")
    with col2:
        DDP = st.text_input("Jitter(DDP)")
    with col3:
        Shimmer = st.text_input("MDVP(Shimmer)")
    with col1:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        APQ3 = st.text_input("Shimmer:APQ3")
    with col3:
        APQ5 = st.text_input("Shimmer:APQ5")
    with col1:
        APQ = st.text_input("MDVP:APQ")
    with col2:
        DDA = st.text_input("Shimmer:DDA")
    with col3:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col3:
        D2 = st.text_input("D2")
    with col1:
        PPE = st.text_input("PPE")
        
    
    
    #code for parkinsoms prediction:
    parkinsons_diagnosis = ""
    
    #create a button for parkinsons prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_disease_prediction =parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if(parkinsons_disease_prediction[0] == 1):
            parkinsons_diagnosis = "The Person has Parkinsons!"
        else:
            parkinsons_diagnosis = "The Person does NOT have Parkinson's disease:)"

    #dispaly the end result for the parkinson disease detection:
    st.success(parkinsons_diagnosis)
        
  
        
#Breast cancer prediction Page:
if(selected == "BreastCancer Prediction"):
    #page title
    st.markdown("<h1 style='color: #66bfbf;'>Breast Cancer Prediction using Machine Learning</h1>", unsafe_allow_html=True)
    
    # getting the input data from the user
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        radius_mean = st.text_input('Radius mean')
    with col2:
        texture_mean = st.text_input('Texture mean')
    with col3:
        perimeter_mean = st.text_input('Perimeter mean')
    with col4:
        area_mean =st.text_input('Area mean')
    with col1:
        smoothness_mean = st.text_input("Smoothness mean")
    with col2:
        compactness_mean = st.text_input("Compactness mean")
    with col3:
        concavity_mean = st.text_input("Concavity mean")
    with col4:
        concave_points_mean = st.text_input("Concave Points Mean")
    with col1:
        symmetry_mean = st.text_input("Symmetry mean")
    with col2:
        fractal_dimension_mean =st.text_input("Fractal Dimension Mean")
    with col3:
        radius_se =st.text_input("Radius se")
    with col4:
        texture_se = st.text_input("Texture Se")
    with col1:
        perimeter_se = st.text_input("Perimeter se")
    with col2:
        area_se = st.text_input("Area se")
    with col3:
        smoothness_se = st.text_input("Smoothness se")
    with col4:
        compactness_se = st.text_input("Compactness se")
    with col1:
        concavity_se = st.text_input("Concavity se")
    with col2:
        concave_points_se = st.text_input("Concave Points se")
    with col3:
        symmetry_se = st.text_input("symmetry se")
    with col4:
        fractal_dimension_se = st.text_input("Fractal Dimmension")
    with col1:
        radius_worst = st.text_input("Radius worst")
    with col2:
        texture_worst = st.text_input("Texture Worst")
    with col3:
        perimeter_worst =st.text_input("Perimeter worst")
    with col4:
        area_worst = st.text_input("Area worst")
    with col1:
        smoothness_worst = st.text_input("Smoothness worst")
    with col2:
        compactness_worst = st.text_input("Compactness worst")
    with col3:
        concavity_worst = st.text_input("Concavity worst")
    with col4:
        concave_points_worst =st.text_input("Concave Points Worst")
    with col1:
        symmetry_worst = st.text_input("Symmetry Worst")
    with col2:
        fractal_dimension_worst = st.text_input("Fractal Dimension worst")
        
    # code for Prediction
    breastcancer_diagnosis = ""
     
    # creating a button for Prediction
    if st.button("Breast Cancer Test Result"):
        #[[]] -> to show that we are predicting for one model
        breastcancer_prediction = breastcancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean,
                                                               symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se,
                                                               concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, 
                                                               compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])
       
        #check if the person is diabetic or not and display the result.
        if (breastcancer_prediction[0] == 'M' ):
            breastcancer_diagnosis = "The person has Breast Cancer"
        else:
            breastcancer_diagnosis = "The person dose NOT have breast cancer:)"
    
    #display the result
    st.success(breastcancer_diagnosis)
        
        
        
        
    
        