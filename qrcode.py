import pyqrcode as qr

s = "https://payeasily.netlify.app/"

url = qr.create(s)

url.svg("myqr.svg", scale = 8)