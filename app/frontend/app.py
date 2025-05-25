import streamlit as st
import requests
import json
from PIL import Image
import io
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(
    page_title="MediCare - Medical Image Analysis",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
    }
    
    /* Title styling */
    .title-text {
        font-size: 3rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Subtitle styling */
    .subtitle-text {
        font-size: 1.2rem;
        color: #34495e;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    # /* Upload area styling */
    # .upload-area {
    #     background-color: white;
    #     padding: 2rem;
    #     border-radius: 15px;
    #     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    #     margin-bottom: 2rem;
    # }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background-color: #3498db;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
    }
    
    /* Prediction box styling */
    .prediction-box {
        background: linear-gradient(135deg, #3498db, #2980b9);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .prediction-box h3 {
        color: white;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #7f8c8d;
        font-size: 0.9rem;
    }
    
    # /* Progress bar styling */
    # .stProgress > div > div {
    #     background-color: #000000;
    # }
    
    /* File uploader styling */
    .stFileUploader {
        background-color: grey;
        padding: 1rem;
        border-radius: 10px;
        border: 2px dashed #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/hospital-3.png", width=100)
    st.markdown("## MediCare")
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This application uses advanced deep learning to analyze medical images and provide disease predictions.
    
    **Features:**
    - X-ray & MRI analysis
    - Disease prediction
    - Confidence scoring
    - Detailed visualization
    """)
    
    st.markdown("---")
    st.markdown("### Instructions")
    st.markdown("""
    1. Upload your medical image
    2. Click 'Analyze Image'
    3. View the results
    """)

st.markdown('<h1 class="title-text">🏥 MediCare</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Advanced Medical Image Analysis with Deep Learning</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="upload-area">', unsafe_allow_html=True)
    st.markdown("### Upload Image")
    uploaded_file = st.file_uploader("Choose an X-ray or MRI image", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=300)
        
        if st.button("🔍 Analyze Image", key="analyze"):
            try:
                with st.spinner("Analyzing image..."):
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                    
                    response = requests.post("http://localhost:8000/analyze", files=files)
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        with col2:
                            st.markdown("### Analysis Results")
                            
                            st.markdown(f"""
                                <div class="prediction-box">
                                    <h3>Prediction: {result['prediction']}</h3>
                                    <p>Confidence: {result['confidence']:.2%}</p>
                                </div>
                            """, unsafe_allow_html=True)
                            
                            scores = result['all_scores']
                            fig, ax = plt.subplots(figsize=(10, 4))
                            conditions = list(scores.keys())
                            values = list(scores.values())

                            bars = ax.bar(conditions, values, color=['#3498db', '#ffffff', '#e74c3c'])
                            ax.set_ylim(0, 1)
                            ax.set_ylabel('Confidence Score', fontsize=12)
                            ax.set_title('Prediction Confidence Scores', fontsize=14, pad=20)
                            
                            for bar in bars:
                                height = bar.get_height()
                                ax.text(bar.get_x() + bar.get_width()/2., height,
                                        f'{height:.2%}',
                                        ha='center', va='bottom', fontsize=10)
                            
                            plt.xticks(rotation=45, fontsize=10)
                            plt.grid(axis='y', linestyle='--', alpha=0.7)
                            plt.tight_layout()
                            
                            st.pyplot(fig)
                            
                    else:
                        st.error("Error analyzing image. Please try again.")
                        
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>Note: This is a demonstration version with a dummy model. Results are simulated for testing purposes.</p>
        <p>© 2025 MediCare - Medical Image Analysis System by HK</p>
    </div>
""", unsafe_allow_html=True) 