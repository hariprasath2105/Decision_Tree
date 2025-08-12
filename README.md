# Customer Purchase Predictor (Decision Tree)

A Flask-based web application that predicts whether a website visitor will make a purchase based on their behavior. It uses a **Decision Tree Classifier** trained on features like time spent on the site, number of pages viewed, device type, and referral source.

---

## Overview

This project demonstrates how classification models can be used to predict purchase behavior in e-commerce. Users input session details and receive an instant prediction.

---

## Project Structure

```
customer-purchase-predictor/
│
├── model.py              
├── model.pkl
├── app.py             
├── customer_purchase_data.csv     
├── requirements.txt
├── templates/
│ └── index.html      
├── static/
│ └── style.css             
└── README.md              
```

---

## Dataset

**File**: `customer_purchase_data.csv`

**Columns**:
- `Time_on_Site` (float): Minutes spent on the site  
- `Page_Views` (int): Number of pages visited  
- `Device` (string): Type of device used (Mobile/Desktop)  
- `Referral` (string): Referral source (Google/Facebook/Direct)  
- `Purchased` (int): Target variable (1 = Purchased, 0 = Not Purchased)

📎 [Sample Dataset](./customer_purchase_data.csv)

---

## Features

- Predicts customer purchasing behavior from session info  
- Clean and colorful web interface using HTML + CSS  
- Pre-trained Decision Tree model  
- Encodes categorical features using LabelEncoder  

---

## Tech Stack

| Technology     | Use                  |
|----------------|----------------------|
| Python         | Core language        |
| Flask          | Web framework        |
| scikit-learn   | ML modeling          |
| pandas         | Data handling        |
| NumPy          | Numerical operations |
| HTML/CSS       | Frontend styling     |


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/hariprasath2105/Linear-Regression.git
cd customer-purchase-predictor
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train the Model
```bash
python model.py
```
### Step 4: Run the App Start the Flask server:
```bash
python app.py
```
---

## Usage

Go to http://127.0.0.1:5000/ in your browser.

Fill in session details.

Click "Predict" to see if the user will purchase.

---

## Screenshots

### Input UI
<img width="938" height="648" alt="image" src="https://github.com/user-attachments/assets/8b5754a4-7032-44a2-b726-4d48d329922d" />

### Output Prediction
<img width="938" height="648" alt="image" src="https://github.com/user-attachments/assets/530da7de-6f53-4aa8-9914-2db940a590da" />

---
