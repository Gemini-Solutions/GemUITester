import streamlit as st
import google.generativeai as genai

import secret_key
from secret_key import GOOGLE_API_KEY

# import textwrap
# from IPython.display import display
# from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
def unit_test_cases(code):
    GOOGLE_API_KEY = secret_key.GOOGLE_API_KEY

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    #st.header('Gemini Test Case Generator')

    #code = st.text_input('Your Code here')
    if code:
        # response = model.generate_content()
        test_cases = model.generate_content(
            ''' I have a piece of code written in Java. The code is for validating user's sign in on website.
            Give detailed description of the code and Please generate a comprehensive suite of unit tests for this code. The unit tests should cover:
            Happy Path: Test cases that provide valid input and verify the expected output.
            Edge Cases: Test cases that explore scenarios with invalid input, boundary conditions, or unexpected data.
            Error Handling: Test cases that verify the code handles errors gracefully and throws appropriate exceptions when necessary.
            
            Generate code for the test cases. The code is provided below: 
            
            ''' + code)

        # st.write(response.prompt_feedback)
        # st.write(response.text)
        # st.write(test_cases.prompt_feedback)
        # st.write(test_cases.text)

        return test_cases.text