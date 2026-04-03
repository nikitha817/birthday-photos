import qrcode
url = "http://127.0.0.1:5500/birthday-photos/index.html".strip()
file_path = "C:\\Users\\kanth\\OneDrive\\Desktop\\qr_code.png"
qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(file_path)