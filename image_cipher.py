from PIL import Image
import os

def encrypt_image(image_path, shift=50):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Simple encryption: shift and invert color
            pixels[i, j] = (
                (255 - r + shift) % 256,
                (255 - g + shift) % 256,
                (255 - b + shift) % 256
            )

    encrypted_path = "encrypted_" + os.path.basename(image_path)
    img.save(encrypted_path)
    print(f"[✔] Encrypted image saved as: {encrypted_path}")


def decrypt_image(image_path, shift=50):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Reverse of encryption
            pixels[i, j] = (
                (255 - r - shift) % 256,
                (255 - g - shift) % 256,
                (255 - b - shift) % 256
            )

    decrypted_path = "decrypted_" + os.path.basename(image_path)
    img.save(decrypted_path)
    print(f"[✔] Decrypted image saved as: {decrypted_path}")


def main():
    print("=== Image Encryption Tool ===")
    path = input("Enter image path (e.g. image.png): ")
    if not os.path.exists(path):
        print("[✘] File not found.")
        return

    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    shift = int(input("Enter shift value (default is 50): ") or 50)

    if choice == 'e':
        encrypt_image(path, shift)
    elif choice == 'd':
        decrypt_image(path, shift)
    else:
        print("[✘] Invalid choice. Use 'e' for encrypt or 'd' for decrypt.")


if __name__ == "__main__":
    main()
