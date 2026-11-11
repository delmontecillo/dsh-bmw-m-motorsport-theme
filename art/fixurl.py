import base64
import pathlib

pkg = pathlib.Path(r'C:\Users\admin\dsh-bmw-m-motorsport-theme')
js = (pkg / 'client.js').read_text(encoding='utf-8')
uri = 'data:image/png;base64,' + base64.b64encode((pkg / 'art' / 'logo-lockup.png').read_bytes()).decode('ascii')
marker = '__BMW_M_LOGO_URI__'

js = js.replace(uri, marker)
old = 'background-image:\n          ${LOGO_URI},'
new = 'background-image:\n          url("${LOGO_URI}"),'
print('css anchor found:', js.count(old))
js = js.replace(old, new)
js = js.replace(marker, uri)
(pkg / 'client.js').write_text(js, encoding='utf-8')

check = (pkg / 'client.js').read_text(encoding='utf-8')
print('url wrapper present:', 'url("data:image/png;base64,' in check)
print('bare data uri left:', '\n          data:image/png;base64,' in check)
print('bytes:', len(check.encode('utf-8')))
