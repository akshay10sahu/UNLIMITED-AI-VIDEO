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
    height=200
)

if st.button("🎬 Generate Video"):
    st.success("Video generation feature will be added in the next version.")
