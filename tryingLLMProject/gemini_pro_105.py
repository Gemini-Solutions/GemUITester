import google.generativeai as genai
import secret_key
#from secret_key import GOOGLE_API_KEY


def unit_test_cases2(code):
    GOOGLE_API_KEY = secret_key.GOOGLE_API_KEY
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    print("I am in gemini Pro")

    if code:
        prompt2 = """ 
            Task: Please generate a comprehensive suite of unit tests for the codebase provided.
            
            Testing Framework: Check the best suited framework as per the language of developer codebase.
            
            Test Format: 
                Each test case is a comment followed by the respective code with the following format:
                ```
                [ TestCaseID | TestCaseDescription | Expected Output | Actual Output | Pass/Fail ]
                Code: Provide the unit test cases written in the best suited language for the codebase.
                
                ```
            

            Examples:

            ```
            // TC_01 | To check if the empty array is passed | result = -1 | result = -1 | Pass
            @test
            // Your code here
            ```
            
            Notes:

            * Make sure that test cases are created corresponding to all the cases be it Happy path, edge cases, exception handling, error handling, positive test cases or negative test cases, anything and everything should be covered.
            * If there is some prompt before the codebase then it should be given utmost importance.
            * If codebase have some faulty code that may provide error in future then it should be told to the user in the form of suggestion after the test cases. Also, this error should be handled while writing the test cases.

            The additional prompt and codebase is : 
            """
        test_cases = model.generate_content(prompt2 + code)
        print("I returned the response")
        return test_cases.text
