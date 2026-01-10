import qrcode

texto = input("ingrese en el texto para generar el codigo QR: ")
img = qrcode.make(texto)
img.save("test.png")