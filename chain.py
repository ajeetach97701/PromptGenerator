from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()


api = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=api)
def generate_prompt(input):
    template = """You are an expert prompt engineer and an expert at building llm application. Your task is explained below: 
    1. You should write a zero shot prompt that will act as a input prompt to the chatbot who will be a virtual representative.
    2. The prompt you provide should be about performing a specific task which is:`{input}`
    3. Do not provide a conversation prompt. The prompt you will generate is not user input prompt but it is a instruction that will be given to the chatbot. 
    Generate the prompt with words less than 300 words.

    """
    prompt = ChatPromptTemplate.from_template(template=template)
    chain = prompt| llm

    # input = "my company name is abc company ltd. The services we provide is car wash, servicing, engineering, carpentering, delivery, barista."
    res = chain.invoke(input)
    return res.content