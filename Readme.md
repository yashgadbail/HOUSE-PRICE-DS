# Home Price Prediction API

A Flask-based web application for predicting home prices based on location, square footage, number of bedrooms, and bathrooms.

## Overview

This project provides a web interface and API for real estate price predictions. The application uses a machine learning model (managed by the `util` module) to estimate property prices based on various features.

## Features

- Web interface for home price prediction
- REST API endpoints for programmatic access
- Location-based price estimation
- Considers square footage, bedrooms, and bathrooms

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/bhushanzade02/HOUSE-PRICE-DS.git
   cd HOUSE-PRICE-DS
   ```
2. Create virtual environment
   ```
   python -m venv .venv
   ./.venv/Scripts/activate
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the server:
   ```
   python server/server.py
   ```

## API Endpoints

### GET /
- Returns the home page

### GET /get_location_names
- Returns a list of available locations
- Response format: `{"locations": ["location1", "location2", ...]}`

### POST /predict_home_price
- Predicts the price of a home based on input parameters
- Request body format (JSON):
  ```json
  {
    "total_sqft": 1000,
    "location": "Example Location",
    "bhk": 2,
    "bath": 2
  }
  ```
- Response format: `{"estimated_price": 1500000}`

## Usage

1. Access the web interface by navigating to `http://localhost:5000` in your browser
2. Select a location, enter the square footage, number of bedrooms, and bathrooms
3. Submit the form to get a price estimate

## Development

- Server runs in debug mode by default
- CORS headers are enabled for all API endpoints
- Error handling is implemented for the prediction endpoint

## Starting the Application

```
python server/server.py
```

The server will start with the message "Starting Python Flask Server For Home Price Prediction..." and will be accessible at `http://localhost:5000`.
