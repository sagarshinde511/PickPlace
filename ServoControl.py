import streamlit as st
import requests

# Initialize session state for sliders and previous values
for i in range(1, 5):
    slider_key = f"servo_{i}"
    prev_key = f"prev_servo_{i}"
    if slider_key not in st.session_state:
        st.session_state[slider_key] = 90  # Default angle
    if prev_key not in st.session_state:
        st.session_state[prev_key] = 90

# Convert 0–180 angle to 0–99
def convert_angle(angle):
    return round(angle * (99 / 180))

# Function to send only the changed servo
def send_single_servo(servo_num, angle):
    scaled_value = convert_angle(angle)
    if(servo_num ==3):
        servo_num = 0
    combined_value = f"{servo_num}{scaled_value:02d}"  # Ensure it's 2 digits with leading 0
    url = f"https://aeprojecthub.in/flagChange.php?f5=1&f1={combined_value}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.success(f"Sent Servo {servo_num}: Angle {angle} → Scaled {scaled_value}")
            st.write("URL:", url)
            st.write("Response:", response.text)
        else:
            st.error(f"Failed to send Servo {servo_num}. Status: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")

# Draw sliders and check for changes
for i in range(1, 5):
    slider_key = f"servo_{i}"
    prev_key = f"prev_servo_{i}"

    new_value = st.slider(f"Servo {i}", 0, 180, st.session_state[slider_key], key=slider_key)

    # Check if value changed
    if new_value != st.session_state[prev_key]:
        st.session_state[prev_key] = new_value
        send_single_servo(i, new_value)
