import pathlib
import re

asar = pathlib.Path(r'C:\Users\admin\AppData\Local\Programs\DeepSeek Harness\resources\app.asar')
data = asar.read_bytes()

for needle in (b'data-phase="hero"', b'data-phase=hero', b'data-phase'):
    print(needle, data.count(needle))

i = data.find(b'hero.headline')
print('--- around hero.headline ---')
print(data[max(0, i - 500):i + 500].decode('utf-8', 'replace').replace('\n', ' '))

for word in (b'headline', b'heroTitle', b'heroTitleText', b'_title'):
    print(word, data.count(word))
