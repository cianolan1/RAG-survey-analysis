import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the dataset
    df = pd.read_excel(file_path)

    # Example preprocessing: Remove rows with missing values
    df = df.dropna()

    # Additional preprocessing logic can go here (e.g., scaling, encoding)
    return df

# Example usage
if __name__ == "__main__":
    raw_data_path = '../raw/sustainability_survey.xlsx'
    processed_data = load_and_preprocess_data(raw_data_path)

    # Save the preprocessed data to the processed directory
    processed_data.to_csv('../processed/sustainability_survey_processed.csv', index=False)
