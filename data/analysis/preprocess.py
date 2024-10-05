import pandas as pd

def clean_column_names(df):
    """
    Cleans up the column names, combining relevant 'Unnamed' columns
    and ensuring questions are represented clearly.
    """
    # Use a raw string to handle the regex properly
    df.columns = df.columns.str.replace(r'Unnamed: \d+', 'Unknown')
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
    print("Cleaned Column Names:", df.columns)  # Print column names for debugging
    return df

def load_and_preprocess_data(file_path, skip_rows=2):
    """
    Loads the dataset, cleans column names, removes irrelevant rows, and
    restructures the data for analysis.
    """
    # Load the dataset
    df = pd.read_excel(file_path, skiprows=skip_rows)
    
    # Clean the column names
    df = clean_column_names(df)
    
    # Drop rows that are completely empty
    df = df.dropna(how='all')
    
    # Check if 'Total Sample' or similar column exists
    possible_cols = [col for col in df.columns if 'Total' in col]
    if possible_cols:
        total_sample_col = possible_cols[0]  # Get the first matching column
        # Remove rows with summary information
        df = df[~df[total_sample_col].str.contains('Total', na=False)]
    else:
        print("Warning: 'Total Sample' column not found")
    
    # Print the first few rows for inspection
    print("Preprocessed Data:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    # Load and preprocess the sustainability dataset
    sustainability_data = load_and_preprocess_data('data/raw/Dataset 1 (Sustainability Research Results).xlsx')
    sustainability_data.to_csv('data/processed/sustainability_processed.csv', index=False)

    # Load and preprocess the Christmas dataset
    christmas_data = load_and_preprocess_data('data/raw/Dataset 2 (Christmas Research Results).xlsx')
    christmas_data.to_csv('data/processed/christmas_processed.csv', index=False)


