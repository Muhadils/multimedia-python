from PIL import Image

# Memuat gambar
image = Image.open('fotocowok.jpeg')

# Menyimpan gambar
image.save('result.jpg')