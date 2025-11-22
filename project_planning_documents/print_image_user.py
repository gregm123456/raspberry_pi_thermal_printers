import sys
import os
from escpos.printer import Usb
from escpos.exceptions import DeviceNotFoundError, USBNotFoundError

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
        
        # Print the image
        p.image(image_path)
        
        # Feed paper to ensure the image clears the cutter
        p.text("\n" * 5)
        
        p.cut()
        print("Success")
        
    except (DeviceNotFoundError, USBNotFoundError) as e:
        print(f"Printer not found: {e}")
        print("\nTroubleshooting:")
        print("1. Check if printer is powered on and connected via USB")
        print("2. Run 'lsusb' to verify device is detected")
        print("3. Check if udev rules are configured (see documentation)")
        print("4. Verify you are in the 'lp' group: groups $USER")
        sys.exit(1)
    except PermissionError as e:
        print(f"Permission denied: {e}")
        print("\nYou need permission to access the USB device.")
        print("Either:")
        print("1. Run with sudo (not recommended for regular use)")
        print("2. Set up udev rules (see documentation)")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 print_image_user.py <path_to_image.png>")
        print("       ./venv/bin/python3 print_image_user.py <path_to_image.png>")
        sys.exit(1)
    
    img_path = sys.argv[1]
    if not os.path.exists(img_path):
        print(f"Error: File not found: {img_path}")
        sys.exit(1)
        
    print_image(img_path)
