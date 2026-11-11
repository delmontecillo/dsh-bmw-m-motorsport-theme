from PIL import Image

ART = r'C:\Users\admin\dsh-bmw-m-motorsport-theme\art'
src = Image.open(ART + r'\logo-source.png').convert('RGB')

# Element boxes measured from the source logo.
BOXES = {
    'roundel': (54, 216, 248, 410),
    'm': (335, 252, 683, 373),
    'word': (52, 447, 684, 520),
}

SCALE = 3.0
HEIGHTS = {'roundel': 72, 'm': 45, 'word': 27}
GAPS = {'roundel': 14, 'm': 18}
PAD = 0

def cut(box):
    crop = src.crop(box).convert('RGB')
    # Treat the black field as alpha: unpremultiply the colour so the artwork
    # composites cleanly over the plate instead of dragging a black box.
    rgba = crop.convert('RGBA')
    px = rgba.load()
    w, h = rgba.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            a = max(r, g, b)
            if a == 0:
                px[x, y] = (0, 0, 0, 0)
            else:
                px[x, y] = (min(255, r * 255 // a), min(255, g * 255 // a), min(255, b * 255 // a), a)
    return rgba

parts = []
for key in ('roundel', 'm', 'word'):
    part = cut(BOXES[key])
    target_h = HEIGHTS[key]
    ratio = target_h / part.height
    part = part.resize((max(1, round(part.width * ratio)), target_h), Image.LANCZOS)
    parts.append(part)

canvas_h = max(p.height for p in parts)
width = sum(p.width for p in parts) + GAPS['roundel'] + GAPS['m']
canvas = Image.new('RGBA', (width, canvas_h), (0, 0, 0, 0))

x = 0
for i, part in enumerate(parts):
    y = (canvas_h - part.height) // 2
    canvas.alpha_composite(part, (x, y))
    x += part.width
    if i < len(parts) - 1:
        x += GAPS['roundel' if i == 0 else 'm']

canvas.save(ART + r'\logo-lockup.png')
print('lockup', canvas.size, 'css', (canvas.width / SCALE, canvas.height / SCALE))

# Mock banner: black plate with the livery stripe along its bottom edge.
PLATE_W, PLATE_H = 180, 32
PLATE_PAD = 12

def mock(bg, label):
    img = Image.new('RGB', (640, 90), bg)
    plate = Image.new('RGB', (PLATE_W, PLATE_H), (10, 10, 11))
    logo = canvas.resize((round(canvas.width / SCALE), round(canvas.height / SCALE)), Image.LANCZOS)
    plate.paste(logo, (PLATE_PAD, (PLATE_H - logo.height) // 2), logo)
    for i, col in enumerate([(23, 68, 154), (47, 123, 255), (53, 183, 242), (216, 30, 30)]):
        for x in range(i * PLATE_W // 4, (i + 1) * PLATE_W // 4):
            for y in range(PLATE_H - 3, PLATE_H):
                plate.putpixel((x, y), col)
    img.paste(plate, (0, 0))
    img.save(ART + rf'\mock-{label}.png')

mock((245, 242, 236), 'light')
mock((10, 11, 14), 'dark')
print('mocks written')
