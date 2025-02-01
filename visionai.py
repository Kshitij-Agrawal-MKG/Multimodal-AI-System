from PIL import Image
import pytesseract
from transformers import BlipProcessor, BlipForConditionalGeneration

# Set Tesseract path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

def generate_image_caption(image_path: str) -> str:
    # Open the image
    raw_image = Image.open(image_path).convert('RGB')

    # Process the image
    inputs = processor(raw_image, return_tensors="pt")

    # Generate caption
    out = model.generate(**inputs)
    
    # Decode and return the caption
    return processor.decode(out[0], skip_special_tokens=True)

def extract_text(image_path: str) -> str:
    
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Extract text using Tesseract
        text = pytesseract.image_to_string(image)
        
        return text.strip()
    
    except Exception as e:
        return f"Error: {e}"

