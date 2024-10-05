import pandas as pd

# Function to load the sustainability dataset
def load_sustainability_data():
    return pd.read_csv('data/processed/sustainability_processed.csv')

# Function to load the Christmas dataset
def load_christmas_data():
    return pd.read_csv('data/processed/christmas_processed.csv')
