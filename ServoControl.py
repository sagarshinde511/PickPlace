import streamlit as st
import requests

# Function to send the request
def send_angle(angle):
    url = f"https://aeprojecthub.in/flagChange.php?f5=1&f1={angle}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.success(f"Sent angle {angle} successfully!")
            st.write("Response:", response.text)
        else:
            st.error(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")

# Set default session state
if "last_angle" not in st.session_state:
    st.session_state.last_angle = 90  # default

# Slider
angle = st.slider("Select an angle (0–180)", 0, 180, st.session_state.last_angle, key="angle_slider")

# If slider value changed
if angle != st.session_state.last_angle:
    st.session_state.last_angle = angle
    send_angle(angle)
