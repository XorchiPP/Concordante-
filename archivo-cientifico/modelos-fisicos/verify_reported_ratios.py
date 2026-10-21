#!/usr/bin/env python3
"""Only checks rounded table arithmetic; does NOT regenerate the gauge residual."""
import json
from math import sqrt
from pathlib import Path
rows=[(2,3.8959591467e-4,4.5664944809e-5,.996507,.883253),
      (3,3.1443214983e-4,3.6761861797e-5,.998135,.883332),
      (4,2.56002719497e-4,2.9924184220e-5,.998746,.883276)]
out=[]
for n,error,predictor,cosine,reported in rows:
 ratio=predictor/error
 remaining=sqrt(1+ratio*ratio-2*ratio*cosine)
 assert abs(remaining-reported)<1e-6
 out.append(dict(N=n,predictor_to_error=ratio,remaining_norm_ratio=remaining,reported_remaining=reported))
result=dict(scope='Arithmetic consistency of rounded reported numbers only; no independent numerical residual reproduction.',status='PASS_TABLE_ARITHMETIC',rows=out)
Path(__file__).with_name('reported_ratios.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
