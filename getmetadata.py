#!/usr/local/bin/python3
import pandas as pd
import argparse
import os

def get_file_metadata(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    # Determine the file type based on the file extension
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension in ['.xls', '.xlsx']:
        # Load the Excel file
        excel_file = pd.ExcelFile(file_path)
        
        # Get sheet names
        sheet_names = excel_file.sheet_names
        print(f"Sheet names: {sheet_names}")
        
        # Loop through each sheet and get metadata
        for sheet in sheet_names:
            print(f"\nMetadata for sheet: {sheet}")
            df = excel_file.parse(sheet)
            display_metadata(df)
    
    elif file_extension == '.csv':
        # Load the CSV file
        df = pd.read_csv(file_path)
        print("\nMetadata for CSV file:")
        display_metadata(df)
    
    elif file_extension == '.json':
        # Load the JSON file
        df = pd.read_json(file_path)
        print("\nMetadata for JSON file:")
        display_metadata(df)
    
    else:
        print(f"Unsupported file type: {file_extension}")
    
def display_metadata(df):
    # Get basic information
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    
    # Get data types of each column
    print("Column Data Types:")
    print(df.dtypes)
    
    # Get column names
    print("Column Names:")
    print(df.columns.tolist())
    
    # Display if there are missing values
    print(f"Missing values in each column:\n{df.isnull().sum()}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Get metadata from a file (Excel, CSV, or JSON)")
    parser.add_argument('file_path', type=str, help="Path to the file (Excel, CSV, JSON)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the metadata extraction function
    get_file_metadata(args.file_path)

if __name__ == "__main__":
    main()
