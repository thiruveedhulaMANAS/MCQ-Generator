import os
import PyPDF2
import json
import traceback
import pandas as pd

def file_read(file):
    if(file.name.endswith(".pdf")):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading the pdf file")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception("unsupported file format only pdf and text file supported.")
    
# def get_table_data(quiz):
#     try:
#         # quiz_dict = json.loads(quiz_str)
#         # return quiz_dict
#         quiz_dict = json.loads(quiz)
#         quiz_table_data = []

#         for key,val in quiz_dict.items():
#             mcq = val["mcq"]
#             options=" || ".join([
#                 f"{option}-> {option_value}" for option,option_value in val["options"].items()
#             ])
#             correct_val = val["correct"]
#             quiz_table_data.append({"MCQ":mcq,"Choices":options,"Correct": correct_val})
#         print(quiz_table_data)
#         return quiz_table_data
#     except json.JSONDecodeError as e:
#         print("Invalid JSON syntax",e)

def get_table_data(response):
    try:
        data = json.loads(response)
        quiz_questions = []
        for question_id, question_info in data[0].items():
            print(f"Question ID: {question_id}")
            print(f"MCQ: {question_info['mcq']}")
            print("Options:")
            for option_key, option_value in question_info['options'].items():
                print(f"  {option_key}: {option_value}")
            print(f"Correct answer: {question_info['correct']}")
            print()
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax",e)
    