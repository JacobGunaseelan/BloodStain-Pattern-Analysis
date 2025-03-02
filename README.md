# Bloodstain Pattern Analysis

## Overview
Bloodstain Pattern Analysis (BPA) is an AI-powered forensic tool that classifies bloodstain patterns from images. It helps in crime scene investigations by identifying the type of stain, weapon used, impact surface, and movement.

## Features
- Upload and analyze bloodstain images
- Predicts stain type, weapon, impact surface, and movement
- Uses deep learning for classification
- User-friendly web interface

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript (React/Flask-based UI)
- **Backend:** Python (Flask, FastAPI)
- **Machine Learning:** TensorFlow/Keras.

---

## Installation & Setup
### 1. Clone the Repository
```bash
[git clone https://github.com/your-username/bloodstain-analysis.git
cd bloodstain-analysis](https://github.com/JacobGunaseelan/BloodStain-Pattern-Analysis)
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
#### Backend Server:
```bash
python app.py
```
#### Frontend (if React is used):
```bash
cd frontend
npm install
npm start
```

---

## Dataset & Model Training
### 1. Data Collection
- Use forensic datasets of bloodstain patterns.

### 2. Model Training
```python
python train_model.py
```
- Uses CNN for image classification.
- Saves model weights (`model.h5`).

---

## Usage
1. Upload a bloodstain image.
2. Click "Predict".
3. View stain classification details.

---

## Future Enhancements
- Improve model accuracy with more training data.
- Implement real-time video analysis.
- Add a mobile-friendly UI.

---

## License
MIT License.

---

## Contributors
- Jacob Gunaseelan J(https://github.com/JacobGunaseelan)
- Bharath R(https://github.com/bharathramachandran04)
- Hemesh k(https://github.com/Hemeshk2004)
- Divit P(https://github.com/Divit9954)

Feel free to contribute by submitting issues and pull requests!

![ui1](https://github.com/user-attachments/assets/2e4b2047-1386-4360-9440-64384d8d26a0)

![WhatsApp Image 2025-03-01 at 08 59 32_499e3cad](https://github.com/user-attachments/assets/308ca1cb-7d10-4ff5-9a01-9d77210dd4fd)


