"""Compare scientific JSON, ignoring incidental stdout timing. No computation rerun."""
import json
import sys
from pathlib import Path
p = Path(sys.argv[1])
text = p.read_text()
marker = '===CERTIFICATE_JSON==='
if text.count(marker) != 1:
    raise ValueError('Expected exactly one scientific certificate')
actual = json.loads(text.split(marker)[1])
expected = json.loads(Path(__file__).with_name('certificado_historico.json').read_text())
if actual != expected:
    raise ValueError('Scientific certificate differs from the historical certificate')
print('PASS: exact scientific certificate equality; timing ignored')
