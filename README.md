
# 🏘️ Real Estate Price Prediction Web App - Gurgaon
An interactive Streamlit web application to analyze real estate trends in Gurgaon and predict residential property prices using machine learning.

## 🚀 Features
📄 Home

Project overview, objectives, and structure explanation.

Highlights challenges in real estate price estimation across Gurgaon sectors.

## 📈 Analysis Dashboard

Interactive visualizations powered by Plotly:

🗺️ Geo Map – Average price per sqft by Gurgaon sectors

📊 BHK Pie Chart – Property distribution by number of bedrooms

🌐 Word Cloud – Common property listing terms

📉 Boxplot & Distplot – Price variations across property types

🟡 Scatter Plot – Price per sqft vs Built-up area

## 💰 Price Predictor

User inputs: sector, BHK, area, luxury tag, etc.

Trained ML model instantly predicts the estimated house price.

Clean and intuitive UI using Streamlit widgets

## 🧠 Model Details
### 🔍 Price Prediction Model

#### ->Model: Linear Regression / Random Forest (via Scikit-learn)

#### -> Input Features Used: Sector , Number of Bedrooms (BHK), Built-up Area, Luxury Status 

#### -> Output: Predicted Property Price (₹)

#### -> Video Demo  https://youtu.be/sKq1i68I7CI


## 💻 How to Run the App

Clone the Repository

```bash
git clone https://github.com/Globbleofficial/Real-Estate-Price-Prediction-Web-App-Gurgaon.git
cd Real-Estate-Price-Prediction-Web-App-Gurgaon

```
Launch the App

```bash
streamlit run Home.py

```

## 🧭 How to Use

->Navigate between pages using the sidebar: Home, Analysis App, and Price Predictor

->Explore Gurgaon’s real estate trends using interactive charts

->Use the predictor to estimate property prices by entering relevant details

->Get real-time price output with visual feedback

## 📦 Requirements

Install required Python libraries via:

```bash 
pip install -r requirements.txt
```
