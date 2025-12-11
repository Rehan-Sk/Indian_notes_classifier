# 🇮🇳 Indian Currency Note Classifier Website

A deep-learning–based web application for classifying Indian currency notes using **fine-tuned InceptionV3**.  
This project includes **data processing**, **model training**, and a full **Flask web application** built using HTML, CSS, and Python.

---

## 📌 Project Overview

This project aims to automatically classify Indian currency notes into their correct denominations and versions.  
A note-image dataset was processed and trained using **InceptionV3**, achieving **~85% test accuracy**.

The final trained model is exported as **`currency_model.h5`** and is used inside a Flask web interface for real-time prediction.

---

## 🧠 Features

- ✔️ Trained using **InceptionV3**
- ✔️ ~85% classification accuracy
- ✔️ Predicts **10 classes** of Indian currency notes
- ✔️ Clean and simple **Flask web UI**
- ✔️ Supports **image upload** and real-time predictions
- ✔️ Modular structure for easy updates

---

## 🏷️ Classes

The classifier predicts the following note categories:

- INDIA100NEW  
- INDIA100OLD  
- INDIA10NEW  
- INDIA10OLD  
- INDIA20  
- INDIA200  
- INDIA2000  
- INDIA500  
- INDIA50NEW  
- INDIA50OLD  


---

## 🧰 Technology Stack

- **Python 3.x**
- **TensorFlow / Keras (InceptionV3)**
- **NumPy**
- **Flask**
- **HTML / CSS (Frontend)**


## 🚀 How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone <your-repo-link>
cd indian-currency-classifier
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```
### 3️⃣Download & place the model
```bash
Link-https://drive.google.com/file/d/1g-5Q7n9pts05w-XAUM7UjSD8DydWQry5/view?usp=sharing
```
Download the currency_model.h5 file from your Google Drive link and place it in:

model/currency_model.h5

4️⃣ Run the Flask app
```bash
python app.py

```
Then open your browser at:
```bash
http://127.0.0.1:5000/
```
