import qrcode
import os

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()
filepath = os.path.join("29. QR Code Generator", f"{filename}.png")

qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filepath)
print("QR Code Generated")