from PIL import Image, ImageFilter, ImageOps

# loads image
filename = "image.jpg"
with Image.open(filename) as image:
    image.load()

gray_image = image.convert("L") # converts to Grayscale

result = ImageOps.autocontrast(gray_image)
result.show()