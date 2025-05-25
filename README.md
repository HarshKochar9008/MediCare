# MediCare - Medical Image Analysis System

A full-stack web application for medical image analysis using deep learning. The system can process X-ray and MRI images to predict potential diseases.

## Features

- Upload and analyze X-ray/MRI images
- Optional medical report attachment
- Deep learning-based disease prediction
- Confidence score visualization
- User-friendly interface

## Project Structure

```
MediCare/
├── app/
│   ├── backend/
│   │   ├── main.py
│   │   └── model.py
│   └── frontend/
│       └── app.py
├── models/
│   └── dummy_model.py
├── static/
│   └── styles/
├── templates/
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the FastAPI backend:
```bash
cd app/backend
uvicorn main:app --reload
```

4. In a new terminal, start the Streamlit frontend:
```bash
cd app/frontend
streamlit run app.py
```

5. Access the application:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Note

This is a development version with a dummy model for testing purposes. Replace the dummy model with a real trained model for production use. 