import os
import qrcode
from urllib.parse import urlparse
import requests

os.makedirs("QRCODEs", exist_ok=True)


# Enter the link here
def is_valid_url(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        if not parsed.netloc:
            return False
        return True
    except Exception:
        return False


def url_responds(url):
    try:
        resp = requests.head(url, allow_redirects=True, timeout=5)
        return resp.status_code < 400
    except Exception:
        return False


while True:
    data = input("Plase enter the link here: ")
    if not is_valid_url(data):
        print(
            "[ERROR] Invalid URL. Please include http:// or https:// and a valid domain."
        )
        continue
    if not url_responds(data):
        print(
            "[ERROR] Unable to access the URL. Please check if it exists and is online."
        )
        continue
    break

# Enter the colors in hexadecimal
fill_color = input("Enter the fill color in hexadecimal (ex: #10254B): ")
back_color = input("Enter the background color in hexadecimal (ex: #FFFFFF): ")

# Creating the QR Code
qr = qrcode.QRCode(
    version=1,  # Size of the QR Code (1 a 40)
    error_correction=qrcode.ERROR_CORRECT_H,  # Error correction level
    box_size=5,  # Size of the blocks of the QR Code
    border=4,  # Border around the QR Code
)
qr.add_data(data)
qr.make(fit=True)

# Creating and saving the QR Code image
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Extract domain from URL for filename
try:
    parsed_url = urlparse(data)
    domain = parsed_url.netloc
    # Remove common domain extensions
    domain_extensions = [
        ".vercel",
        ".com",
        ".org",
        ".net",
        ".edu",
        ".gov",
        ".mil",
        ".int",
        ".co",
        ".io",
        ".ai",
        ".app",
        ".dev",
        ".tech",
        ".info",
        ".biz",
        ".tv",
        ".me",
        ".us",
        ".br",
        ".uk",
        ".de",
        ".fr",
        ".es",
        ".it",
        ".jp",
        ".cn",
        ".ru",
        ".in",
        ".au",
        ".ca",
    ]

    for ext in domain_extensions:
        if domain.endswith(ext):
            domain = domain[: -len(ext)]
            break

    filename = f"qrcode_{domain}.png"
except:
    filename = "qrcode.png"

with open(f"QRCODEs/{filename}", "wb") as f:
    img.save(f)  # Save the QR Code as image

# Show the QR Code image
# img.show()
print(f"QR Code generated and saved as '{filename}'")
print(f"Open the '{filename}' file to view the QR Code")
