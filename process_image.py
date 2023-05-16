from PIL import Image

# loads image
filename = "image.jpg"
with Image.open(filename) as image:
    image.load()

gray_image = image.convert("L") # converts to Grayscale

gray_image.show()
