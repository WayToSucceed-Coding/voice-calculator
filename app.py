import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Voice-Controlled Calculator", page_icon="🧮")
st.header("Voice-Controlled Calculator")

col1, col2 = st.columns([1, 1])  # side-by-side (i.e., same row)

# Converts words to mathematical expression
def clean_and_solve(text):
    text = text.lower()
    text = text.replace("multiplied by", "*")
    text = text.replace("divided by", "/")
    text = text.replace("into", "*")
    text = text.replace("over", "/")
    text = text.replace("x", "*")
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("what is", "")
    text = text.replace("calculate", "")
    text = text.replace("can you", "")
    text = text.replace("solve", "")
    text = text.replace("please", "")
    st.code(f"Expression: {text}")

    try:
        result = eval(text)
        st.success(f"Result: {result}")
    except:
        st.error("Invalid expression. Please try saying something like 'three plus four' or 'nine divided by three'.")


with col1:
    st.image("calculator.png", width=300)
    
with col2:
    st.markdown(
        """
        Click the mic and say something like:
        - `three plus five`
        - `twelve divided by four`
        - `seven times nine`
        """
    )
    
    audio_file = st.audio_input("Say your calculation out loud")
    
    if audio_file is not None:
        recognizer = sr.Recognizer()
        
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            try:
                spoken_text = recognizer.recognize_google(audio)
                st.success(f"You said: {spoken_text}")
                clean_and_solve(spoken_text)
            except sr.UnknownValueError:
                st.warning("Sorry, couldn't understand. Please try again.") 
            except Exception as e:
                st.error(f"Error: {e}")
