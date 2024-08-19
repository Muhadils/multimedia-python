from PIL import Image, ImageFilter

# Memuat gambar
image = Image.open('fotocowok.jpeg')

# Menerapkan filter ke gambar
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')