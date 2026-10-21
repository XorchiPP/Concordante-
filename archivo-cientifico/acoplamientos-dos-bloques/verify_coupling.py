#!/usr/bin/env python3
"""Exact finite audit for block-projective Haar couplings. Python stdlib only.

Concordante, copyright 2026. All rights reserved.
Not a physical model validation or a replacement for the proof in REPORT.md.
"""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKS = {}


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS[name] = CHECKS.get(name, 0) + 1


def rates(n, m, c, d, theta):
    """Per-displacement rates, including q(0,0)=0 as a convention."""
    M, N = 1 << n, 1 << m
    alpha = c / M - (N - 1) * theta / (M * N)
    beta = d / N - (M - 1) * theta / (M * N)
    gamma = theta / (M * N)
    return {(u, v): (gamma if u and v else alpha if u else beta if v else F(0))
            for u in range(M) for v in range(N)}


def block_average_expansion(n, m, c, d, theta):
    """Independent construction by three reset events; includes diagonal."""
    M, N = 1 << n, 1 << m
    out = {(u, v): F(0) for u in range(M) for v in range(N)}
    for u in range(M):
        out[u, 0] += (c - theta) / M
    for v in range(N):
        out[0, v] += (d - theta) / N
    for uv in out:
        out[uv] += theta / (M * N)
    out[0, 0] -= c + d - theta
    return out


def eigenvalue(q, a, b):
    return sum(rate * ((-1 if ((a & u).bit_count() + (b & v).bit_count()) % 2 else 1) - 1)
               for (u, v), rate in q.items())


def surjections(n, r):
    """Enumerate every linear map by its n columns and retain full image."""
    for columns in itertools.product(range(1 << r), repeat=n):
        image = []
        for x in range(1 << n):
            y = 0
            for i, col in enumerate(columns):
                if x >> i & 1:
                    y ^= col
            image.append(y)
        if len(set(image)) == 1 << r:
            yield image


def projected_rates(q, pi, rho):
    out = {(a, b): F(0) for a in sorted(set(pi)) for b in sorted(set(rho))}
    for (u, v), value in q.items():
        if pi[u] or rho[v]:
            out[pi[u], rho[v]] += value
    return out


def reachable(q):
    """Exact support connectivity by XOR reachability, not spectral inference."""
    support = [x for x, rate in q.items() if rate > 0]
    reached = {(0, 0)}
    todo = [(0, 0)]
    while todo:
        a, b = todo.pop()
        for u, v in support:
            y = (a ^ u, b ^ v)
            if y not in reached:
                reached.add(y)
                todo.append(y)
    return len(reached)


def main():
    family = [(F(1), F(1), F(0)), (F(1), F(1), F(1, 2)),
              (F(1), F(1), F(1)), (F(2), F(1), F(1)),
              (F(2, 3), F(3, 2), F(1, 3)), (F(0), F(1), F(0)),
              (F(0), F(0), F(0))]
    # Every displacement and every Fourier character, n,m = 1,...,4.
    for n, m in itertools.product(range(1, 5), repeat=2):
        M, N = 1 << n, 1 << m
        for c, d, theta in family:
            q = rates(n, m, c, d, theta)
            check('nonnegative_off_diagonal', all(v >= 0 for v in q.values()))
            states = list(q)
            check('symmetric_generator_entries',
                  all(q[x[0] ^ y[0], x[1] ^ y[1]] == q[y[0] ^ x[0], y[1] ^ x[1]]
                      for x in states for y in states))
            reset = block_average_expansion(n, m, c, d, theta)
            check('generator_reset_identity', all(q[x] == reset[x] for x in q if x != (0, 0)))
            check('zero_row_sum', reset[0, 0] == -sum(q.values()))
            for u in range(1, M):
                check('first_marginal', sum(q[u, v] for v in range(N)) == c / M)
            for v in range(1, N):
                check('second_marginal', sum(q[u, v] for u in range(M)) == d / N)
            for a, b in itertools.product(range(M), range(N)):
                expected = -(c + d - theta) if a and b else -c if a else -d if b else F(0)
                check('all_Fourier_eigenvalues', eigenvalue(q, a, b) == expected)
    # Exhaust all separate proper quotient maps for n,m <= 3. Their
    # compositions cover arbitrary pairs of proper quotient maps.
    quotient_counts = {}
    for n, r in [(2, 1), (3, 1), (3, 2)]:
        maps = list(surjections(n, r))
        quotient_counts[f'{n}->{r}'] = len(maps)
        for m in range(1, 4):
            for c, d, theta in family:
                for pi in maps:
                    id_m = list(range(1 << m))
                    check('quotient_first_block', projected_rates(rates(n, m, c, d, theta), pi, id_m)
                          == rates(r, m, c, d, theta))
                    check('quotient_second_block', projected_rates(rates(m, n, c, d, theta), id_m, pi)
                          == rates(m, r, c, d, theta))
    check('surjection_enumerator', quotient_counts == {'2->1': 3, '3->1': 7, '3->2': 42})
    # The finite positivity boundary is checked on an exact rational grid,
    # including two deliberately inadmissible points beyond each boundary.
    finite_cases = 0
    for n, m in itertools.product(range(1, 5), repeat=2):
        M, N = 1 << n, 1 << m
        for c, d in [(F(1), F(1)), (F(2), F(1)), (F(2, 3), F(3, 2)), (F(0), F(1))]:
            bound = min(c * N / (N - 1), d * M / (M - 1))
            for k in range(-1, 7):
                theta = bound * k / 4 if bound else F(k, 4)
                positive = all(v >= 0 for v in rates(n, m, c, d, theta).values())
                check('finite_interval_equivalence', positive == (0 <= theta <= bound))
                finite_cases += 1
    # Minimal irreducible counterexample: valid 2x2, impossible 4x4.
    q11 = rates(1, 1, F(1), F(1), F(3, 2))
    q22 = rates(2, 2, F(1), F(1), F(3, 2))
    check('counterexample_small_positive', [q11[1, 0], q11[0, 1], q11[1, 1]] == [F(1, 8), F(1, 8), F(3, 8)])
    check('counterexample_irreducible', reachable(q11) == 4)
    check('counterexample_extension_negative', q22[1, 0] == q22[0, 1] == F(-1, 32))
    check('counterexample_joint_eigenvalue', eigenvalue(q11, 1, 1) == F(-1, 2))
    check('finite_endpoint_not_irreducible', reachable(rates(1, 1, F(1), F(1), F(2))) == 2)
    # Quantitative coarse-level extendibility: dimension D allows theta <=
    # 1/(1-2^-D) for equal unit reset clocks. Cases cross each first failure.
    witness_levels = []
    for D in range(1, 5):
        top, next_top = F(1, 1 - F(1, 1 << D)), F(1, 1 - F(1, 1 << (D + 1)))
        theta = (top + next_top) / 2
        check('truncated_family_positive', all(v >= 0 for n in range(1, D + 1) for m in range(1, D + 1)
                                               for v in rates(n, m, F(1), F(1), theta).values()))
        check('next_level_obstruction', rates(D + 1, D + 1, F(1), F(1), theta)[1, 0] < 0)
        witness_levels.append({'last_allowed_dimension': D, 'theta': str(theta)})
    # Full GL invariance at dimension 2 forces alpha=beta=gamma, which with
    # prescribed unit marginal clocks holds iff theta=1 on this grid.
    gl2 = list(surjections(2, 2))
    for theta in map(F, [0, F(1, 2), 1, F(3, 2), 2]):
        q = rates(1, 1, F(1), F(1), theta)
        invariant = all(q[x & 1, x >> 1] == q[pi[x] & 1, pi[x] >> 1]
                        for pi in gl2 for x in range(4))
        check('full_GL_selector', invariant == (theta == 1))
    result = {
        'id': 'two-block-projective-couplings',
        'status': 'PASS', 'arithmetic': 'exact Python fractions.Fraction and integers',
        'assertions': CHECKS, 'total_assertions': sum(CHECKS.values()),
        'bounds': {'spectra': 'all characters and displacements for 1<=n,m<=4, seven specified clocks',
                   'quotients': 'all separate proper linear surjections for 1<=target<source<=3, seven specified clocks',
                   'finite_interval_cases': finite_cases},
        'surjection_counts': quotient_counts,
        'counterexample': {'M': 2, 'N': 2, 'c': '1', 'd': '1', 'theta': '3/2',
                           'alpha': '1/8', 'beta': '1/8', 'gamma': '3/8', 'joint_decay': '1/2',
                           'at_M_N_4_alpha_beta': '-1/32', 'at_M_N_4_gamma': '3/32'},
        'truncated_extension_witnesses': witness_levels,
        'non_claims': ['The finite run does not prove the all-dimensional theorem.',
                       'No physical principle, derivation from a physical principle, or empirical fit is established.',
                       'The factorization and block-equivariant convolution contract are assumed.']}
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    (ROOT / 'certificate.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
