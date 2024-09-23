#!/usr/local/bin/python3
import pandas as pd
import argparse
import os

def get_excel_metadata(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    # Load the Excel file
    excel_file = pd.ExcelFile(file_path)
    
    # Get sheet names
    sheet_names = excel_file.sheet_names
    print(f"Sheet names: {sheet_names}")
    
    # Loop through each sheet and get metadata
    for sheet in sheet_names:
        print(f"\nMetadata for sheet: {sheet}")
        
        # Read the sheet into a DataFrame
        df = excel_file.parse(sheet)
        
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
    parser = argparse.ArgumentParser(description="Get metadata from an Excel file")
    parser.add_argument('file_path', type=str, help="Path to the Excel file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the metadata extraction function
    get_excel_metadata(args.file_path)

if __name__ == "__main__":
    main()


