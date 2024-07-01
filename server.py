import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the API key
api = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=api)
from chain import generate_prompt


# Run the Streamlit app
if __name__ == "__main__":
    st.title("Chatbot Prompt Generator")
    st.write("This application generates a prompt for a chatbot to perform a specific task.")

    # Input field for the specific task
    task = st.text_area("Enter the specific task for the chatbot:", "")

    if st.button("Generate Prompt"):
        if task:
            with st.spinner("Generating prompt..."):
                prompt = generate_prompt(task)
                st.success("Prompt generated successfully!")
                st.write("### Generated Prompt:")
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
        </style>
    <div class="footer">
        <p>Developed by Your Name</p>
    </div>
    """,
    unsafe_allow_html=True
)
