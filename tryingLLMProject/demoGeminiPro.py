import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# this is model with the name llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# this promptTemplate
tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}.")

# this is chain
chain = tweet_prompt.pipe(llm)

if __name__ == "__main__":
    topic = "how ai is really cool"
    resp = chain.invoke({"topic": topic})
    print(resp)