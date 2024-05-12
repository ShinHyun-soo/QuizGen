import base64
import os
from dotenv import load_dotenv

import streamlit as st
import openai

input_path = os.getcwd()
output_path = os.path.join(os.getcwd(), "output")

image_elements = []
load_dotenv()

# Function to encode images
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

for image_file in os.listdir(output_path):
    if image_file.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(output_path, image_file)
        encoded_image = encode_image(image_path)
        image_elements.append(encoded_image)

from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, AIMessage

chain_gpt_4_vision = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1024)

def summarize_image(encoded_image):
    prompt = [
        AIMessage(content="You are a bot that is good at analyzing images."),
        HumanMessage(content=[
            {"type": "text", "text": "Describe the contents of this image."},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                },
            },
        ])
    ]
    response = chain_gpt_4_vision.invoke(prompt)
    return response.content

image_summaries = []
for i, ie in enumerate(image_elements[0:2]):
    summary = summarize_image(ie)
    image_summaries.append(summary)
    print(f"{i + 1}th element of images processed.")


def generate_text(prompt, max_tokens=100):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def main():
    st.title("이미지 기반 퀴즈 생성")

    # Sidebar for user input
    with st.sidebar:
        st.header("이미지 업로드")
        uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        max_tokens = st.number_input("Max Tokens", min_value=10, max_value=500, value=100)

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    else:
        st.write("이미지를 업로드 해주세요.")

    generate_button = st.button("퀴즈 생성")
    # Main content area
    if generate_button and uploaded_image is not None:
        with st.spinner("Generating..."):
            # Encode the uploaded image
            encoded_uploaded_image = base64.b64encode(uploaded_image.read()).decode('utf-8')
            # Summarize the uploaded image
            caption = summarize_image(encoded_uploaded_image)
            st.subheader("이 이미지는 .. ")
            with st.expander("설명 보기"):
                st.write(caption)

            prompt = f"Create multiple-choice questions and answers {caption}, and translate them into korean, only prints korean. "
            # Generate text based on the prompt
            generated_text = generate_text(prompt, max_tokens)
        st.subheader("Generated Text")
        #st.write(generated_text)
        st.session_state.script = generated_text
        st.write(st.session_state.script)


if __name__ == "__main__":
    main()
