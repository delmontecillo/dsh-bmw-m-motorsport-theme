import pathlib

pkg = pathlib.Path(r'C:\Users\admin\dsh-bmw-m-motorsport-theme')
js = (pkg / 'client.js').read_text(encoding='utf-8')

i = js.find('const LOGO_URI')
print('const start:', js[i:i + 60])
print('const end:', js[js.find("'", i + 40) - 30:js.find("'", i + 40) + 1][-40:])

j = js.find('background-image:')
print('--- css ---')
print(js[j - 260:j + 300])
print('--- ---')
print('placeholder left:', js.count('__BMW_M_LOGO_URI__'))
print('url interpolation:', js.count('url("${LOGO_URI}")'))
print('lines:', js.count('\n'))
