import streamlit as st
from summarizer import summarize

st.set_page_config(page_title="AI Text Summarizer")

st.title("🧠 AI Text Summarizer")
st.write("Paste your text below and get a concise summary.")

text = st.text_area("Input Text", height=250)

ratio = st.slider("Summary Length", 0.1, 0.9, 0.3)

if st.button("Summarize"):
    if text.strip():
        summary = summarize(text, ratio)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text.")
