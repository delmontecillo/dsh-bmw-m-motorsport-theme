import base64
import pathlib

pkg = pathlib.Path(r'C:\Users\admin\dsh-bmw-m-motorsport-theme')
js = (pkg / 'client.js').read_text(encoding='utf-8')

if 'ROUNDEL_URI' not in js:
    start = js.index('const LOGO_URI = ')
    end = js.index('\n', start)
    insert = (
        '\n\n    /** The supplied BMW roundel, cropped to a square plate for the rail. */\n'
        "    const ROUNDEL_URI = '__BMW_M_ROUNDEL_URI__';"
    )
    js = js[:end] + insert + js[end:]

uri = 'data:image/png;base64,' + base64.b64encode((pkg / 'art' / 'roundel.png').read_bytes()).decode('ascii')
marker = '__BMW_M_ROUNDEL_URI__'
print('placeholder count:', js.count(marker))
js = js.replace(marker, uri)
(pkg / 'client.js').write_text(js, encoding='utf-8')
print('roundel embedded:', uri[:40] + '...', len(uri))
print('bytes:', len(js.encode('utf-8')))
