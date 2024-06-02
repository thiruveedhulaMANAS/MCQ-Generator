import os
import json
import pandas as pd
import traceback
from langchain_google_genai import GoogleGenerativeAI
from src.mcq.MCQGenerator import generate_evaluate_chain
from src.mcq.utils import file_read,get_table_data
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

with open(r"C:\Users\manas\OneDrive\Desktop\mcqgenerator\Response.json","r") as f:
    Response = json.load(f)
    # Response = f.read()
    # print(Response_json)
st.title("Mcq generator Application using langchain")

with st.form("User Input"):
    uploaded_file = st.file_uploader("Upload a text file")

    mcq_count = st.number_input("No. of Mcqs",min_value=3,max_value=100)
    subject = st.text_input("Insert Subject",max_chars=20)
    tone = st.text_input("Complexity level of Questions",max_chars=20,placeholder="simple")
    button = st.form_submit_button("Create")
    if button  and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = file_read(uploaded_file)
                response = generate_evaluate_chain({
                        "text":text,
                        "number":mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "response_text":Response
                    })
                st.write(response.get('quiz'))
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")
            
            # else:
                
            #     quiz = response.get("quiz" ,None)
            #     if quiz is not None:
            #         data = get_table_data(quiz)
            #         st.write(data)
                # else:
                    # st.write(response)

            
