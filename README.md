# PixelVault – Steganography Tool

**PixelVault** is a web-based steganography tool that allows users to hide secret messages inside images and retrieve them securely. It uses the Least Significant Bit (LSB) technique to encode text within image pixels, making the data invisible to the human eye but retrievable with the right tool.

## Project Objectives

- Hide sensitive messages inside image files using steganography  
- Retrieve and decode hidden messages from encoded images  
- Offer a simple, secure web interface for both encoding and decoding  
- Demonstrate the fundamentals of LSB-based image steganography  

## Technologies Used

- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS (via Flask templates)  
- **Image Processing**: PIL (Python Imaging Library)  
- **Algorithm**: Least Significant Bit (LSB) steganography  
- **File Handling**: Local file storage via Flask’s upload folder  

## Key Features

- **Text-to-Image Encoding**  
  Converts secret text into binary and embeds it in the LSBs of an image’s RGB values

- **Image-to-Text Decoding**  
  Extracts the hidden message from encoded images and displays it to the user

- **Web Interface**  
  Upload your own image and type a message to encode or decode without needing any technical setup

- **Input Validation**  
  Checks message length to avoid exceeding image capacity, and handles corrupted data gracefully

- **Error Handling**  
  Detects corrupted images, unsupported characters, or decoding issues and shows friendly messages  

## How It Works

### 1. Encoding Process

- User uploads an image and inputs the secret message  
- The message is converted to binary and its length is prepended in 32 bits  
- The bits are hidden in the least significant bits (LSBs) of the image pixels  
- The modified image is saved and downloaded by the user  

### 2. Decoding Process

- User uploads the previously encoded image  
- The system reads the first 32 bits to determine message length  
- Remaining bits are read and reconstructed into the original message  

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sudarshan007AS/PixelVault.git
cd PixelVault
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Project Structure

```
PixelVault/
│
├── app.py                 # Main Flask app
├── steg.py                # Steganography logic (encode/decode)
├── requirements.txt       # Dependencies (Flask, Pillow)
├── templates/
│   ├── index.html         # Home page for encoding/decoding
│   └── result.html        # Result page for decoded messages
├── static/
│   └── encoded_image.png  # Output image with hidden message
└── uploads/               # Temporary storage for uploaded images
```

## Future Enhancements

- Add support for file-based (non-text) payloads  
- Implement image encryption before encoding  
- Add image preview and dark mode  
- Support drag-and-drop for files  

## 👤 Author

**Sudarshan A S**  
[LinkedIn](https://www.linkedin.com/in/sudarshanas) • [GitHub](https://github.com/Sudarshan007AS)

---
