import streamlit as st
from google import genai

st.set_page_config(page_title="AI Tool", page_icon="🤖")

st.title("🤖 AI Tool")
st.write("Apna question ya topic likhein aur AI aapko answer dega:")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        # New Google GenAI Client
        client = genai.Client(api_key=api_key)
        
        user_prompt = st.text_area("Aap kya poochhna chahte hain?")
        
        if st.button("Generate Answer"):
            if user_prompt:
                with st.spinner("Answer generate ho raha hai..."):
                    # Updated modern model call
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_prompt,
                    )
                    st.write("### Result:")
                    st.write(response.text)
            else:
                st.warning("Pehle kuch type toh karein!")
    except Exception as e:
        st.error(f"Error details: {e}")
