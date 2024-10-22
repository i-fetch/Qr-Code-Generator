import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=4)

qr.add_data('https://play.google.com/store/apps/details?id=team.opay.pay')
qr.make(fit=True)

img =qr.make_image(fill_color='purple',back_color='white')
img.save('Snapchat.jpg')










