from PIL import Image

# Encrypt the image by inverting the RGB values
def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)  # Invert colors
    img.save(output_path)
    print(f"Encrypted image saved as: {output_path}")

# Decrypt image (invert again to get original)
def decrypt_image(input_path, output_path):
    encrypt_image(input_path, output_path)  # Inversion is symmetric

# Example usage
if __name__ == "__main__":
    print("1. Encrypt Image\n2. Decrypt Image")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        encrypt_image("input.jpg", "encrypted.png")
    elif choice == "2":
        decrypt_image("encrypted.png", "decrypted.png")
    else:
        print("Invalid choice.")
