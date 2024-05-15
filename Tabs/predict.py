import streamlit as st
from Train import predict


@st.cache_data(persist=True)
def load_data():
    pass

@st.cache_data(persist=True)
def predict_stroke(X, y, features):
    pass

def app(df, X, y):
    data = load_data()
    st.markdown(
    """
    <h1 style='color: red; text-align: left;'>CARDIOVASACULAR FORECASTING USING MACHINE LEARNING</h1>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        """
            <p style="font-size:25px">
                This Application uses <b style="color:green">Decision Tree Classifier</b> for Cardiovascular Forecasting using Machine Learning.
            </p>
        """, unsafe_allow_html=True)
    st.markdown(
        """
            <p style="font-size:25px">
                This Application was <b style="color:green">Developed by ,</b>
                \n<b style="font-size:20px; padding-left:9cm;"> S.HARIKISHORE</b> 
                \n<b style="font-size:20px; padding-left:9cm;"> V.CIBIRAJAN</b> 
                \n<b style="font-size:20px; padding-left:9cm;"> S.SAKTHIVEL</b> 
            </p>
        """, unsafe_allow_html=True)
    st.markdown(
        """
            <p style="font-size:25px">
                This Project was <b style="color:green">Guided by ,</b>
                \n<b style="font-size:20px; padding-left:9cm;">Dr T.SARAVANAN</b> 
            </p>
        """, unsafe_allow_html=True)
    st.markdown("""General Convention:
    \n 0 -> Absent or False
    \n 1 -> Present or True\n 
    
    \nSex:\n
    0 -> Male
    1 -> Female
    
    """)
    
    
    # Take input of features from the user.
    A = st.slider("Age", int(df["age"].min()), int(df["age"].max()))
    B = st.slider("Sex", int(df["sex"].min()), int(df["sex"].max()))
    C= st.slider("Cerebral palsy", int(df["cp"].min()), int(df["cp"].max()))
    D = st.slider("Trestbps", int(df["trestbps"].min()), int(df["trestbps"].max()))
    E = st.slider("Cholesterol", int(df["chol"].min()), int(df["chol"].max()))
    F = st.slider("Fasting blood sugar", int(df["fbs"].min()), int(df["fbs"].max()))
    G = st.slider("Restecg", int(df["restecg"].min()), int(df["restecg"].max()))
    H = st.slider("Maximum Heart Rate", int(df["thalach"].min()), int(df["thalach"].max()))
    I = st.slider("Exercise Induced Angina", int(df["exang"].min()), int(df["exang"].max()))
    J = st.slider("Oldpeak", float(df["oldpeak"].min()), float(df["oldpeak"].max()))
    K = st.slider("Slope", int(df["slope"].min()), int(df["slope"].max()))
    L = st.slider("Cancer", int(df["ca"].min()), int(df["ca"].max()))
    M = st.slider("Thalassemia", int(df["thal"].min()), int(df["thal"].max()))
    
    features = [A,B,C,D,E,F,G,H,I,J,K,L,M]
    if st.button("Predict"):
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")
        if (prediction == 1):
            st.warning("The patient is likely to have heart disease!!")
        else:
            st.success("The patient is not likely to have heart disease!!")
