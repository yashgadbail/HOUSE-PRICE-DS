import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
import os

# Load model from model directory
model_path = os.path.join("model", "house_price_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__, template_folder="templates")
locations = ["Baner", "Hinjewadi", "Kothrud", "Wakad"]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        total_sqft = float(request.form['total_sqft'])
        bath = int(request.form['bath'])
        balcony = int(request.form['balcony'])
        BHK = int(request.form['BHK'])
        area_type = request.form['area_type']
        site_location = request.form['site_location']
        
        input_data = pd.DataFrame([[total_sqft, bath, balcony, BHK]], columns=['total_sqft', 'bath', 'balcony', 'BHK'])
        
        # Load feature names from the trained model
        with open("model/feature_columns.pkl", "rb") as f:
            feature_columns = pickle.load(f)
        
        for col in feature_columns:
            input_data[col] = 1 if col == f'area_type_{area_type}' or col == f'site_location_{site_location}' else 0
        
        price = model.predict(input_data)[0]
        return render_template('index.html', prediction_text=f'Predicted House Price: ₹{price:.2f} Lakhs')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)