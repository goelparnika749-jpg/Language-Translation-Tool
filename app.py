import streamlit as st
from translate import Translator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍"
)

st.title("🌍 Language Translation Tool")
st.write("Enter text and select a language to translate it.")

languages = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh",
    "Arabic": "ar"
}

text = st.text_area(
    "Enter text:",
    placeholder="Type your sentence here..."
)

target_language = st.selectbox(
    "Select target language:",
    list(languages.keys())
)

if st.button("🔄 Translate"):

    if not text.strip():
        st.warning("Please enter some text first.")

    else:
        try:
            translator = Translator(
                from_lang="en",
                to_lang=languages[target_language]
            )

            translated_text = translator.translate(text)

            st.subheader("Translated Text")
            st.success(translated_text)

        except Exception:
            st.error(
                "Translation failed. Please check your internet connection "
                "and try again."
            )