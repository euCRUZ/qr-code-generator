# QR Code Generator

A simple Python project to generate customizable QR codes with custom colors.

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd qr-code-generator
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install qrcode[pil]
   ```

## 📦 Dependencies

The project uses the following libraries:

- **qrcode**: For generating QR codes
- **pillow**: For image manipulation (included with qrcode[pil])
- **urllib**: For URL parsing (included in standard Python)
- **os**: For system operations (included in standard Python)
- **requests**: For checking if the URL exists and is online

## 🎯 How to use

1. **Run the script**

   ```bash
   python qrcodeGenerator.py
   ```

2. **Follow the terminal instructions:**

   - Enter the link/URL you want to convert to QR code
   - Enter the fill color in hexadecimal (ex: #10254B)
   - Enter the background color in hexadecimal (ex: #FFFFFF)

3. **The file will be saved automatically**
   - QR codes are saved in the `QRCODEs/` folder
   - The filename is based on the URL domain
   - Format: `qrcode_[domain].png`

## 🎨 Customization

### Colors

- **Fill color**: Color of the QR code blocks
- **Background color**: Color of the QR code background
- Use hexadecimal codes (ex: #FF0000 for red)

### Popular color examples:

- Black: `#000000`
- White: `#FFFFFF`
- Blue: `#0000FF`
- Red: `#FF0000`
- Green: `#00FF00`
- Purple: `#800080`

## 📁 Project Structure

```
qr-code-generator/
├── qrcodeGenerator.py    # Main script
├── QRCODEs/              # Folder where QR codes are saved
├── requirements.txt      # Dependencies list
├── README.md            # Documentation

```

## ⚙️ QR Code Settings

The script uses the following default settings:

- **Version**: 1 (QR code size, 1-40)
- **Error correction**: H (high error correction)
- **Box size**: 5 pixels
- **Border**: 4 blocks

## 🔧 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'qrcode'"

```bash
pip install qrcode[pil]
```

### Error: "ModuleNotFoundError: No module named 'PIL'"

```bash
pip install pillow
```

### File permission error

- Check if you have write permission in the folder
- Make sure the `QRCODEs` folder exists

## 📝 Usage Example

```bash
$ python qrcodeGenerator.py
Plase enter the link here: https://www.google.com
Enter the fill color in hexadecimal (ex: #10254B): #000000
Enter the background color in hexadecimal (ex: #FFFFFF): #FFFFFF
QR Code generated and saved as 'qrcode_google.png'
Open the 'qrcode_google.png' file to view the QR Code
```

## 📦 About requirements.txt

The `requirements.txt` file is a Python standard that lists all project dependencies. It allows you to install all necessary libraries with a single command:

```bash
pip install -r requirements.txt
```

**File contents:**

- `qrcode[pil]>=7.3` - Main library for generating QR codes (version 7.3 or higher)
- `pillow>=8.0.0` - Library for image manipulation (version 8.0 or higher)

The `[pil]` in `qrcode[pil]` means we're installing qrcode with Pillow (PIL) support for image manipulation.

## 🤝 Contributing

Feel free to contribute with improvements:

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request
