import streamlit as st
from research_agent import run_research
import os

st.set_page_config(page_title="AI Trends Researcher", page_icon="🤖")

st.title("🔍 AI Trends Researcher")
st.write("Discover emerging technology trends for 2024 using CrewAI.")

api_key = st.text_input("Enter your Groq API key", type="password")
topic = st.text_input("Enter a research topic", "AI Agents")

if st.button("Run Research"):
    if not api_key or not topic:
        st.error("Please enter both your API key and topic.")
    else:
        with st.spinner("Researching... Please wait"):
            result = run_research(topic, api_key)
        st.subheader("Research Report")
        st.write(result)

