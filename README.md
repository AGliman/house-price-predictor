# house-price-predictor
# 🏡 Real Estate Price Predictor: Machine Learning End-to-End Project
# 📌 Project Overview
The objective of this project is to predict house prices based on various property features
. By formulating this as a supervised regression problem
, this tool allows real estate agents, landlords, and homebuyers to input property specifications and receive an instant, data-driven fair market valuation.
# 📊 The Dataset
The model was trained on a historical housing dataset containing 545 property entries and 13 columns (features)
.
Target Variable: price
.
Numerical Features: area, bedrooms, bathrooms, stories, parking
.
Categorical Features: mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus
.
# 🛠️ Data Preprocessing & Pipeline
To ensure the machine learning models received clean and standardized data, an automated preprocessing pipeline was built using scikit-learn's ColumnTransformer
:
Numerical Data: Missing values were handled using median imputation (SimpleImputer), and the data was scaled using StandardScaler
.
Categorical Data: Text categories were standardized (lowercase and stripped of spaces)
. Missing values were filled with the most frequent entry, and the text was converted into numbers using OneHotEncoder
.
# 🧠 Machine Learning Models
To find the best predictive engine, the data was split into an 80% training set and a 20% testing set
. Several algorithms were evaluated against a simple Baseline Model
:
Linear Regression
Ridge Regression (Regularized)
Lasso Regression (Regularized)
Random Forest Regressor (Nonlinear Ensemble)
Gradient Boosting Regressor (Nonlinear Ensemble)
The models were evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R 
2
 ) metrics, and were validated using 5-fold cross-validation to ensure stability
.
# 🏆 Final Model & Insights
The Random Forest Regressor was selected as the strongest candidate and was fine-tuned using RandomizedSearchCV to optimize its hyperparameters (such as n_estimators set to 500)
.
What drives house prices? Using permutation importance to interpret the model, the top 3 features that drive a property's predicted price are
:
Total Area (By far the most important factor)
Number of Bathrooms
Air Conditioning
# 💻 Web Application (Streamlit)
The final tuned pipeline was saved using joblib and deployed as an interactive web application using Streamlit and FastAPI/Python. Users can adjust sliders for numerical features (like area and bedrooms) and use dropdowns for categorical features (like furnishing status) to get an instant price prediction on a highly intuitive interface.
