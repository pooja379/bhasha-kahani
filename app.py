import streamlit as st
from datetime import datetime
import os

st.set_page_config(page_title="Bhasha Kahani – Storyteller of India")

st.title("📖 Bhasha Kahani – Storyteller of India")
st.write("Share a story from your language or culture. Let’s preserve India’s traditions through your voice and words.")

name = st.text_input("Your Name (Optional)")
language = st.selectbox("Choose Language", ["Telugu", "Hindi", "Tamil", "Kannada", "Other"])
text_story = st.text_area("Type your story (even a few lines are fine!)")

audio_file = st.file_uploader("Upload your voice story (optional)", type=["mp3", "wav"])
doc_file = st.file_uploader("Upload your written story (PDF or DOCX)", type=["pdf", "docx"])

if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    story_folder = "stories"
    os.makedirs(story_folder, exist_ok=True)

    # Save typed story
    filename = f"{story_folder}/story_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Language: {language}\n")
        f.write("Story:\n")
        f.write(text_story)

    # Save audio file
    if audio_file is not None:
        audio_path = f"{story_folder}/audio_{timestamp}_{audio_file.name}"
        with open(audio_path, "wb") as f:
            f.write(audio_file.read())

    # Save document file
    if doc_file is not None:
        doc_path = f"{story_folder}/doc_{timestamp}_{doc_file.name}"
        with open(doc_path, "wb") as f:
            f.write(doc_file.read())

    st.success("✅ Story submitted successfully. Thank you for contributing!")
    st.subheader("📚 Submitted Stories")

if os.path.exists("stories"):
    for file in os.listdir("stories"):
        if file.endswith(".txt"):
            with open(os.path.join("stories", file), "r", encoding="utf-8") as f:
                st.text_area(file, f.read(), height=200)
else:
    st.info("No stories submitted yet.")

