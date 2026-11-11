from PIL import Image

src = r'C:\Users\admin\dsh-bmw-m-motorsport-theme\art\logo-source.png'
im = Image.open(src).convert('RGB')
w, h = im.size
print('size', w, h)

px = im.load()

def lit(x, y):
    r, g, b = px[x, y]
    return (r + g + b) > 110

rows = [sum(1 for x in range(0, w, 2) if lit(x, y)) for y in range(h)]
cols = [sum(1 for y in range(0, h, 2) if lit(x, y)) for x in range(w)]

def spans(vals, thresh):
    out, start = [], None
    for i, v in enumerate(vals):
        on = v > thresh
        if on and start is None:
            start = i
        elif not on and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, len(vals) - 1))
    return out

print('row bands:', spans(rows, 1))
print('col bands:', spans(cols, 1))
