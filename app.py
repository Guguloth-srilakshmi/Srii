import easyocr
import gradio as gr
import re

# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'hi'])

# Function for OCR and search functionality
def process_image(image, keyword):
    # Perform OCR on the image
    result = reader.readtext(image, detail=0)
    extracted_text = " ".join(result)

    # Highlight the keyword in the extracted text
    highlight_color = "#87CEEB"  # Soft Sky Blue
    if keyword:
        highlighted_text = re.sub(f"({re.escape(keyword)})", 
                                   f"<mark style='background-color: {highlight_color};'>{keyword}</mark>", 
                                   extracted_text, 
                                   flags=re.IGNORECASE)
    else:
        highlighted_text = extracted_text

    # Check if the keyword is in the text
    if keyword and keyword.lower() in extracted_text.lower():
        return f"Keyword '{keyword}' found in the text.", highlighted_text
    else:
        return f"Keyword '{keyword}' not found.", highlighted_text

# Gradio interface
interface = gr.Interface(
    fn=process_image,
    inputs=["image", "text"],
    outputs=["text", "html"],
    title="OCR and Document Search with Highlighting",
    description="Upload an image, extract text, and search for keywords with highlighting."
)

# Launch the app
if __name__ == "__main__":
    interface.launch(share=True)