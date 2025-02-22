import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

# Collect user input
date_time = st.date_input("Pickup Date and Time", datetime.datetime.now())
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

# Build the API request
params = {
    "pickup_datetime": date_time.strftime("%Y-%m-%d %H:%M:%S"),  # Corrected key name
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,  # Corrected key name
    "passenger_count": passenger_count,
}

# Call the API
response = requests.get(url, params=params)

# Initialize prediction variable
prediction = None

# Retrieve the prediction from the JSON response
if response.status_code == 200:
    prediction = response.json().get('fare')
    st.success(f"The estimated fare is: ${prediction:.2f}")
else:
    st.error("Error: Unable to retrieve the prediction. Please check the parameters and try again.")

# Display the prediction if available
if prediction is not None:
    st.write(f"Your ride will only cost ${prediction:.2f}")
