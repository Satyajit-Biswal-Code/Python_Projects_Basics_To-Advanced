import qrcode as qr

img=qr.make("https://www.youtube.com/watch?v=fXhtg7pvUoY&list=RDfXhtg7pvUoY&start_radio=1")
img.save("qr.png")