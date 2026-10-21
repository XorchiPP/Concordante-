# Comparación de geometrías mediante curvatura y difusión

Concordante Lab · Xorch. © 2026. Todos los derechos reservados.

Edición del informe técnico del 21 de octubre de 2026. Argumentos exactos y cálculos históricos se distinguen en cada apartado. El texto técnico completo se conserva en inglés; la guía y el explorador están en español.

## Research question

Can a variational selection principle based only on a binary symmetric compatibility graph, especially the proposed sum of Ollivier–Ricci curvatures, distinguish a two-dimensional geometry from a three-dimensional one?

**Result: No, for this particular action, even with state count, edge count, degree, and edge curvature held fixed.** This is a no-go for the specified *candidate selector*, **not** a no-go for variational selection in general.

## Definitions and conventions

A finite undirected, unweighted, connected graph `G=(V,E)` specifies a symmetric compatibility relation. The graph's combinatorial Laplacian is `L=D-A`; for heat time `t>0`,

\[
 K_G(t)=\operatorname{Tr}e^{-tL}=\sum_i e^{-t\lambda_i}, \qquad
 d_{s,G}(t)=2t\,\frac{\sum_i \lambda_i e^{-t\lambda_i}}{\sum_i e^{-t\lambda_i}}.
\]

Dividing `K` by `|V|` makes it a normalized return probability and does **not** change `d_s`. Since the graph is finite and connected, the zero eigenvalue is simple. Therefore `d_s(t)→0` as `t→0` and as `t→∞`. An intermediate near-constant `d_s` is a *finite-scale signature*, not an asymptotic finite-graph dimension.

For each edge `x~y` use the **idleness-zero** Ollivier curvature with measures uniform on each vertex's neighbors:

\[
\kappa(x,y)=1-W_1(\mu_x,\mu_y),\qquad
 S_\kappa[G]=\sum_{\{x,y\}\in E}\kappa(x,y).
\]

`W1` uses unweighted shortest-path distance as its transport cost; edge weights in `S` equal one. Other idleness, measures, weights, or curvature notions give *different* functionals.

## Exact matched comparison at 4,096 states

All connections are provided by periodic discrete generators, so they are input compatibility graphs, **not assumed Euclidean metric spaces**. All subsequent distances/heat kernels are induced by the adjacency relation.

**2D triangular torus** `G₂`: vertices `(Z/64Z)^2`, positive directions `(1,0),(0,1),(1,1)` together with their inverses.

**3D cubic torus graph** `G₃`: vertices `(Z/16Z)^3`, positive directions `(1,0,0),(0,1,0),(0,0,1)` together with inverses.

| Observable | `G₂` | `G₃` |
|---|---:|---:|
| Vertex count | 4,096 | 4,096 |
| Degree of every vertex | 6 | 6 |
| Number of edges | 12,288 | 12,288 |
| Ollivier curvature of every edge | 0 | 0 |
| Signed action `Sκ` | 0 | 0 |
| `d_s(4)` | 2.0452758366 | 3.1085475388 |
| `d_s(6)` | **2.0293114051** | **3.0632343679** |
| `d_s(8)` | 2.0216778858 | 3.0110128855 |
| `Tr(exp(-6L))` | 31.8150087140 | 6.4662208194 |

**No-go for the tested selector:** The invariants `(n, |E|, degree distribution, {κ_e})` are identical while diffusion-dimension profiles differ. Consequently no action depending *only* on those invariants, including `Σκ`, selects one from this pair. This does not rule out an action depending on e.g. the full spectrum, motifs, holonomy, or additional structure.

### Exact curvature proof (not merely floating point)

Both graphs are periodic Cayley graphs. Translating every point of `μ_x` by the edge displacement `s` yields `μ_{x+s}`, with each transported point moving distance exactly one. Therefore `W1≤1`.

For each generating displacement, choose a coordinate on which it changes by `+1`. On the two **local neighborhood supports**, the corresponding unwrapped coordinate function is 1-Lipschitz with respect to shortest-path distance (for the chosen torus side lengths there is no wraparound shortcut between these supports). Its mean increases by exactly one between `μ_x` and `μ_{x+s}`. By Kantorovich duality, `W1≥1`. Hence `W1=1` and **κ=0** for all generator edges and all their translates. The program independently solves the associated 6×6 transportation linear programs for each direction.

The zero-curvature equality is **for the declared idleness-zero Ollivier convention**, not a claim that all graph Ricci curvatures agree.

### Independent Fourier verification of diffusion dimension

Let `p=2πk/m`, `q=2πl/m` and let `r` denote the third Fourier coordinate. The eigenvalues are:

\[
\lambda_{G_2}(p,q)=6-2\cos p-2\cos q-2\cos(p+q),
\]
\[
\lambda_{G_3}(p,q,r)=6-2\cos p-2\cos q-2\cos r.
\]

Their low-momentum expansions are, respectively, a positive definite **rank-2** quadratic form (`2(p²+q²+pq)`) and a **rank-3** quadratic form (`p²+q²+r²`). In the infinite-volume limit followed by the diffusive long-time regime, Gaussian asymptotics imply `K(t)/n ~ constant·t^{-d/2}` for `d=2` and `d=3`, respectively. This is classical periodic-lattice diffusion mathematics.

For an independent small-instance check, `verificar.py` diagonalizes the actual finite graph Laplacian of `C₁₁`, triangular torus side 8, and cubic torus side 5, then compares to Fourier formulas within `1e-10`.

**Topological guard:** The unfilled graph of the cubic torus has no triangular cliques, so its *flag/clique complex* is one-dimensional, despite its three-dimensional diffusive scaling. To model a 3D cell complex, one must include the relevant squares/cubes or an appropriate simplicial triangulation. Spectral dimension alone does not recover topological dimension.

Las curvas interactivas se encuentran en [el explorador](../explorador.html).

## Coarse-graining: what it does and what it cannot select

Define block contraction `π(x_i)=floor(x_i/2)` in each periodic coordinate, and put an edge between two coarse blocks whenever a source edge joins them. Discard loops inside blocks.

Exact adjacency comparison establishes:

* 2D triangular torus `64×64 → 32×32`, **same triangular generator family**;
* 3D cubic torus `16³ → 8³`, **same cubic generator family**;
* 1D cycle `64 → 32`, **same cycle family**.

This is an exact family-closure calculation, **not** a freely chosen or fitted fixed point. Ordinary block contraction on these inputs produces no convergence to a common dimension. The same construction iterates in each separate `d`-dimensional family.

At the *same unrescaled heat time* `t=6`, the coarse cubic graph has `d_s(6)=1.1853429371`, compared with `3.0632343679` before contraction. This dramatic apparent "dimension flow" comes from entering its finite-volume/mixing regime as its side shrinks (`m=16→8`), not from a genuine attractor dimension. Heat time must be renormalized and scaling windows tracked when interpreting coarse-graining flows.

### Operator convention check

On any `k`-regular graph, normalized and combinatorial Laplacians satisfy `L_norm=L/k`, whence

\[
 d_s^{\mathrm{norm}}(t)=d_s^{\mathrm{comb}}(t/k).
\]

`verificar.py` checks this equality numerically at `k=6`. Plotting unrescaled times under different operator conventions can create spurious flow or apparent dimensional differences.

## Direct minimization counterexample to the proposed signed action

All graphs in the first comparison below have **n=10**:

| Graph | Edges | Edge κ | `Sκ=Σκ` |
|---|---:|---:|---:|
| Cycle `C₁₀` | 10 | 0 | 0 |
| Petersen graph | 15 | −1/3 | **−5** |
| Complete `K₁₀` | 45 | 8/9 | 40 |

The Petersen graph beats the flat cycle under **minimization**. It is *not* claimed to be the global minimizer over all connected ten-vertex graphs. The comparison also varies edge count; that motivates the controlled regular comparison below.

At the **same `n=64`, degree `6`, |E|=192`**, three reproducibly seeded random regular graphs beat the flat triangular torus:

| Graph | `Sκ` | `d_s(6)` |
|---|---:|---:|
| Flat triangular torus (side 8) | 0 | 0.07430 |
| Random regular, seed 3 | −78.83333 | 0.000480 |
| Random regular, seed 7 | −73.50000 | 0.000491 |
| Random regular, seed 19 | −78.50000 | 0.000348 |

The near-zero spectral dimensions at `t=6` here indicate fast finite-graph mixing, **not intrinsic zero-dimensional spaces**. The small flat torus has also entered finite-size saturation at this time. These are controls showing that minimizing *raw* signed Ollivier curvature favors some non-manifold-like competitors at fixed size/degree, not evidence about their ultimate long-scale dimension.

## What remains open, and concrete next action

1. Specify a justified **graph ensemble** with fixed `n`, degree distribution, connectivity, and preferably an explicit manifold-likeness/cell-complex constraint. Do not infer a physical ensemble from the compatibility relation alone.
2. Define a **normalized, explicitly scaled action** and compare its minimizers and Gibbs ensembles against random regular/expander controls. Keep curvature, spectrum, topological dimension, and short-cycle counts as separate diagnostics. Do not insert `d_s≈3` as a target term if the aim is to *derive* 3.
3. Track an independently defined **renormalization map** and measure spectral dimension in matched diffusion windows, rescaling physical lengths and time. Test graph sizes and stochastic seeds. A claim of dimension selection needs a basin of attraction, not one graph's plateau.
4. Evaluate whether the same action predicts **new independent observables** rather than merely reproducing a spectral profile used for tuning.

A spectral functional can distinguish the paired 2D and 3D graphs (`K(6)` differs), but the choice of cutoff function, spectral operator, sign, and temperature are new inputs. `D=√L` alone does **not** establish a Connes-style spectral triple, a Yang–Mills action, or their physical interpretation.

### Hamiltonian and time-direction guard

`L=D−A` is the generator of the symmetric continuous-time random walk once *unit transition rates* are declared; a graph does not uniquely determine a physical Hamiltonian. Normalized Laplacians, weighted transitions, onsite potentials, and other self-adjoint local operators remain possible. On a regular graph, `L=kI−A`; the quantum unitaries `e^{-itL}` and `e^{-itA}` yield identical position probabilities for localized initial real states (up to an overall phase and complex conjugation), so a comparison on an irregular graph is essential to separate those choices.

There is also a simple symmetry obstruction for deterministic local time updates: a cycle `C_n` is edge-transitive. A deterministic isomorphism-equivariant map cannot single out **exactly one distinguished edge** from an unmarked cycle, since rotations move every edge. A single-edge rewrite must break symmetry by marks, randomness, asymmetric context, or an external choice; iteration number alone is not a thermodynamic arrow of time.

### Gauge extension guard

For a torus, flat `SU(2)` holonomies are commuting pairs, simultaneously conjugate into a maximal torus and subject to Weyl inversion; thus the character variety is `(U(1)×U(1))/Z₂`, the pillowcase, with four special singular points. Genus-one moduli do **not** follow the generic irreducible genus-`g≥2` dimension formula by naive substitution. A three-dimensional Chern–Simons action needs additional orientation/framing, a 3D setting and a choice of level; the 2D flat character variety alone does not derive it.

## Reproducción y bibliografía

El programa `verificar.py` y el certificado histórico se entregan junto con los datos. La ejecución completa requiere NumPy, SciPy y NetworkX. El alcance de la comprobación actual está en ../VERIFICACION.md. Las referencias públicas se reúnen en ../BIBLIOGRAFIA.md.
