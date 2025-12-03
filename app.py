import streamlit as st
import numpy as np
import pickle
from datetime import datetime, date, time

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("flight_price.pkl", "rb"))

# -----------------------------
# Streamlit Page Settings
# -----------------------------
st.set_page_config(page_title="Flight Price Prediction",
                   layout="centered",
                   page_icon="✈️")

st.markdown("""
    <h2 style='text-align:center; color:#4CAF50;'>
        ✈️ Flight Price Prediction System
    </h2>
    <p style='text-align:center; font-size:17px;'>
        Enter flight details below to estimate the ticket price
    </p>
    <hr>
""", unsafe_allow_html=True)


# -----------------------------
# Input Fields
# -----------------------------
st.subheader("📝 Enter Flight Details")

airline = st.selectbox("Airline", [
    'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
    'Jet Airways Business', 'Multiple carriers',
    'Multiple carriers Premium economy', 'SpiceJet',
    'Trujet', 'Vistara', 'Vistara Premium economy'
])

source = st.selectbox("Source", ['Kolkata'])   # only one encoded column
destination = st.selectbox("Destination", [
    'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'
])

total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])
duration = st.number_input("Total Duration (Minutes)", min_value=1)

journey_date = st.date_input("Date of Journey", date.today())
dep_time = st.time_input("Departure Time", time(10, 0))
arr_time = st.time_input("Arrival Time", time(12, 0))

# Extract date/time features
day = journey_date.day
month = journey_date.month
year = journey_date.year
dep_hour = dep_time.hour
dep_min = dep_time.minute
arrival_hour = arr_time.hour


# -------------------------------------------------
# Create Feature Vector (25 Features)
# -------------------------------------------------

# 1. Numerical features
features = [
    total_stops,
    duration,
    day,
    month,
    year,
    arrival_hour,
    dep_hour,
    dep_min,
]

# 2. Airline OneHotEncoding (10 columns)
airlines_map = [
    'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
    'Jet Airways Business', 'Multiple carriers',
    'Multiple carriers Premium economy', 'SpiceJet',
    'Trujet', 'Vistara', 'Vistara Premium economy'
]

for a in airlines_map:
    features.append(1 if airline == a else 0)

# 3. Source (only Kolkata column exists)
features.append(1 if source == "Kolkata" else 0)

# 4. Destination OneHotEncoding (5 columns)
dest_map = ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi']

for d in dest_map:
    features.append(1 if destination == d else 0)


# -----------------------------
# PREDICT BUTTON
# -----------------------------
if st.button("🔮 Predict Flight Price"):
    try:
        final_features = np.array([features])
        prediction = float(model.predict(final_features)[0])

        st.success(f"💰 Estimated Flight Price: **₹ {prediction:.2f}**")

    except Exception as e:
        st.error(f"Error: {e}")


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
    <hr>
    <p style='text-align:center; font-size:14px; color:grey;'>
        © 2025 | Flight Price Prediction System | Machine Learning Project
    </p>
""", unsafe_allow_html=True)

st.markdown("""
    <hr>
    <p style='text-align:center; font-size:15px; color:#555;'>
        🚀 Developed with ❤️ by <b>Vikash Singh</b><br>
        © 2025 | Flight Price Prediction System
    </p>
""", unsafe_allow_html=True)