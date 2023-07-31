import streamlit as st
import pandas as pd
from io import BytesIO

# Function to convert CSV to Excel
def csv_to_excel(file_path):
    df = pd.read_csv(file_path)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

# Function to convert Excel to CSV
def excel_to_csv(file_path):
    df = pd.read_excel(file_path)
    output = BytesIO()
    df.to_csv(output, index=False)
    return output.getvalue()

# Function to convert JSON to CSV
def json_to_csv(file_path):
    df = pd.read_json(file_path)
    output = BytesIO()
    df.to_csv(output, index=False)
    return output.getvalue()

st.title("File Format Converter")

file = st.file_uploader("Upload your file:", type=["csv", "xlsx", "json"])

if file is not None:
    file_format = st.selectbox("Select the file format:", ["CSV", "Excel", "JSON"])

    if file_format == "CSV":
        st.write("You can convert your file to:")
        if st.button("Convert to Excel"):
            converted_file = csv_to_excel(file)
            st.download_button("Download Converted File", data=converted_file, file_name="output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        if st.button("Convert to JSON"):
            converted_file = json_to_csv(file)
            st.download_button("Download Converted File", data=converted_file, file_name="output.json", mime="application/json")

    elif file_format == "Excel":
        st.write("You can convert your file to:")
        if st.button("Convert to CSV"):
            converted_file = excel_to_csv(file)
            st.download_button("Download Converted File", data=converted_file, file_name="output.csv", mime="text/csv")

        if st.button("Convert to JSON"):
            converted_file = excel_to_csv(file)
            st.download_button("Download Converted File", data=converted_file, file_name="output.json", mime="application/json")

    elif file_format == "JSON":
        st.write("You can convert your file to:")
        if st.button("Convert to CSV"):
            converted_file = json_to_csv(file)
            st.download_button("Download Converted File", data=converted_file, file_name="output.csv", mime="text/csv")

        if st.button("Convert to Excel"):
            converted_file = json_to_csv(file)
            st.download_button("Download Converted File", data=converted_file, file_name="output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
