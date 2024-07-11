from setuptools import find_packages, setup

setup(
    
    name ='mcq generator',
    version="0.1",
    author="priyansh",
    install_requires=["openai","langchain","streamlit","python-dotenv","pypdf2"],
    packages=find_packages()
)