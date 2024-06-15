import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI
load_dotenv()

google_API = os.getenv("OPENAI_API_KEY")

#Function for pandasai for making query

def chat_with_csv(df,prompt):
    llm = OpenAI()
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df,prompt = prompt)
    print(result)
    return result
st.set_page_config(layout='wide')
st.title("Chat with CSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file",type=['csv'])

if input_csv is not None:
    
    col1,col2 =st.columns([1,1])
    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data)
        
    with col2:
        st.info("Chat with your CSV")
        input_text = st.text_area("Enter yor query")
        
        if input_text is not None:
            if st.button("Start your Chat"):
                st.info("Make an asking,"+input_text)
                result = chat_with_csv(data,input_text)
                st.success(result)