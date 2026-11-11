import json
import pathlib

pkg = pathlib.Path(r'C:\Users\admin\dsh-bmw-m-motorsport-theme')
s = (pkg / 'client.js').read_text(encoding='utf-8')
print('roundel data uri:', "const ROUNDEL_URI = 'data:image/png;base64," in s)
print('greeting code left:', 'GreetingLine' in s)
print('greeting css left:', 'bmw-greeting' in s)
print('team label key:', "'team.label': 'Into the unknown'" in s)
print('team tracking token:', '--bmw-team-tracking' in s)
print('brandMark hide left:', 'brandMark' in s)

p = json.loads((pkg / 'package.json').read_text(encoding='utf-8'))
p['version'] = '1.6.0'
p['description'] = (
    'BMW M Motorsport theme for DeepSeek Harness: Warsteiner-liveried M3 white, '
    'royal blue, azure, cyan, red, checkered flags, the BMW Motorsport banner, the '
    'supplied roundel on the rail, and the INTO THE UNKNOWN banner line.'
)
(pkg / 'package.json').write_text(json.dumps(p, indent=2) + '\n', encoding='utf-8')
print('version', p['version'])
