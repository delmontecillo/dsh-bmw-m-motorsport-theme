import pathlib
import re

asar = pathlib.Path(r'C:\Users\admin\AppData\Local\Programs\DeepSeek Harness\resources\app.asar')
data = asar.read_bytes()

words = set()
for m in re.finditer(rb'[A-Za-z0-9]{4,8}_[A-Za-z0-9_]*[Hh]eadline[A-Za-z0-9_]*', data):
    words.add(m.group(0).decode('ascii', 'replace'))
print('headline classes:', sorted(words)[:20])

# Hero phase context, written as UTF-8 to a file.
i = data.find(b'data-phase=hero')
ctx = data[max(0, i - 700):i + 700]
pathlib.Path(r'C:\Users\admin\dsh-bmw-m-motorsport-theme\art\hero-context.txt').write_bytes(ctx)
print('context written, phase idx', i)

j = data.find(b'"hero.headline"')
print('locale key idx', j)
