import pathlib

asar = pathlib.Path(r'C:\Users\admin\AppData\Local\Programs\DeepSeek Harness\resources\app.asar')
data = asar.read_bytes()
needle = b'data-phase'
start = 0
hits = 0
while hits < 4:
    i = data.find(needle, start)
    if i < 0:
        break
    hits += 1
    lo = max(0, i - 160)
    hi = min(len(data), i + 200)
    print(f'--- hit {hits} ---')
    print(data[lo:hi].decode('utf-8', 'replace').replace('\n', ' '))
    start = i + 1
print('hits:', hits)
