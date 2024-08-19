from PIL import Image

# Memuat gambar
image = Image.open('example.jpeg')

# Resizing
resized_image = image.resize((100, 100))
resized_image.save('resized_result.jpg')