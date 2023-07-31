import streamlit as st
import pandas as pd

# Function to convert CSV to Excel
def csv_to_excel(file_path, output_path):
    df = pd.read_csv(file_path)
    df.to_excel(output_path, index=False)

# Function to convert Excel to CSV
def excel_to_csv(file_path, output_path):
    df = pd.read_excel(file_path)
    df.to_csv(output_path, index=False)

# Function to convert JSON to CSV
def json_to_csv(file_path, output_path):
    df = pd.read_json(file_path)
    df.to_csv(output_path, index=False)

# Function to convert CSV to JSON
def csv_to_json(file_path, output_path):
    df = pd.read_csv(file_path)
    df.to_json(output_path, orient='records')

st.title("File Format Converter")

file = st.file_uploader("Upload your file:", type=["csv", "xlsx", "json"])

if file is not None:
    file_format = st.selectbox("Select the file format:", ["CSV", "Excel", "JSON"])

    if file_format == "CSV":
        st.write("You can convert your file to:")
        if st.button("Convert to Excel"):
            csv_to_excel(file, "output.xlsx")
            st.success("File successfully converted to Excel! You can download it [here](output.xlsx).")

        if st.button("Convert to JSON"):
            csv_to_json(file, "output.json")
            st.success("File successfully converted to JSON! You can download it [here](output.json).")

    elif file_format == "Excel":
        st.write("You can convert your file to:")
        if st.button("Convert to CSV"):
            excel_to_csv(file, "output.csv")
            st.success("File successfully converted to CSV! You can download it [here](output.csv).")

        if st.button("Convert to JSON"):
            excel_to_csv(file, "output.json")
            st.success("File successfully converted to JSON! You can download it [here](output.json).")

    elif file_format == "JSON":
        st.write("You can convert your file to:")
        if st.button("Convert to CSV"):
            json_to_csv(file, "output.csv")
            st.success("File successfully converted to CSV! You can download it [here](output.csv).")

        if st.button("Convert to Excel"):
            json_to_csv(file, "output.xlsx")
            st.success("File successfully converted to Excel! You can download it [here](output.xlsx).")
