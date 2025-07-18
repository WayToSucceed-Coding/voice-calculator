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
        Press the button and say something like:
        - `three plus five`
        - `twelve divided by four`
        - `seven times nine`
        """
        )
    
    if st.button("🎤 Start Voice Input"):
        recognizer = sr.Recognizer()
        
        with st.spinner("🎤 Listening... Please speak clearly"):
            with sr.Microphone() as source:
                try:
                    audio = recognizer.listen(source, timeout=5)
                    spoken_text = recognizer.recognize_google(audio)
                    st.success(f"You said: {spoken_text}")
                    clean_and_solve(spoken_text)
                except sr.WaitTimeoutError:
                    st.warning("Listening timed out. Please try again.")
                except sr.UnknownValueError:
                    st.warning("Sorry, couldn't understand. Please try again.") 
                except Exception as e:
                    st.error(f"Error: {e}")

   
