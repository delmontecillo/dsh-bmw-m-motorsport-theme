import base64
import pathlib

pkg = pathlib.Path(r'C:\Users\admin\dsh-bmw-m-motorsport-theme')
js = (pkg / 'client.js').read_text(encoding='utf-8')
png = (pkg / 'art' / 'logo-lockup.png').read_bytes()
uri = 'data:image/png;base64,' + base64.b64encode(png).decode('ascii')
marker = '__BMW_M_LOGO_URI__'
print('placeholder occurrences:', js.count(marker))
js = js.replace(marker, uri)
(pkg / 'client.js').write_text(js, encoding='utf-8')
print('client.js bytes:', len(js.encode('utf-8')))
print('data uri chars:', len(uri))
print('placeholder left:', js.count(marker))
