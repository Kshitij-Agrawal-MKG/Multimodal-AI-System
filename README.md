# 🖼 Multimodal AI System for Custom Output Generation

## 📌 Project Overview
The **Multimodal AI System** is a **Streamlit-based web application** that allows users to:
- **Upload an image**.
- **Generate a detailed or creative description** of the image using AI.
- **Extract text from the image** using OCR (Optical Character Recognition).
- **Translate the generated description** into multiple languages (Hindi, Tamil, Telugu, Marathi, Bengali, and English).

This project integrates **Computer Vision**, **Natural Language Processing (NLP)**, and **Machine Translation** to provide a **multimodal AI experience**.

---

## 🚀 Features
- **Image Captioning** 🖼 ➝ AI generates descriptions for uploaded images.
- **Text Extraction (OCR)** 📄 ➝ Extracts text from images using Tesseract.
- **Custom Prompts** 📝 ➝ Users can define how they want the AI to describe the image.
- **Multi-Language Support** 🌍 ➝ The AI-generated description can be translated into multiple languages.
- **Interactive UI** 🎨 ➝ Uses Streamlit for a clean and user-friendly interface.

---

## 🏗️ **Project Structure**

📂 **Multimodal-AI**

- `app.py`               — Streamlit UI for user interaction
- `llm.py`               — Uses AI models to generate image descriptions
- `trans.py`             — Handles text translation using Microsoft Translator API
- `visionai.py`          — Performs OCR and image captioning
- `requirements.txt`     — List of required Python packages
- `README.md`            — Project documentation


---

## 🛠 **Installation Guide**
Follow these steps to set up the project on your local machine.

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/Multimodal-AI-System.git
cd Multimodal-AI-System
```


### 2️⃣ **Set Up a Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```bash
streamlit run app.py
```
This will start a **local web server**, and you can access the app in your browser.

---

## 📝 **How It Works**
1. **Upload an Image** 🖼 ➝ Select an image file (`.jpg`, `.png`, `.jpeg`).
2. **Enter a Custom Prompt** 📝 ➝ Describe how you want the AI to interpret the image.
3. **Process the Image** 🚀 ➝ Click on the "Process Image & Generate Output" button.
4. **View the AI-Generated Description** 🔍 ➝ The system will display:
   - AI-generated caption.
   - Extracted text from the image (OCR).
   - Translated output (if selected).
5. **Choose a Language** 🌍 ➝ Translate the output into Hindi, Tamil, Telugu, Marathi, Bengali, or English.

---

## 📜 **Detailed Explanation of Scripts**

### 1️⃣ **`app.py` (Main Web App)**
- **Uses Streamlit** to create an interactive web interface.
- **Handles file uploads**, user input, and language selection.
- **Calls `llm.py` to generate AI-based descriptions**.
- **Calls `trans.py` to translate the descriptions**.

### 2️⃣ **`llm.py` (AI-Based Image Captioning)**
- Uses **Salesforce's BLIP model** to generate an image caption.
- Extracts **text using OCR (Tesseract)**.
- Sends a **customized request** to the AI model via **Groq API**.
- Uses **LLaMA 3.3-70B** to **generate detailed descriptions** based on user input.

### 3️⃣ **`trans.py` (Text Translation)**
- Uses **Microsoft Cognitive Translator API** to convert English descriptions into:
  - **Hindi, Tamil, Telugu, Marathi, and Bengali**.
- Sends a **POST request** to the **Microsoft Translator API** and retrieves the translated text.

### 4️⃣ **`visionai.py` (Computer Vision & OCR)**
- **Image Captioning** ➝ Uses **BLIP (Salesforce's model)** to generate descriptions.
- **Text Extraction (OCR)** ➝ Uses **Tesseract** to extract text from the image.

---

## 🔧 **Dependencies**
All required dependencies are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

---

## 🔑 **Environment Variables & API Keys**
To use **Microsoft Translator API** and **Groq API**, replace placeholders with your actual API keys:

- **Inside `trans.py` (Microsoft Translator API)**
  ```python
  key = "YOUR_MICROSOFT_TRANSLATOR_API_KEY"
  location = "YOUR_REGION"
  ```
  
- **Inside `llm.py` (Groq API)**
  ```python
  api = "YOUR_GROQ_API_KEY"
  ```

---

## 🚀 Live Demo  
[Click here to access the project](https://multiamodal-ai-system.streamlit.app/)

## 🎥 **Demo Video**

👉 **[Click here to watch the demo video](https://youtu.be/JduGvL-vdhM)** 




## 🤝 **Contributing**
Feel free to contribute by:
- Fixing issues 🛠️
- Adding new features 🚀
- Improving performance ⚡
- Creating better UI enhancements 🎨

Fork the repository and submit a pull request.

---

## 📜 **License**
This project is **open-source** under the **MIT License**.

---

## 📧 **Contact**
If you have any questions, feel free to reach out:
- **Developer**: Kshitij Agrawal  
- **Email**: kshitiijagrawal53@gmail.com  
- **LinkedIn**: [Kshitij Agrawal](https://www.linkedin.com/in/kshitij-agrawal-319b36293/)


---

🌟 **Star this repo if you find it useful!** ⭐
```
