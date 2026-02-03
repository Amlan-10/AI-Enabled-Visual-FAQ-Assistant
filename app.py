import streamlit as st
from vision import extract_text_from_image
from llm import generate_explanation
from PIL import Image

st.set_page_config(page_title="AI Visual FAQ Assistant")

st.title("🧠 AI-Enabled Visual FAQ Assistant")
st.write("Upload an image and ask a question about it.")

uploaded_image = st.file_uploader(
    "Upload image (dashboard, error screen, product, etc.)",
    type=["png", "jpg", "jpeg"]
)

question = st.text_area("Ask your question")

if uploaded_image and question:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze"):
        with st.spinner("Analyzing image..."):
            extracted_text = extract_text_from_image(image)
            answer = generate_explanation(extracted_text, question)

        st.subheader("AI Explanation")
        st.write(answer)
