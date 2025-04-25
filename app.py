import streamlit as st
import openai
import os

st.set_page_config(page_title="Resume Optimizer", layout="centered")
st.title("📄 Smart Resume Optimizer")
st.markdown("Paste your resume and job description to get an AI-enhanced, tailored resume.")

openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.api_base = st.secrets["OPENAI_BASE_URL"]

job_desc = st.text_area("🧾 Job Description", height=200)
resume_text = st.text_area("📄 Your Resume", height=200)

if st.button("🔧 Optimize Resume"):
    with st.spinner("Optimizing..."):
        prompt = f"""
        You are a career coach. Improve and tailor this resume to match the job description.

        Job Description:
        {job_desc}

        Resume:
        {resume_text}

        Return a clean, professional resume that fits the role.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600
            )

            if response.choices:
                content = response.choices[0].message.content.strip()
                st.subheader("🎯 AI-Optimized Resume")
                st.markdown(content)
            else:
                st.warning("⚠️ No content returned. Try again.")

        except Exception as e:
            st.error("❌ Something went wrong.")
            st.code(str(e))
