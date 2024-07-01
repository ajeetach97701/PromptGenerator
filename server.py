import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def generate_prompt(task, api):
    api = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(api_key=api)
    template = """
    You are an expert prompt engineer and an expert at building LLM application. Your task is explained below: 
    1. You should write a zero shot prompt that will act as an input prompt to the chatbot who will be a virtual representative.
    2. The prompt you provide should be about performing a specific task which is:`{input}`
    3. Do not provide a conversation prompt. The prompt you will generate is not user input prompt but it is an instruction that will be given to the chatbot. 
    Generate the prompt with words less than 300 words.
    """
    prompt = ChatPromptTemplate.from_template(template=template)
    chain = prompt | llm
    res = chain.invoke(task)
    return res.content

# Run the Streamlit app
if __name__ == "__main__":
    st.title("Chatbot Prompt Generator")
    st.write("This application generates a prompt for a chatbot to perform a specific task.")

    # New input field
    Openai_api_key = st.text_input("Enter your name:", "")

    # Input field for the specific task
    task = st.text_area("Enter the specific task for the chatbot:", "")

    if st.button("Generate Prompt"):
        if task:
            with st.spinner("Generating prompt..."):
                prompt = generate_prompt(task=task, api=Openai_api_key)
                st.success("Prompt generated successfully!")
                st.write(prompt)
        else:
            st.error("Please enter a specific task.")

    # Add a footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            text-decoration: none;
            color: #0366d6;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            <p>Developed by 
                <a href="https://www.linkedin.com/in/ajeet-acharya" target="_blank">Ajeet Acharya</a> | 
                <a href="https://github.com/ajeetacharya" target="_blank">GitHub</a> 
                and 
                <a href="https://www.linkedin.com/in/aagab-pant" target="_blank">Aagab Pant</a> | 
                <a href="https://github.com/aagabpant" target="_blank">GitHub</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
