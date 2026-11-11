from PIL import Image

src = r'C:\Users\admin\dsh-bmw-m-motorsport-theme\art\logo-source.png'
im = Image.open(src).convert('RGB')
px = im.load()
w, h = im.size

def lit(x, y):
    r, g, b = px[x, y]
    return (r + g + b) > 110

def band_box(x0, x1, y0, y1, thresh=1):
    xs, ys = [], []
    for y in range(y0, y1):
        for x in range(x0, x1, 1):
            if lit(x, y):
                xs.append(x)
                ys.append(y)
    if not xs:
        return None
    return (min(xs), min(ys), max(xs), max(ys))

# symbol row 216..409, text row 447..519
roundel = band_box(40, 260, 200, 430)
m_mark = band_box(270, 700, 200, 430)
wordmark = band_box(40, 700, 440, 530)
print('roundel', roundel, 'size', (roundel[2]-roundel[0]+1, roundel[3]-roundel[1]+1) if roundel else None)
print('m_mark', m_mark, 'size', (m_mark[2]-m_mark[0]+1, m_mark[3]-m_mark[1]+1) if m_mark else None)
print('wordmark', wordmark, 'size', (wordmark[2]-wordmark[0]+1, wordmark[3]-wordmark[1]+1) if wordmark else None)
