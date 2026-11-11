from PIL import Image

ART = r'C:\Users\admin\dsh-bmw-m-motorsport-theme\art'
src = Image.open(ART + r'\logo-source.png').convert('RGB')

# Roundel box measured from the supplied logo, plus breathing room.
box = (54 - 10, 216 - 10, 248 + 10, 410 + 10)
tile = src.crop(box).resize((96, 96), Image.LANCZOS)
tile.save(ART + r'\roundel.png')
print('roundel tile', tile.size)

bg = src.getpixel((5, 5))
print('source background', bg)

# Preview: the row the user asked for, at 2x, on the dark sidebar fill.
row = Image.new('RGB', (520, 88), (13, 16, 19))
icon = Image.open(ART + r'\roundel.png').resize((48, 48), Image.LANCZOS)
row.paste(icon, (16, 20))
row.save(ART + r'\row-preview.png')
print('row preview written')
