import streamlit as st
import requests

# Title
st.title("Send Angle Value (0 to 180) to Database")

# Slider for angle between 0 and 180
angle = st.slider("Select an angle", min_value=0, max_value=180, value=90)

# Button to send data
if st.button("Send Angle"):
    # Prepare data
    payload = {"angle": angle}

    try:
        # POST request to your backend
        response = requests.post("http://localhost:8000/add-angle", json=payload)

        if response.status_code == 200:
            st.success("Angle sent successfully!")
        else:
            st.error(f"Failed to send angle. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
