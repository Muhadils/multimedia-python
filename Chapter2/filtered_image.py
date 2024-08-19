from PIL import Image, ImageFilter

# Memuat gambar
image = Image.open('example.jpeg')

# Filtering
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')