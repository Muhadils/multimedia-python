from PIL import Image

# Memuat gambar
filtered_image = Image.open('filtered_result.jpg')

# Jika gambar dalam mode RGBA, ubah menjadi RGB
if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')

# Menyimpan gambar
filtered_image.save('converted_image.jpg')