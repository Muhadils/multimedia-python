from PIL import Image

# Memuat gambar
image = Image.open('fotocowok.jpeg')

# Cropping
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')