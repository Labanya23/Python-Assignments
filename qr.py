import qrcode

date = input("Enter the text or URL for the QR code:")

img = qrcode.make(date)

#img.save('d1.png')

#print("QR code saved 'd1.png'")

qr= qrcode.RCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_date(date)
qr.make(fit=True)

img= qr.make_image(fill_color='red', black_color = 'white')
img.save('my_qr_code.png')

print("QR Code saved as 'my_qr_code.png'")