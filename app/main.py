import streamlit as st
from chain import Chain
import os

st.title('Cold email generator')
url_input = st.text_input("Enter the job description", value="")
submit_button = st.button("Submit")

resume = st.text_input("Paste resume")


if(submit_button):
    chain = Chain()
    extract_resume = chain.extract_resume(resume)
    page_data = chain.scrape_from_web(url_input)
    job = chain.extract_job_desc(page_data)
    email = chain.write_email(job, extract_resume)
    st.write(email)
    st.write(extract_resume)
