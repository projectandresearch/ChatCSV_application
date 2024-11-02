import pandas as pd
import pandasai
from pandasai import SmartDatalake
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json


st.set_page_config(layout='wide')
# load_dotenv()

st.title("chatCSV powered by Gemini LLM")

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key="AIzaSyAGPmRJFjBSUvDAJPzZ1uAFmU9X8i0TfBs")


def chat_with_csv(json_data, prompt):

    formatted_prompt = f"The data: {json_data}\n\nQuery: {prompt}"
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(formatted_prompt)
    output = response.text
    return output




input_csv = st.file_uploader("Upload your CSV file", type=['csv'])
if input_csv:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV uploaded successfully...")
        data = pd.read_csv(input_csv)
        st.dataframe(data)
               
        all_records = data.to_json(orient='records')
        json_data = json.loads(all_records)  


    with col2:
        st.info("Chat with your CSV")
        input_text = st.text_input("Enter your query: ")
        if input_text:
            if st.button("Chat with CSV"):
                st.info("Your query: " + input_text)
                                
                result = chat_with_csv(json_data=json_data, prompt=input_text)
                
                st.success(result)
