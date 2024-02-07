import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple pdfs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask questions about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process' " , accept_multiple_files=True)

        if st.button("Process"):
            

if __name__ == '__main__':
    main
    
