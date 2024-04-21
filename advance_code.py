import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=5)

qr.add_data("https://www.pinterest.com/")
qr.make(fit=True)
# img = qr.make_image(fill_color="red", back_color="blue")
img = qr.make_image(fill_color="brown", back_color="white")
img.save("Pinterest Web.png")
