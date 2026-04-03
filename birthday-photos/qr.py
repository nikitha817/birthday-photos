import qrcode
qr = qrcode.make("http://127.0.0.1:5500/birthday-photos/index.html")
qr.save("qr.png")
print("QR code generated and saved as qr.png")
print("You can open qr.png to view the QR code, which will direct you to the birthday photos webpage.")
print(qr)