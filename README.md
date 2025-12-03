# Flight Price Prediction

A machine learning project to predict airline ticket prices using historical flight data.  
The model analyzes key features such as Airline, Journey Date, Source, Destination, Route, Duration, and Total Stops to estimate the final fare.

---

## Overview
- Performed full data preprocessing: cleaning, feature extraction (day, month, hour, duration minutes), and categorical encoding.
- Conducted EDA to understand pricing trends across airlines, routes, and stop counts.
- Built multiple ML models including Linear Regression, KNN, Decision Tree, Random Forest, ANN, and XGBoost.
- **XGBoost delivered the best performance with an R² score of 0.8629.**

---

## Deployment
- Integrated the final model into a **Streamlit web application**.
- Users can input journey details and receive instant flight price predictions.

---

## Technologies Used
- Python, Pandas, NumPy  
- Scikit-learn, XGBoost, TensorFlow/Keras  
- Matplotlib, Seaborn  
- Streamlit  

---

## 📌 Outcome
A reliable prediction system that helps estimate flight prices accurately, supporting travelers, booking platforms, and airline pricing analysis.

