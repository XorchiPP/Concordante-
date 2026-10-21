# Escala de difusión, acciones espectrales y toro triangulado

Concordante Lab · Xorch. © 2026. Todos los derechos reservados.

Edición del informe técnico del 21 de octubre de 2026. Argumentos exactos y cálculos históricos se distinguen en cada apartado. El texto técnico completo se conserva en inglés; la guía y el explorador están en español.

## D1 | The proposed exact heat-kernel identity is false

Let `C_m^3` denote the cubic periodic graph on `(Z/m)^3` with six cardinal nearest-neighbor moves. Its combinatorial Laplacian eigenvalues are

`lambda_m(k) = sum_{j=1}^{3} [2 - 2 cos(2 pi k_j/m)]`.

For corresponding low Fourier modes of the 16-to-8 block quotient, **each coordinate contribution** satisfies

`lambda_8,j(k) = 4 cos²(pi k_j/16) lambda_16,j(k)`.

This is asymptotic to a factor four only when `k_j/16` is small. No scalar `lambda_8(k) = 4 lambda_16(k)` identity holds generally. Furthermore, `K_8³(0)=512` and `K_16³(0)=4096`; thus the full traces cannot obey `K_8³(t)=K_16³(4t)`. Dividing by vertex count changes the spectral density, not the spectral dimension, and still does not make the heat kernels identical.

If effective edge lengths are `a_fine=1` and `a_coarse=2` while the physical torus side is held fixed, *matching physical diffusion time* `t_phys=t_graph a²` requires `t_coarse=t_fine/4`.

| Fine `t` (16³) | Coarse `t/4` (8³) | Fine `d_s` | Coarse `d_s` | Coarse minus fine |
|---:|---:|---:|---:|---:|
| 6 | 1.5 | 3.063234 | 3.408149 | +0.344915 |
| 12 | 3 | 2.721674 | 2.830313 | +0.108639 |
| 24 | 6 | 1.079516 | 1.185343 | +0.105827 |
| 48 | 12 | 0.058713 | 0.074557 | +0.015844 |

**Result D1:** no exact collapse. The coarse and fine systems use different UV dispersions, and the finite torus eventually reaches its mixing scale. A continuum-rescaled limit may recover spectral convergence (classical discrete-torus theory). Closure under the particular block map proves neither an exact RG fixed point nor attraction from arbitrary initial graph families.

Véase [el explorador](../explorador.html), con tiempos físicos emparejados.

## D2 | Heat-trace action detects the matched graphs, but local motifs do too

Recall from `comparación de geometrías`: 4,096 vertices, 12,288 edges, degree six, and idleness-zero Ollivier curvature zero on every edge for both:

- Triangular two-torus `(Z/64)^2` with moves ±(1,0), ±(0,1), ±(1,1).
- Cubic periodic graph `(Z/16)^3` with moves ±e1,±e2,±e3; its **unfilled clique complex is one-dimensional**.

The heat trace `S_t(G)=K_G(t)=Tr exp(-t L)` is mathematically defined for any finite graph, but this alone **is not a proof of a Connes–Chamseddine spectral triple** or the gravitational action.

| `t` | `K_triangular` | `K_cubic` | Difference |
|---:|---:|---:|---:|
| 0.1 | 2,320.7836 | 2,316.2192 | +4.5643 |
| 0.5 | 488.5009 | 413.8523 | +74.6486 |
| 1 | 208.8308 | 120.2709 | +88.5599 |
| 2 | 98.4722 | 36.3315 | +62.1408 |
| 6 | 31.8150 | 6.4662 | +25.3488 |

All 13 probed `t>0` in the certificate give `K_triangular > K_cubic`. **No universal all-t ordering is claimed from this finite scan.**

A simpler discriminator exists. The triangular two-torus has **8,192 triangular 3-cycles**, and the cubic graph has none. Since for a d-regular simple graph `L=d I-A`, `Tr(A³)=6 T` where `T` is the number of triangles. When two graphs share `n` and `d`, with their first two Laplacian spectral moments equal, Taylor expansion yields

`Delta K(t) = Delta T * t³ + O(t⁴) = 8192 t³ + O(t⁴)`.

**Corrected no-go scope:** no functional depending *only* on matched quantities `(n, E, degree distribution, per-edge idleness-zero Ollivier curvature)` can distinguish this pair. A local triangle-counting functional can. It is mathematically false to infer that *no local action* can distinguish them.

For a fixed graph, `K(t)` decreases monotonically in `t>0` and increases with the chosen cutoff `Lambda=1/sqrt(t)`; minimizing the cutoff itself is a trivial boundary problem. Minimizing graph selection at a **fixed declared scale** is meaningful, but lacks a derived reason to prefer spatial dimension three.

## D3 | Finite sampled Boltzmann library is not a phase transition

Controls: triangular 2-torus side 8, cubic graph side 4, plus **80 seeded simple connected six-regular random graphs** from `networkx.random_regular_graph(6,64,seed=0..79)`. Every candidate has exactly `n=64`, `E=192` and uniform degree six. For action `K(1)=Tr exp(-L)`:

- Triangular torus: `3.2649584`.
- Cubic periodic graph: `2.1416318`.
- Random controls: minimum `2.0050563`, median `2.0708793`, maximum `2.1236200`.

All 80 sampled random controls beat both periodic lattices under **minimization** of this heat-trace action. This result depends on the specified ensemble, size, and action time; it is neither an exact optimization over all regular graphs nor a proof that expanders always win.

At `t=1`, the random controls show `d_s` in `[2.944923, 3.055096]` (median `3.008770`), but they do **not** have a demonstrated three-dimensional plateau: at `t=0.5` the medians are around `3.256`, falling to about `0.715` by `t=2` due to finite-size mixing. A *one-time* value near three therefore easily misclassifies nonmanifold expander-like graphs.

For the finite library of exactly 82 candidate graphs, normalized reweighting `p_beta(G)∝exp(-beta K_G(1))` yields `P(random pool)≈0.99436` at `beta=10`. This is a toy sampling measure whose prior gives random samples an eighty-to-two numerical advantage; it cannot be interpreted as an actual graph-counting Boltzmann ensemble. For every finite collection, its partition function is analytic in beta, so there is no thermodynamic singularity. The correct next task is an increasing-size ensemble with a reproducible graph prior and a declared coarse-graining kernel.

## D4 | Verified three-dimensional **flag** torus

Use `V=(Z/m)^3`, `m≥5`. Define undirected compatibility edges by the seven positive displacements `S={(a,b,c):a,b,c∈{0,1}, not all zero}` and their inverses. These are exactly the edges of the periodic Freudenthal/Kuhn subdivision of cubes into six tetrahedra. Take the flag (clique) complex, with no embedding or edge lengths supplied to the code.

At `m=5`, independent graph-clique enumeration produces

`(f0,f1,f2,f3)=(125,875,1500,750)`, maximum simplex dimension exactly 3, `Euler=0`.

Boundary-matrix reductions over `F2` produce

`rank(∂1)=124`, `rank(∂2)=748`, `rank(∂3)=749`, and

**`(b0,b1,b2,b3)=(1,3,3,1)`**.

The link of one vertex is a connected closed triangulated surface with `(14,36,24)` vertices, edges and triangles, Euler characteristic 2; its edges lie in exactly two faces and all its vertex links are circles. It is a 2-sphere. Translation symmetry proves the same for every vertex. Consequently the complex is a closed combinatorial 3-manifold. Together with the explicitly periodic cube-subdivision construction, this identifies the underlying PL space with the three-torus. Homology **alone** would not prove that homeomorphism; the explicit triangulated construction supplies the missing topology.

The idleness-zero Ollivier curvature was also solved by exact-formulated **numerical** optimal transport on each of the seven edge-direction orbits at `m=5`, all equal to zero to numerical tolerance. This is not being promoted as a symbolic all-m curvature proof.

A general `m≥5` construction has `n=m³`, regular degree `14` and simplex counts `(n,7n,12n,6n)`. The Fourier-Laplacian eigenvalue formula is

`lambda=14-2[cos p+cos q+cos r+cos(p+q)+cos(p+r)+cos(q+r)+cos(p+q+r)]`.

Its low-momentum quadratic form has matrix

`Q = [[4,2,2],[2,4,2],[2,2,4]]`, strictly positive of rank three.

Finite-size diffusion evidence: `m=16`, `d_s(2)=3.0893`, `d_s(3)=3.0102`; `m=24`, `d_s(4)=3.0427`, `d_s(6)=3.0086`. These values agree with a three-dimensional intermediate scaling regime. The series still saturates and tends to zero at very large graph times for any fixed m. Véase [el explorador interactivo](../explorador.html).

**Comparison guard:** the 3D flag torus has degree 14, unlike the 2D triangulated torus degree 6. In fact, any degree-regular closed simplicial triangulation of a 2-torus has degree **exactly 6**, since Euler `V−E+F=0` and `3F=2E` imply `E=3V`. Therefore one cannot simply demand that these specific regular 2D toroidal triangulations match the degree-14 comparator without changing the admissible class. The original degree/curvature-matched no-go remains valid for its specific graph class; D4 is a structurally fairer manifold benchmark, not a new matched-degree no-go.

## Important distinctions retained

1. **Regge versus Ollivier:** Regge's Einstein–Hilbert discretization requires a simplicial metric: hinge deficit angles times `(d−2)`-dimensional **hinge volume** (not simply dual volume), with suitable dimensional constants. Ollivier curvature probes metric transport and cannot be substituted without a justified continuum limiting statement.
2. **Local versus global:** equality of one selected set of local invariants does not imply equality of every local graph statistic. The corrected `D2` Taylor certificate supplies an explicit low-order local discriminator.
3. **Spectral triple versus a numerical triple:** `spectrum, homology, scale` is a useful descriptor but **not** definitionally a spectral triple `(A,H,D)`. The appropriate Dirac operator, representation and first-order structure must be specified.
4. **Three dimensions versus selection:** examples of 3D graph diffusion and 3D manifold topology do not exhibit uniqueness or attraction to `d=3`.
5. **RG versus time:** blocking is a change of resolution, not intrinsically physical time. Concordante's existing `estudio previo de entropía y resolución` proves that coarse hidden-information entropy does not by itself give a thermodynamic arrow; Markov dynamics and equilibrium conditions are additional input.
6. **Falsifiability:** absence of a 3D fixed point in one specified ensemble/action/RG scheme falsifies **that scheme**. It cannot logically rule out `any natural action and any RG flow` through a finite computation. A genuine claim needs an explicitly delimited admissible class.

## Proposed next experiment: `siguiente estudio de selección`

Define a growing series of finite *flag-manifold-admissible* ensembles and explicit block/rewrite Markov kernels, then seek stable non-UV, non-mixing spectral plateaux under a physical-time matching rule. Compare 2D and 3D families as blind controls; apply no `|d_s−3|` preference in the action. Record posterior class probabilities after adjusting for graph prior and counting multiplicities. Introduce a **predeclared** fixed-point detection tolerance/window and independent falsifier on topology or holonomy. Keep action selection and causal/entropy arrow as separate hypotheses.

## Reproducción y bibliografía

Se entregan el programa `verificar.py`, el certificado histórico y los resultados CSV. El explorador español reproduce las series históricas incrustadas. Véanse ../VERIFICACION.md y ../BIBLIOGRAFIA.md para ejecución, fuentes y alcance.
