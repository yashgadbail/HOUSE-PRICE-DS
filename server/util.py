import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
    except ValueError:
        loc_index = -1  # If location is not found, set it to -1

    # Create an array of zeros with the same size as model features
    x = np.zeros(len(__data_columns))

    # Assign input values
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # If location exists in the feature columns, set it to 1
    if loc_index >= 0:
        x[loc_index] = 1

    # Reshape to match model expectations
    x = x.reshape(1, -1)

    # Debugging: Print shape of input
    print(f"Input array shape: {x.shape}, Expected features: {len(__data_columns)}")

    return round(__model.predict(x)[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __locations
    global __model

    with open("./server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open("./server/artifacts/pune_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print(f"Loaded model with {len(__data_columns)} features")
    print("Loading saved artifacts... done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Aundh', 1000, 2, 2))
    print(get_estimated_price('Baner', 1000, 2, 2))
