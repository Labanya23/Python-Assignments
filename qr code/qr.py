import qrcode

date = input("Enter the text or URL for the QR code:")

img = qrcode.make(date)

img.save('d1.png')

print("QR code saved 'd1.png'")