import streamlit as st
from chatbot import predict_disease

st.set_page_config(
    page_title="Healthcare Chatbot",
    page_icon="🩺",
    layout="centered"
)

st.markdown("""
<style>
body {
    background: linear-gradient(to right, #f8fbff, #e0f2fe);
}
.chatbox {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 Healthcare Chatbot")
st.subheader("Offline Disease Prediction System")

st.markdown("<div class='chatbox'>", unsafe_allow_html=True)

user_input = st.text_area(
    "Enter your symptoms (comma separated):",
    placeholder="fever, headache, vomiting"
)

if st.button("🔍 Predict Disease"):
    if user_input.strip() == "":
        st.warning("Please enter symptoms")
    else:
        disease = predict_disease(user_input)
        st.success(f"🩺 Possible Disease: **{disease}**")
        st.info("⚠️ This is not a medical diagnosis. Please consult a doctor.")

st.markdown("</div>", unsafe_allow_html=True)
