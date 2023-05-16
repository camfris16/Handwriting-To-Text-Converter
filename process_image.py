from PIL import Image, ImageFilter, ImageOps

# loads image
filename = "image.jpg"
with Image.open(filename) as image:
    image.load()

gray_image = image.convert("L") # converts to Grayscale
smooth = gray_image.filter(ImageFilter.SMOOTH)
edges = smooth.filter(ImageFilter.FIND_EDGES)

final = edges.filter(ImageFilter.BLUR).filter(ImageFilter.MinFilter(3))
final2 = final.filter(ImageFilter.MinFilter)
result = ImageOps.autocontrast(final2)
result.show()