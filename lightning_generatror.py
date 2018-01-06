from PIL import Image, ImageDraw

background = Image.open("rainy_sky.jpg")
foreground = Image.new('RGB', (400, 400))

draw = ImageDraw.Draw(foreground)
draw.line((100, 200, 150, 300), fill=128)

background.paste(foreground, (0, 0))
background.show()
background.save('test.png', 'PNG')
