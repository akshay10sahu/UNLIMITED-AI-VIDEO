import streamlit as st

st.set_page_config(
    page_title="Unlimited AI Studio",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Unlimited AI Studio")
st.write("Welcome to the AI Movie Generator")

language = st.selectbox(
    "Choose Language",
    [
        "English",
        "Hindi",
        "Bengali",
        "Tamil",
        "Telugu",
        "Urdu"
    ]
)

prompt = st.text_area(
    "Describe your movie",
    height=200,
    placeholder="Write your movie idea here..."
)

duration = st.selectbox(
    "Choose Video Duration",
    [
        "30 Seconds",
        "1 Minute",
        "3 Minutes",
        "5 Minutes"
    ]
)

if st.button("🎬 Generate Video"):
    if prompt.strip() == "":
        st.warning("Please write your movie idea first.")
    else:
        st.success("Your AI movie request has been submitted!")
        st.write("Language:", language)
        st.write("Duration:", duration)
        st.write("Story:", prompt)
