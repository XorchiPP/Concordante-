#!/usr/bin/env python3
"""Controles exactos de cascarones y vecinos primos.
Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
Edición acotada: conserva las cinco funciones de comprobación originales.
"""
from itertools import product
from math import comb
import json

def universal_shell(n, A8=0):
    """Número de vectores de norma cuadrada 4 de M(C) si d(C)>=8.
    Si d(C)>=12, A8=0 y queda sólo el cascarón sqrt(2) D_n.
    """
    return 4 * comb(n, 2) + 128 * A8


def mandatory_survivors(n, p):
    assert p % 2 and p >= 3
    classes=(p+1)//2  # clases a ~ -a en F_p
    q,r=divmod(n, classes)
    pairs=(classes-r)*comb(q, 2) + r*comb(q+1, 2)
    return 2 * pairs  # como mínimo ±v por pareja colisionada


def is_prime(p):
    return p >= 2 and all(p % a for a in range(2, int(p**0.5)+1))


def first_unobstructed_prime(n):
    p=2*n-1
    while not is_prime(p):
        p+=1
    return p


def exhaustive_pigeonhole_small():
    counts={}
    for p in (3,5,7):
        n=(p+1)//2+1
        num=0
        for vec in product(range(p), repeat=n):
            keys=[min(v, p-v) for v in vec]
            assert len(set(keys))<n
            # Entre las cuatro elecciones de signos ±e_i±e_j
            # alguna ortogonalidad mod p es inevitable.
            pairs=sum(keys[i]==keys[j] for i in range(n) for j in range(i+1,n))
            assert pairs>=1
            num+=1
        counts[str(p)]=num
    return counts


def main():
    assert universal_shell(24,759)==98256
    assert universal_shell(32,620)==81344
    assert universal_shell(48,0)==4512
    assert universal_shell(72,0)==10224
    survivors={str(n):{str(p):mandatory_survivors(n,p) for p in (3,5,7)} for n in (48,72)}
    assert survivors['48']=={'3':1104,'5':720,'7':528}
    assert survivors['72']=={'3':2520,'5':1656,'7':1224}
    primes={str(n):first_unobstructed_prime(n) for n in (48,72)}
    assert primes=={'48':97,'72':149}
    tests=exhaustive_pigeonhole_small()
    assert tests=={'3':27,'5':625,'7':16807}
    result=dict(
        M_C_norm4_shells={'24_Golay':98256,'32_RM25':81344,'48_any_d_ge_12':4512,'72_any_d_ge_16':10224},
        mandatory_shell_survivors_one_step=survivors,
        prime_sieve_threshold=primes,
        finite_residue_exhaustion_cases=tests)
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
