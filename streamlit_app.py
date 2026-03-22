import os
import pandas as pd
import streamlit as st
from mlproject.pipeline.prediction import PredictionPipeline

st.set_page_config(
    page_title="Drink Quality Detection",
    page_icon="🍷",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #3b0a45, #6a0572, #1b1b2f, #16213e);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    min-height: 100vh;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
}

.custom-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 20px;
    color: white;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
}

.main-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
    color: white;
}

.subtitle {
    text-align: center;
    margin-bottom: 1.8rem;
    color: #ddd;
    font-size: 1rem;
}

.field-label {
    color: white;
    font-size: 15px;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 0.25rem;
}

.field-range {
    float: right;
    color: #ccc;
    font-size: 12px;
    font-weight: 400;
}

.small-note {
    color: #ffb3c6;
    font-size: 13px;
    margin-top: -0.25rem;
    margin-bottom: 0.75rem;
}

.result-card {
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(15px);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
    color: white;
    margin-top: 1.5rem;
}

.result-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 20px;
}

.result-good {
    color: #00ffab;
    font-size: 30px;
    font-weight: bold;
    margin: 20px 0;
}

.result-bad {
    color: #ff4b5c;
    font-size: 30px;
    font-weight: bold;
    margin: 20px 0;
}

.footer-box {
    margin-top: 25px;
    text-align: center;
    font-size: 14px;
    color: #bbb;
}

.footer-box a {
    color: #ff9a9e;
    text-decoration: none;
    margin: 0 6px;
}

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    width: 100%;
    padding: 0.8rem 1rem;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
    color: white;
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.markdown('<div class="main-title">🍷 Drink Quality Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Adjust the wine chemistry values and analyze quality</div>', unsafe_allow_html=True)

st.markdown("### Train Model")
if st.button("Train Model"):
    with st.spinner("Training model..."):
        os.system("python main.py")
    st.success("Model training completed.")

st.markdown("---")

with st.form("prediction_form"):
    st.markdown("### Enter Wine Features")

    st.markdown('<div class="field-label">Fixed Acidity</div>', unsafe_allow_html=True)
    fixed_acidity = st.slider("fixed_acidity", 4.0, 16.0, 8.0, 0.1, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {fixed_acidity}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Volatile Acidity</div>', unsafe_allow_html=True)
    volatile_acidity = st.slider("volatile_acidity", 0.1, 1.6, 0.5, 0.01, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {volatile_acidity}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Citric Acid</div>', unsafe_allow_html=True)
    citric_acid = st.slider("citric_acid", 0.0, 1.0, 0.3, 0.01, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {citric_acid}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Residual Sugar</div>', unsafe_allow_html=True)
    residual_sugar = st.slider("residual_sugar", 0.5, 15.0, 2.0, 0.1, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {residual_sugar}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Chlorides</div>', unsafe_allow_html=True)
    chlorides = st.slider("chlorides", 0.01, 0.6, 0.08, 0.01, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {chlorides}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Free Sulfur Dioxide</div>', unsafe_allow_html=True)
    free_sulfur_dioxide = st.slider("free_sulfur_dioxide", 1, 75, 15, 1, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {free_sulfur_dioxide}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Total Sulfur Dioxide</div>', unsafe_allow_html=True)
    total_sulfur_dioxide = st.slider("total_sulfur_dioxide", 6, 300, 46, 1, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {total_sulfur_dioxide}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Density</div>', unsafe_allow_html=True)
    density = st.slider("density", 0.990, 1.005, 0.996, 0.001, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {density:.3f}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">pH</div>', unsafe_allow_html=True)
    pH = st.slider("pH", 2.8, 4.0, 3.3, 0.01, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {pH}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Sulphates</div>', unsafe_allow_html=True)
    sulphates = st.slider("sulphates", 0.3, 2.0, 0.65, 0.01, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {sulphates}</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Alcohol %</div>', unsafe_allow_html=True)
    alcohol = st.slider("alcohol", 8.0, 15.0, 10.0, 0.1, label_visibility="collapsed")
    st.markdown(f'<div class="small-note">Value: {alcohol}</div>', unsafe_allow_html=True)

    submitted = st.form_submit_button("Analyze Quality")

if submitted:
    try:
        columns = [
            'fixed acidity',
            'volatile acidity',
            'citric acid',
            'residual sugar',
            'chlorides',
            'free sulfur dioxide',
            'total sulfur dioxide',
            'density',
            'pH',
            'sulphates',
            'alcohol'
        ]

        data = pd.DataFrame([[
            fixed_acidity, volatile_acidity, citric_acid,
            residual_sugar, chlorides, free_sulfur_dioxide,
            total_sulfur_dioxide, density, pH,
            sulphates, alcohol
        ]], columns=columns)

        obj = PredictionPipeline()
        prediction = obj.predict(data)
        final_result = str(prediction[0])

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="result-title">🍷 Prediction Result</div>', unsafe_allow_html=True)

        if final_result == '1':
            st.markdown('<div class="result-good">Good Quality Drink ✅</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-bad">Low Quality Drink ❌</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Something went wrong: {e}")

st.markdown("""
<div class="footer-box">
    Developed by <strong>Shivansh Vyas</strong><br><br>
    <a href="https://www.linkedin.com/in/shivanshvyas/" target="_blank">LinkedIn</a> |
    <a href="https://github.com/Shivanshvyas1729" target="_blank">GitHub</a> |
    <a href="mailto:shivanshvyas1729@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)