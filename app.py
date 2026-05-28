import streamlit as st
import pandas as pd
import joblib

# 1. Load the trained model
# Make sure 'house_price_model.joblib' is in the same folder!
model = joblib.load('house_price_model.joblib')

# 2. Add a title and description to your web app
st.title("🏡 Real Estate Price Predictor")
st.write("Enter the details of a house below to get an instant price estimation!")

# 3. Create input widgets for the user
# We divide the layout into two columns to make it look nice
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Details")
    area = st.number_input("Total Area (sq ft)", min_value=1000, max_value=20000, value=5000)
    bedrooms = st.slider("Bedrooms", 1, 6, 3)
    bathrooms = st.slider("Bathrooms", 1, 4, 1)
    stories = st.slider("Stories", 1, 4, 2)
    parking = st.slider("Parking Spaces", 0, 3, 1)

with col2:
    st.subheader("Special Features")
    mainroad = st.selectbox("Main Road Access?", ["yes", "no"])
    guestroom = st.selectbox("Guestroom?", ["yes", "no"])
    basement = st.selectbox("Basement?", ["yes", "no"])
    hotwaterheating = st.selectbox("Hot Water Heating?", ["yes", "no"])
    airconditioning = st.selectbox("Air Conditioning?", ["yes", "no"])
    prefarea = st.selectbox("Preferred Area?", ["yes", "no"])
    furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# 4. Create a "Predict" button
if st.button("Predict House Price"):
    # Group the user's inputs into a dictionary
    user_data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }
    
    # Convert dictionary to a Pandas DataFrame (just like your notebook's data)
    input_df = pd.DataFrame([user_data])
    
    # Make the prediction using your pipeline
    prediction = float(model.predict(input_df)[0])

    # Display the result beautifully on the screen!
    st.success(f"### Estimated Price: ${prediction:,.2f}")
    st.balloons() # Adds a fun animation when a prediction is made!