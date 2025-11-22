import sys
import os
from escpos.printer import Usb

def print_image(image_path):
    # Vendor: 0x4b43, Product: 0x3538
    # Out Endpoint: 0x03
    # In Endpoint: 0x81
    try:
        # Initialize printer with the specific endpoints found earlier
        p = Usb(0x4b43, 0x3538, in_ep=0x81, out_ep=0x03)
        
        # Fix for "media.width.pixel field not set" warning
        # The MC582H is a 58mm printer with 384 dots of resolution (203 DPI)
        p.profile.profile_data['media'] = {
            'width': {'pixels': 384},
            'dpi': 203
        }
        
        print(f"Printing image: {image_path}")
        
        # The image method handles printing. 
        # Note: For 58mm printers like the MC582H, the print width is typically 384 dots.
        # If the image is wider, the library might attempt to scale it or it might be truncated 
        # depending on implementation, but usually it's best to resize images to ~384px width beforehand.
        p.image(image_path)
        
        # Feed paper to ensure the image clears the cutter
        p.text("\n" * 5)
        
        p.cut()
        print("Success")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: sudo ./venv/bin/python3 print_image.py <path_to_image.png>")
        sys.exit(1)
    
    img_path = sys.argv[1]
    if not os.path.exists(img_path):
        print(f"Error: File not found: {img_path}")
        sys.exit(1)
        
    print_image(img_path)
