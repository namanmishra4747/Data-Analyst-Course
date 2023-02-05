import streamlit as st  #streamlit is library which will generate code result as webapp(react)

st.title("String App")
message = st.text_area("enter some text")
button = st.button("Process text")

if button:
    st.write(message)
if st.checkbox("Show Words"):
    words = message.split()
    st.write(words)
if st.checkbox("charater count"):
    for char in message:
        st.write(f'{char} : {message.count(char)}')

st.video('https://www.youtube.com/watch?v=MB8VbnhE-w4')
