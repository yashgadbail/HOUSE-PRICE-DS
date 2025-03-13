import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df.drop(columns=['society'], inplace=True)  # Drop 'society' due to many missing values
    df['BHK'] = df['size'].str.extract('(\d+)').astype(float)  # Convert 'size' to numeric BHK
    
    def convert_sqft(sqft):
        if '-' in str(sqft):
            vals = list(map(float, sqft.split('-')))
            return np.mean(vals)
        try:
            return float(sqft)
        except:
            return None
    
    df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
    df.dropna(subset=['total_sqft', 'BHK', 'bath', 'balcony', 'price'], inplace=True)
    df = pd.get_dummies(df, columns=['area_type', 'site_location'], drop_first=True)
    df.drop(columns=['availability', 'size'], inplace=True)
    return df

# Load and preprocess data
data_path = "Pune house data.csv"
df = load_and_preprocess_data(data_path)

# Train model
X = df.drop(columns=['price'])
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("model/house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

def predict_price(total_sqft, bath, balcony, BHK, area_type, site_location):
    input_data = pd.DataFrame([[total_sqft, bath, balcony, BHK]], columns=['total_sqft', 'bath', 'balcony', 'BHK'])
    
    for col in X.columns[4:]:
        input_data[col] = 1 if col == f'area_type_{area_type}' or col == f'site_location_{site_location}' else 0
    
    return model.predict(input_data)[0]

# Example usage
print("Predicted Price:", predict_price(1200, 2, 1, 2, 'Super built-up  Area', 'Aundh'))
