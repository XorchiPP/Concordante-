"""Compare a reproduction with the documented exact and floating-point outputs."""
import json
import sys
from pathlib import Path

expected = json.loads(Path(__file__).with_name('certificado_historico.json').read_text())
actual = json.loads(Path(sys.argv[1]).read_text())
tolerance = 3e-11
max_difference = 0.0

def compare(a, b, path='root'):
    global max_difference
    if isinstance(a, dict):
        if not isinstance(b, dict) or a.keys() != b.keys():
            raise ValueError(path + ': different keys')
        for key in a:
            compare(a[key], b[key], path + '/' + key)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            raise ValueError(path + ': different list structure')
        for index, (x, y) in enumerate(zip(a, b)):
            compare(x, y, path + '/' + str(index))
    elif isinstance(a, float):
        difference = abs(a-b)
        if not difference <= tolerance:
            raise ValueError(path + ': floating-point tolerance exceeded')
        max_difference = max(max_difference, difference)
    elif type(a) != type(b) or a != b:
        raise ValueError(path + ': exact value differs')

compare(expected, actual)
print(json.dumps({'status':'PASS','exact_fields_equal':True,
                  'floating_absolute_tolerance':tolerance,
                  'maximum_absolute_difference':max_difference},sort_keys=True))
