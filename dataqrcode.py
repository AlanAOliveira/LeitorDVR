import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

def generate_qrcode_from_string(data, filename="qrcode.png"):

    qr = qrcode.QRCode(
        version=None,  # Automatically determine version based on data size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")
    return img

# Example usage
if __name__ == "__main__":
    long_string = """ """
    generate_qrcode_from_string(long_string)