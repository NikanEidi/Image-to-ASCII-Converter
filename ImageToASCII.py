from PIL import Image
import os

# ASCII characters used to represent pixel intensity
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize the image according to the terminal width
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjusting for terminal aspect ratio
    return image.resize((new_width, new_height))

# Convert image to grayscale
def grayify(image):
    return image.convert("L")

# Convert each pixel to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

# Process the image to ASCII art
def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string to fit the terminal width
    ascii_width = image.width
    ascii_art = "\n".join([ascii_str[i:i + ascii_width] for i in range(0, len(ascii_str), ascii_width)])
    return ascii_art

# Save the ASCII art to a text file
def save_ascii_art(ascii_art, output_file="hacker_ascii_art.txt"):
    with open(output_file, "w") as f:
        f.write(ascii_art)
    print(f"ASCII art saved to {output_file}")

# Main function
if __name__ == "__main__":
    image_path = "2.png"  # Replace with your image path
    ascii_art = image_to_ascii(image_path, new_width=100)
    if ascii_art:
        print(ascii_art)
        save_ascii_art(ascii_art)