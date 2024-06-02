from setuptools import find_packages,setup

setup(
    name ="mcqgenerator",
    version = '0.0.1',
    install_requires = ['langchain','langchain_google_genai','streamlit','langchain_community','python-dotenv','PyPDF2'],
    packages =find_packages()
)