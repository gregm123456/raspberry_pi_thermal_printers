from escpos.printer import Usb

# Vendor: 0x4b43, Product: 0x3538
# Out Endpoint: 0x03 (found via scan)
# In Endpoint: 0x81 (found via scan)
try:
    p = Usb(0x4b43, 0x3538, in_ep=0x81, out_ep=0x03)
    
    p.text("Hello World\n")
    p.text("Endpoint Configuration Correct!\n")
    p.cut()
    print("Success")
except Exception as e:
    print(f"Error: {e}")
