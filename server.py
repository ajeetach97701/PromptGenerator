import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def generate_prompt(task, api):
    Openai_api_key = api
    llm = ChatOpenAI(api_key=Openai_api_key)
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
    st.set_page_config(page_title="Chatbot Prompt Generator", page_icon="🤖", layout="centered")
    
    st.markdown(
        """
        <style>
        .main {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            border-top: 1px solid #e0e0e0;
        }
        .footer a {
            text-decoration: none;
            color: #0366d6;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🤖 Chatbot Prompt Generator")
    st.write("This application generates a prompt for a chatbot to perform a specific task.")

    st.write("---")

    with st.container():
        # Input field for the API key
        Openai_api_key = st.text_input("🔑 Enter your API KEY FOR OPENAI:", "")

        # Input field for the specific task
        task = st.text_area("✍️ Enter the specific task for the chatbot:", "")

        if st.button("Generate Prompt"):
            if task:
                with st.spinner("Generating prompt..."):
                    prompt = generate_prompt(task=task, api=Openai_api_key)
                    st.success("Prompt generated successfully!")
                    st.write("### Generated Prompt:")
                    st.write(prompt)
            else:
                st.error("Please enter a specific task.")
    
    # Add a footer
    st.markdown(
        """
        <div class="footer">
            <p>Developed by 
                <a href="https://www.linkedin.com/in/ajeet-acharya" target="_blank">Ajeet Acharya</a> | 
                <a href="https://github.com/ajeetach97701/" target="_blank">GitHub</a> 
                and 
                <a href="https://www.linkedin.com/in/aagab-pant" target="_blank">Aagab Pant</a> | 
                <a href="https://github.com/aagabpant" target="_blank">GitHub</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
