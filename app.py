import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Jannat AI Tool", page_icon="🤖")

st.title("🤖 Jannat AI Tool")
st.write("Apna question ya topic likhein aur AI aapko answer dega:")

# API Key Input
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # User Input
    user_prompt = st.text_area("Aap kya poochhna chahte hain?")
    
    if st.button("Generate Answer"):
        if user_prompt:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_prompt)
            st.write("### Result:")
            st.write(response.text)
        else:
            st.warning("Pehle kuch type toh karein!")
