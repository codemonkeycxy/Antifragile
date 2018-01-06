from PIL import Image, ImageDraw

background = Image.open("rainy_sky.jpg")
draw = ImageDraw.Draw(background)
draw.line((100, 200, 150, 300), fill=128)

background.show()
background.save('test.png', 'PNG')
