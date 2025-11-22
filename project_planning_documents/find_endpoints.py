import usb.core

# Vendor: 0x4b43, Product: 0x3538
dev = usb.core.find(idVendor=0x4b43, idProduct=0x3538)

if dev is None:
    print("Device not found")
else:
    print("Device found!")
    for cfg in dev:
        print(f"Configuration: {cfg.bConfigurationValue}")
        for intf in cfg:
            print(f"  Interface: {intf.bInterfaceNumber}, Alt: {intf.bAlternateSetting}")
            for ep in intf:
                print(f"    Endpoint: {hex(ep.bEndpointAddress)}")
                # 0 = Control, 1 = Isochronous, 2 = Bulk, 3 = Interrupt
                type_attr = ep.bmAttributes & 0x03
                direction = "IN" if (ep.bEndpointAddress & 0x80) else "OUT"
                print(f"      Type: {type_attr} (2=Bulk), Direction: {direction}")
