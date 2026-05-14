import streamlit as st
import pickle
import numpy as np

# 1. Page Config
st.set_page_config(page_title="AI Health Premium", page_icon="⚡", layout="wide")

# 2. Custom CSS (Wahi Ultra Dark Theme jo aapko pasand hai)
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #0e1117 0%, #040507 100%);
        color: #ffffff;
    }
    .main-title {
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .prediction-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(194, 233, 251, 0.2);
        backdrop-filter: blur(5px);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
        margin-top: 20px;
    }
    .price-text {
        font-size: 60px;
        color: #a1c4fd;
        font-weight: bold;
        text-shadow: 0 0 25px rgba(161, 196, 253, 0.5);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 20px;
        width: 100%;
        box-shadow: 0 6px 20px rgba(118, 75, 162, 0.4);
        margin-top: 20px;
    }
    /* Input field background fix */
    .stNumberInput, .stSelectbox {
        background-color: rgba(255,255,255,0.05);
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Model Load
@st.cache_resource
def load_model():
    return pickle.load(open('insurance_model.pkl', 'rb'))

model = load_model()

# 4. Header
st.markdown("<h1 class='main-title'>⚡Insurance Cost Prediction by Ajay ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Advanced analytics for your insurance premium estimation.</p>", unsafe_allow_html=True)
st.write("---")

# 5. UI Layout - One Page Form
col_info, col_form = st.columns([1, 1.5], gap="large")

with col_info:
    st.markdown("### 🏥 Health Analytics")
    st.info("""
    **Did you know?**
    - Smoker status has the highest impact on premiums.
    - Maintaining a BMI under 25 can save up to 20% on costs.
    - Regular checkups help in early risk detection.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=200)

with col_form:
    st.write("#### 📝 Fill All Details")
    
    # Grid Layout for Inputs
    r1_c1, r1_c2 = st.columns(2)
    with r1_c1:
        age = st.number_input("Age (Years)", 1, 100, 25)
        bmi = st.number_input("Body Mass Index (BMI)", 10.0, 60.0, 24.5)
        sex = st.selectbox("Gender", ["Male", "Female"])
    
    with r1_c2:
        children = st.selectbox("No. of Children", [0,1,2,3,4,5])
        smoker = st.selectbox("Smoker?", ["Yes", "No"])
        region = st.selectbox("Region", ["Southeast", "Other"])

    # --- BUTTON KO FORM KE NICHE SET KIYA ---
    predict_btn = st.button("🚀 Calculate Estimated Annual Premium")

# Data Transformation (Button ke bahar)
is_female = 1 if sex == "Female" else 0
is_smoker = 1 if smoker == "Yes" else 0
region_southeast = 1 if region == "Southeast" else 0
bmi_category_Obese = 1 if bmi >= 30 else 0

# 6. Prediction Logic
if predict_btn:
    input_data = np.array([age, is_female, bmi, children, is_smoker, region_southeast, bmi_category_Obese]).reshape(1, -1)
    prediction = model.predict(input_data)
    
    st.markdown(f"""
        <div class="prediction-box">
            <h2 style='color: #ffffff; font-weight: 300;'>Estimated Annual Insurance Premium</h2>
            <div class="price-text">${prediction[0]:,.2f}</div>
            <p style='color: #8b949e;'>Calculation based on AI-optimized risk analysis.</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()

# 7. Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Developed with ❤️ by Ajay | For Educational Purposes")