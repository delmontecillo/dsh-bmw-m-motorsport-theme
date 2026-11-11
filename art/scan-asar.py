import pathlib

asar = pathlib.Path(r'C:\Users\admin\AppData\Local\Programs\DeepSeek Harness\resources\app.asar')
needle = b'Into the Unknown'
data = asar.read_bytes()
print('asar bytes:', len(data))
start = 0
hits = 0
while True:
    i = data.find(needle, start)
    if i < 0:
        break
    hits += 1
    lo = max(0, i - 120)
    hi = min(len(data), i + 160)
    chunk = data[lo:hi].decode('utf-8', 'replace').replace('\n', ' ')
    print(f'--- hit {hits} at {i} ---')
    print(chunk)
    start = i + 1
    if hits >= 6:
        break
print('hits:', hits)
