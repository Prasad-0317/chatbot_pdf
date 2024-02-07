import streamlit as st
import pdfplumber
from PyPDF2 import PdfReader

st.title("Chat with PDF...")
st.write("Upload a PDF and start chatting!") 

def extract_text_pdf(pdf):
    pdf_reader = PdfReader(pdf)
    return ''.join(page.extract_text() for page in pdf_reader.pages)

def main():
    pdf = st.file_uploader('Choose your .pdf file', type="pdf")
    if pdf : text = extract_text_pdf(pdf)
    st.write("PDF Content Extracted!")
    st.write(text)

if __name__ == '__main__': main() 