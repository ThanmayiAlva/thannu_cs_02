# 🖼️ Image Encryption Tool using Pixel Manipulation

A simple Python program that encrypts and decrypts images by manipulating pixel values using basic mathematical operations. Ideal for learning how image data can be transformed securely at the pixel level.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🔐 Features

- Encrypts image pixels by inverting and shifting RGB values
- Decrypts back using the reverse logic
- Works with any `.jpg`, `.png`, or compatible image format
- Customizable shift value for different encryption variations

---

## 🛠️ How It Works

- **Encryption:**  
  `(255 - R + shift) % 256` for each RGB value
- **Decryption:**  
  `(255 - R - shift) % 256` for each RGB value

This simple pixel transformation is **reversible**, making it a good teaching tool for basic encryption concepts.

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have Python 3 installed and then install **Pillow**:

```bash
pip install pillow

python image_cipher.py

image-encryption-tool/
├── image_cipher.py        # Main Python script
├── README.md              # Project documentation
├── encrypted_<filename>   # Encrypted image output
├── decrypted_<filename>   # Decrypted image output

Enter image path: photo.jpg
Encrypt or decrypt? (e/d): e
Enter shift value: 50

✔ Encrypted image saved as: encrypted_photo.jpg

Enter image path: encrypted_photo.jpg
Encrypt or decrypt? (e/d): d
Enter shift value: 50

✔ Decrypted image saved as: decrypted_encrypted_photo.jpg
