#!/usr/bin/env python3
"""Exact, local audit of boundary-indistinguishable weighted networks.

Dependency: SymPy. Run: python verify_boundary_gauge.py
Only writes audit_results.json beside this script; no network access is used.
All quantities are rational or exact polynomials, never rounded for assertions.
"""
from itertools import combinations, permutations
import json
from pathlib import Path
import sympy as sp

EDGES = list(combinations(range(5), 2))
Z5 = sp.zeros(5)
ONE = sp.ones(5, 1)
s = sp.symbols('s', nonnegative=True)
x = sp.symbols('x')


def edge_laplacian(i, j):
    b = sp.eye(5)[:, i] - sp.eye(5)[:, j]
    return b * b.T


def laplacian(weights):
    return sum((w * edge_laplacian(i, j) for (i, j), w in zip(EDGES, weights)), Z5.copy())


def clean(A):
    return A.applyfunc(sp.cancel)


def iszero(A):
    return clean(A) == sp.zeros(*A.shape)


def transfer(L, M, B=(0, 1)):
    I = tuple(i for i in range(5) if i not in B)
    C = L.extract(B, I)
    K = L.extract(I, I)
    Mi = M.extract(I, I)
    return clean(L.extract(B, B) - C * (K + s * Mi).inv() * C.T)


def kron(L, B=(0, 1, 2)):
    I = tuple(i for i in range(5) if i not in B)
    return clean(L.extract(B, B) - L.extract(B, I) * L.extract(I, I).inv() * L.extract(I, B))


def enc(v):
    if isinstance(v, sp.MatrixBase):
        return [[str(a) for a in row] for row in v.tolist()]
    if isinstance(v, dict):
        return {k: enc(a) for k, a in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(a) for a in v]
    if isinstance(v, (bool, int, str)) or v is None:
        return v
    return str(v)


def audit(name, M, L, S, require_activity):
    T = sp.diag(sp.eye(2), S)
    H = clean(T.T * L * T)
    Mi = M[2:, 2:]
    assert iszero(S * sp.ones(3, 1) - sp.ones(3, 1))
    assert iszero(T.T * M * T - M)
    assert iszero(L * ONE) and iszero(H * ONE)
    assert L == L.T and H == H.T
    weights = [-L[i, j] for i, j in EDGES]
    weights2 = [-H[i, j] for i, j in EDGES]
    assert all(w > 0 for w in weights + weights2)
    assert L != H
    # Exhaustive weighted-graph isomorphism test, including boundary-moving permutations.
    matches = [p for p in permutations(range(5)) if L.extract(p, p) == H]
    assert not matches
    assert sorted(L.diagonal()) != sorted(H.diagonal())
    F, F2 = transfer(L, M), transfer(H, M)
    assert iszero(F - F2)
    det_i = sp.factor((L[2:, 2:] + s * Mi).det())
    assert all(a > 0 for a in sp.Poly(det_i, s).all_coeffs())
    # Q is a row Markov generator; exp(t Q) is its transition kernel.
    Q, Q2 = -M.inv() * L, -M.inv() * H
    assert iszero(Q2 - T.inv() * Q * T)
    assert iszero(Q * ONE) and iszero(Q2 * ONE)
    m = M * ONE
    pi = m / sum(m)
    assert iszero(pi.T * Q) and iszero(pi.T * Q2)
    assert iszero(sp.diag(*pi) * Q - (sp.diag(*pi) * Q).T)
    assert iszero(sp.diag(*pi) * Q2 - (sp.diag(*pi) * Q2).T)
    for i, j in EDGES:
        assert Q[i, j] / Q[j, i] == Q2[i, j] / Q2[j, i] == m[j] / m[i]
    # Exact similarity proves the exponential identity for every t; these are extra checks.
    for k in range(13):
        assert iszero((Q**k)[:2, :2] - (Q2**k)[:2, :2])
    spectrum = (M.inv() * L).charpoly(x).as_expr()
    assert spectrum == (M.inv() * H).charpoly(x).as_expr()
    obs = []
    for A in (L, H):
        C = A[:2, 2:]
        Kdyn = Mi.inv() * A[2:, 2:]
        O = C.col_join(C * Kdyn).col_join(C * Kdyn**2)
        U = Mi.inv() * C.T
        ctr = U.row_join(Kdyn * U).row_join(Kdyn**2 * U)
        assert O.rank() == 3 and ctr.rank() == 3
        obs.append({'rank': O.rank(), 'first_three_rows_minor': O[:3, :].det(), 'matrix': O})
    activity = -sum(pi[i] * Q[i, i] for i in range(5))
    activity2 = -sum(pi[i] * Q2[i, i] for i in range(5))
    assert activity == sp.trace(L) / sum(m)
    assert activity2 == sp.trace(H) / sum(m)
    assert (activity == activity2) == require_activity
    D, D2 = kron(L), kron(H)
    difference = clean(D - D2)
    assert D[2, 2] != D2[2, 2]
    # u_B=(0,0,1), interior harmonic equilibration, gives distinct measured currents.
    uB = sp.Matrix([0, 0, 1])
    current, current2 = D * uB, D2 * uB
    assert current[2] == D[2, 2] and current2[2] == D2[2, 2]
    ordinary_heat_second_derivative_difference = (L**2 - H**2)[:2, :2]
    if M == sp.eye(5):
        assert iszero(T.T * T - sp.eye(5))
        assert L.charpoly(x).as_expr() == H.charpoly(x).as_expr()
        assert iszero(ordinary_heat_second_derivative_difference)
    else:
        assert not iszero(ordinary_heat_second_derivative_difference)
        assert L.charpoly(x).as_expr() != H.charpoly(x).as_expr()
    return {
        'name': name, 'M': M, 'L': L, 'S': S, 'L2': H,
        'weights_L': weights, 'weights_L2': weights2,
        'degrees_L': list(L.diagonal()), 'degrees_L2': list(H.diagonal()),
        'all_weights_positive': True, 'permutation_isomorphisms': matches,
        'transfer': F, 'interior_pencil_determinant': det_i,
        'observability': obs, 'stationary_probability': pi,
        'spectrum_polynomial_MinvL': spectrum,
        'stationary_jump_activity_L': activity,
        'stationary_jump_activity_L2': activity2,
        'activity_change_L2_minus_L': sp.factor(activity2 - activity),
        'common_uniform_mean_exit_rate': sp.trace(M.inv() * L) / 5,
        'third_boundary_response_L': D, 'third_boundary_response_L2': D2,
        'third_boundary_u001_current_L': current,
        'third_boundary_u001_current_L2': current2,
        'third_boundary_current2_difference_L_minus_L2': difference[2, 2],
        'ordinary_heat_second_derivative_difference': ordinary_heat_second_derivative_difference,
        'all_assertions_passed': True,
    }


def main():
    m = sp.Matrix([1, 2, 3, 4, 5])
    M = sp.diag(*m)
    Mi = M[2:, 2:]
    v = sp.Matrix([1, -2, 1])
    S = sp.eye(3) - 2 * v * (v.T * Mi) / (v.T * Mi * v)[0]
    L0 = 15 * M - m * m.T
    L = L0 + 11 * edge_laplacian(0, 2) + 13 * edge_laplacian(0, 4) + edge_laplacian(2, 4)
    reports = [audit('principal_distinct_capacities_matched_activity', M, L, S, True)]
    L = laplacian([5, 6, 5, 4, 4, 7, 5, 5, 6, 4])
    S = sp.Matrix([[6, -2, 3], [-2, 3, 6], [3, 6, -2]]) / 7
    reports.append(audit('secondary_equal_capacities', sp.eye(5), L, S, True))
    path = Path(__file__).resolve().parent / 'audit_results.json'
    path.write_text(json.dumps(enc(reports), indent=2, ensure_ascii=False) + '\n')
    for result in reports:
        print(result['name'] + ': PASS')
        print('  Observability minors:', ', '.join(str(a['first_three_rows_minor']) for a in result['observability']))
        print('  Stationary jump activities:', result['stationary_jump_activity_L'], result['stationary_jump_activity_L2'])
        print('  Third-boundary current at node 2:', result['third_boundary_u001_current_L'][2], result['third_boundary_u001_current_L2'][2])
    print('Exact report:', path.name)


if __name__ == '__main__':
    main()
