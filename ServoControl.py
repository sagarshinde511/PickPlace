import streamlit as st
import requests

# Title
st.title("Send Angle (0 to 180) to API")

# Slider for selecting angle
angle = st.slider("Select an angle (0 to 180)", min_value=0, max_value=180, value=90)

# Button to send
if st.button("Send to API"):
    # Construct the URL with the angle
    url = f"https://aeprojecthub.in/flagChange.php?f5=1&f1={angle}"

    try:
        # Send GET request
        response = requests.get(url)

        if response.status_code == 200:
            st.success(f"Sent angle {angle} successfully!")
            st.write("Response:", response.text)
        else:
            st.error(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
