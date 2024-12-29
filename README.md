# Image to ASCII Converter

This project is a Python-based script that converts images into ASCII art. The resulting ASCII representation captures the essence of the image using a customizable character set.

## Features
- Convert any image to ASCII art.
- Supports various character sets for customization.
- Easily adjustable resolution for detailed ASCII representation.
- Export the result as a text file.

## Requirements
- Python 3.7 or higher
- Required Libraries:
  - `Pillow` (for image processing)
  - `sys` (for handling command-line arguments)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ImageToASCII.git
   cd ImageToASCII
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:
```bash
python ImageToASCII.py <path-to-image> [<output-width>]
```

- `<path-to-image>`: The path to the input image file.
- `[<output-width>]` (optional): The desired width of the ASCII output (default: 100).

### Example
```bash
python ImageToASCII.py example.jpg 150
```

## Output
The ASCII art will be displayed in the terminal and saved to a `.txt` file in the current directory.

## Contribution
Feel free to fork this repository and make contributions. Submit a pull request for any major changes or new features.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Inspired by the classic art of ASCII and the community of creative developers.
