import pandas as pd
import numpy as np
import time
import os


def data_cleaning_master(file_path, file_name):
    print("\n🔰 Welcome to the **Data Cleaning Master** Tool! 🔰\n")
    time.sleep(2)
    
    print("🕵️ Starting the analysis...")
    time.sleep(1)

    if not os.path.exists(file_path):
        print("\n❌ Invalid file path! Please double-check and try again.\n")
        return
    else:
        time.sleep(2)
        print(f"✅ File path validated: {file_path}\n")
        time.sleep(1)

        if file_path.endswith('.csv'):
            print("📂 Dataset identified as a CSV file. Loading now...\n")
            time.sleep(2)
            df = pd.read_csv(file_path, encoding_errors='ignore')
        elif file_path.endswith('.xlsx'):
            print("📂 Dataset identified as an Excel file. Loading now...\n")
            time.sleep(2)
            df = pd.read_excel(file_path)
        else:
            print("\n❌ Unknown file type! Supported formats are .csv and .xlsx only.\n")
            return

    print(f"✅ Dataset loaded successfully!\n")
    time.sleep(2)

    # Showing number of records
    print(f"🔍 Initial analysis shows:\n- Total Rows: {df.shape[0]}\n- Total Columns: {df.shape[1]}\n")
    time.sleep(2)

    # Checking duplicates
    duplicates = df.duplicated()
    total_duplicates = duplicates.sum()

    print(f"📊 Duplicate Record Check:\n- Total Duplicates: {total_duplicates}\n")
    time.sleep(2)

    # Saving the duplicates
    if total_duplicates > 0:
        duplicate_records_df = df[duplicates]
        duplicate_file = f"{file_name}_duplicates.csv"
        duplicate_records_df.to_csv(duplicate_file, index=False)
        print(f"⚠️ Duplicate records saved to: {duplicate_file}\n")
        time.sleep(2)

    df.drop_duplicates(inplace=True)
    print("🧹 Duplicate records removed from the dataset.\n")
    time.sleep(1)

    # Find missing values
    total_missing_value = df.isnull().sum().sum()
    print(f"🔍 Missing Values Check:\n- Total Missing Values: {total_missing_value}\n")

    if total_missing_value > 0:
        print("✨ Dealing with missing values column by column...\n")
    time.sleep(2)

    # Dealing with missing values
    columns = df.columns
    for col in columns:
        if df[col].dtype in (float, int):
            df[col] = df[col].fillna(df[col].mean())
            print(f"✅ Filled missing values in column '{col}' with the column's mean.\n")
        else:
            df.dropna(subset=[col], inplace=True)
            print(f"✅ Dropped rows with missing values in column '{col}'.\n")
        time.sleep(1)

    # Data is cleaned
    print("\n🎉 **Congratulations! Your dataset is now clean!** 🎉\n")
    print(f"- Cleaned Dataset Rows: {df.shape[0]}\n- Cleaned Dataset Columns: {df.shape[1]}\n")
    time.sleep(2)

    # Saving the clean dataset
    clean_file = f"{file_name}_clean_data.csv"
    df.to_csv(clean_file, index=False)
    print(f"💾 Cleaned dataset saved successfully to: {clean_file}\n")
    time.sleep(1)
    print("Thank you for using **Data Cleaning Master**. Have a great day! 🌟\n")


if __name__ == "__main__":
    print("🌟 Welcome to the **Data Cleaning Master** Tool! 🌟\n")

    # Ask path and file name
    file_path = input("📂 Please enter the dataset path: ")
    file_name = input("📝 Please enter a name for the output files: ")

    # Calling the function
    data_cleaning_master(file_path, file_name)
