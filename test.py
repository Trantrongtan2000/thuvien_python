import pyqrcode
qr = pyqrcode.create('Unladden swallow')
qr.png('qr.png', scale=5)