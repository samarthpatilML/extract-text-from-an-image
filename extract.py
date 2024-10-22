import pytesseract
from PIL import Image

# If Tesseract is not in your PATH, specify the installation path
# pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract_executable'

def image_to_text(image_path, note_path):
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Use pytesseract to extract text from image
        extracted_text = pytesseract.image_to_string(img)
        
        # Write the extracted text to a note (text file)
        with open(note_path, 'w') as note_file:
            note_file.write(extracted_text)
        
        print("Text extracted and saved to:", note_path)
    except Exception as e:
        print("Error occurred:", str(e))

# Usage example
image_path = 'C:\Users\sammy\OneDrive\Pictures\Screenshots'  # Replace with your image path
note_path = 'extracted_text_note.txt'  # Path where you want to save the note
image_to_text(image_path, note_path)
