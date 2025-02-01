import streamlit as st
from llm import generate_image_description
from trans import translate_text
import tempfile

# Set up page layout
st.set_page_config(page_title="Multimodal AI System", layout="wide")

# --- Sidebar (Language Selection & Settings) ---
st.sidebar.title("⚙ Settings")
language = st.sidebar.selectbox("🌍 Select Output Language", ["English", "Hindi", "Bengali", "Marathi", "Telugu", "Tamil"])

# --- Main Title ---
st.title("🖼 Multimodal AI System for Custom Output Generation")

# --- Upload Image Section ---
st.subheader("📷 Upload Image for Analysis")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# --- Display Uploaded Image ---
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=300)

# --- User-Defined Prompt Section ---
st.subheader("📝 Describe What You Want")
image_prompt = st.text_area("Enter a prompt to customize the AI response:", height=100, placeholder="E.g., 'Describe this image in a poetic way'")

# --- Processing Button ---
process_button = st.button("🚀 Process Image & Generate Output")

# --- Language Translation Handling ---
def handle_translation(output_text, target_language):
    # Translate the output text to the selected language
    translated_text = translate_text(output_text, target_language)
    return translated_text

# --- Output Section ---
if process_button:
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp.close()
        
        # Generate the description based on the image and user prompt
        output = generate_image_description(tmp.name, image_prompt)
        
        # Translate the generated description based on user-selected language
        if language != "English":
            output = handle_translation(output, language)
    
    st.subheader("🔍 AI-Generated Output")
    st.write(output)

# --- Footer ---
st.markdown("---")
st.markdown("👨‍💻 Developed by **Kshitij Agrawal** | Powered by AI & Vision Models")
