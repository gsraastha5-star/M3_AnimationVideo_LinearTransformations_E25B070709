#set page(
  paper: "a4",
  margin: (x: 2.0cm, top: 2.2cm, bottom: 2.2cm),
  header: align(right)[
    #text(size: 8pt, fill: rgb("#64748b"))[B.Tech Linear Algebra & Calculus (M3) • Mathematical Derivation]
  ],
  footer: [
    #text(size: 8pt, fill: rgb("#64748b"))[
      Linear Transformations & Matrix Representations
      #h(1fr)
      Internal Assessment Technical Report
    ]
  ]
)

#set text(font: "Helvetica", size: 10pt, fill: rgb("#0f172a"))
#set par(justify: true, leading: 0.65em)

// Document Header Block
#align(center)[
  #block(
    fill: rgb("#0f172a"),
    inset: 18pt,
    radius: 8pt,
    width: 100%,
    [
      #text(size: 11pt, weight: "bold", fill: rgb("#38bdf8"))[B.TECH MATHEMATICS 3 (M3) — INTERNAL ASSESSMENT]\
      #v(6pt)
      #text(size: 20pt, weight: "bold", fill: rgb("#ffffff"))[MATHEMATICAL DERIVATION & PROOF REPORT]\
      #v(4pt)
      #text(size: 13pt, fill: rgb("#94a3b8"))[Rigorous Algebraic and Geometric Foundations of Linear Transformations]\
      #v(6pt)
      #text(size: 9pt, fill: rgb("#cbd5e1"))[Matrix: $A = mat(2, 1; 0, 1)$ • Vector: $v = [1, 1]^T$ • Transformed: $A v = [3, 1]^T$]
    ]
  )
]

#v(14pt)

== 1. Abstract & Scope

This mathematical technical report provides the complete formal foundation for the B.Tech Linear Algebra and Calculus (M3) animation project. We rigorously investigate the action of the $2 times 2$ matrix $A = mat(2, 1; 0, 1)$ on the real vector space $RR^2$. We establish:
1. The formal axiomatic definition of a linear map $T: RR^2 -> RR^2$.
2. The fundamental basis-representation theorem proving that a linear transformation is uniquely determined by its action on the standard basis ${e_1, e_2}$.
3. The exact algebraic derivation of $A v = [3, 1]^T$ for $v = [1, 1]^T$.
4. The geometric decomposition into horizontal dilation (scale factor 2) and horizontal shear.
5. Invariance principles (origin anchoring, straight line preservation, parallelism preservation) and determinant-induced area doubling.

---

== 2. Formal Definition of a Linear Transformation

Let $V$ and $W$ be vector spaces over the field of real numbers $RR$. A mapping $T: V -> W$ is defined to be a *linear transformation* if and only if it satisfies two fundamental axioms:

#block(
  fill: rgb("#f8fafc"),
  stroke: 1pt + rgb("#e2e8f0"),
  inset: 12pt,
  radius: 6pt,
  width: 100%,
  [
    *Axiom 1 (Additivity / Principle of Superposition):*
    $ forall u, v in V, quad T(u + v) = T(u) + T(v) $

    *Axiom 2 (Homogeneity / Scalar Scaling):*
    $ forall v in V, quad forall c in RR, quad T(c v) = c T(v) $
  ]
)

These two conditions can be compactly synthesized into a single equivalent criterion:
$ forall u, v in V, quad forall c_1, c_2 in RR, quad T(c_1 u + c_2 v) = c_1 T(u) + c_2 T(v) $

=== Immediate Corollaries:
1. *Preservation of the Zero Vector:*
   Setting $c = 0$ in Axiom 2 yields:
   $ T(bold(0)) = T(0 dot v) = 0 dot T(v) = bold(0) $
   *Geometric Meaning:* Under any linear transformation, the origin $(0, 0)$ is an invariant point; it can never translate or shift.
2. *Preservation of Collinearity:*
   If points lie on a straight line parameterised by $r(t) = p + t d$, then:
   $ T(r(t)) = T(p + t d) = T(p) + t T(d) $
   which is itself the parametric equation of a straight line. Straight lines can never bend, curve, or break under a linear map.

---

== 3. The Basis-Representation Theorem

Let $V = RR^2$ equipped with the standard ordered basis:
$ cal(B) = {e_1, e_2} = { vec(1, 0), vec(0, 1) } $

#block(
  fill: rgb("#f1f5f9"),
  inset: 10pt,
  radius: 4pt,
  [
    *Theorem (Unique Determination by Basis):*  
    _Let $T: RR^2 -> RR^2$ be a linear transformation. Then $T$ is completely and uniquely determined by its action on the basis vectors $T(e_1)$ and $T(e_2)$._
  ]
)

*Proof:*  
Any vector $v = vec(x, y) in RR^2$ can be uniquely expressed as a linear combination of the basis vectors:
$ v = x vec(1, 0) + y vec(0, 1) = x e_1 + y e_2 $

Applying the transformation $T$ and utilizing the linearity axioms:
$ T(v) = T(x e_1 + y e_2) = x T(e_1) + y T(e_2) $

Thus, knowing only the two output vectors $T(e_1)$ and $T(e_2)$ suffices to evaluate $T(v)$ for *all* $v in RR^2$.

Defining the matrix $[T]_cal(B)$ whose column vectors are $T(e_1)$ and $T(e_2)$:
$ [T]_cal(B) = mat(T(e_1), T(e_2)) = mat(a, b; c, d) $
we obtain the canonical matrix-vector multiplication:
$ T(v) = mat(a, b; c, d) vec(x, y) = x vec(a, c) + y vec(b, d) = vec(a x + b y, c x + d y) $

#pagebreak()

== 4. Explicit Matrix Analysis: $A = mat(2, 1; 0, 1)$

We now analyze the specific matrix assigned for this assessment:
$ A = mat(2, 1; 0, 1) $

=== 4.1. Transformed Standard Basis Vectors
Evaluating the action of $A$ on the standard basis vectors:

1. *First Basis Vector $e_1 = [1, 0]^T$:*
   $ T(e_1) = A e_1 = mat(2, 1; 0, 1) vec(1, 0) = vec(2(1) + 1(0), 0(1) + 1(0)) = vec(2, 0) $
   *Geometric Result:* The unit vector along the x-axis is stretched horizontally by a factor of 2, remaining on the x-axis.

2. *Second Basis Vector $e_2 = [0, 1]^T$:*
   $ T(e_2) = A e_2 = mat(2, 1; 0, 1) vec(0, 1) = vec(2(0) + 1(1), 0(0) + 1(1)) = vec(1, 1) $
   *Geometric Result:* The unit vector along the y-axis tilts to the right by 1 unit, landing at $(1, 1)$.

=== 4.2. Verification of Matrix Columns
Notice that:
$ "Column 1 of " A = vec(2, 0) = T(e_1) $
$ "Column 2 of " A = vec(1, 1) = T(e_2) $
This confirms the core pedagogical principle: the columns of the matrix are precisely the transformed standard basis vectors!

---

== 5. Worked Example: Transformation of Vector $v = [1, 1]^T$

Let the input vector be:
$ v = vec(1, 1) $

We compute $T(v)$ through two distinct, mathematically equivalent pathways.

=== Pathway A: Direct Algebraic Matrix Multiplication
$ A v = mat(2, 1; 0, 1) vec(1, 1) $

Evaluating row-by-column dot products explicitly:
- *Row 1 Dot Product:* $2(1) + 1(1) = 2 + 1 = 3$
- *Row 2 Dot Product:* $0(1) + 1(1) = 0 + 1 = 1$

Assembling the resulting vector:
$ A v = vec(2(1) + 1(1), 0(1) + 1(1)) = vec(2 + 1, 0 + 1) = vec(3, 1) $

=== Pathway B: Linear Combination of Transformed Basis Vectors
Expressing $v$ in terms of the standard basis:
$ v = 1 e_1 + 1 e_2 $

By linearity:
$ T(v) = 1 T(e_1) + 1 T(e_2) = 1 vec(2, 0) + 1 vec(1, 1) = vec(2 + 1, 0 + 1) = vec(3, 1) $

Both algebraic dot-product expansion and geometric vector combination yield the identical result: $vec(3, 1)$.

#v(10pt)

#align(center)[
  #block(
    fill: rgb("#f0fdf4"),
    stroke: 1pt + rgb("#22c55e"),
    inset: 10pt,
    radius: 6pt,
    width: 90%,
    [
      #text(weight: "bold", fill: rgb("#15803d"))[Calculation Verification Result:]\
      $ v = vec(1, 1) quad limits(-->)^T quad A v = vec(3, 1) $
      All arithmetic steps verified independently and validated by geometric construction.
    ]
  )
]

---

== 6. Geometric Interpretation & Shear Analysis

=== 6.1. Coordinate System Equations
Let $(x, y)$ be any arbitrary point in the Cartesian plane, and let $(x', y')$ denote its image under $T$:
$ vec(x', y') = mat(2, 1; 0, 1) vec(x, y) = vec(2x + y, y) $

This gives the system of transformation equations:
$ cases(x' = 2x + y, y' = y) $

=== 6.2. Two Fundamental Geometric Properties:
1. *Vertical Invariance ($y' = y$):*
   Every horizontal line $y = k$ satisfies $y' = k$. The vertical coordinates of all points in the plane remain strictly invariant. Space does not compress or stretch in the y-direction.
2. *Horizontal Shear and Dilation ($x' = 2x + y$):*
   The horizontal coordinate undergoes two simultaneous effects:
   - Dilation by factor 2: Every x-coordinate is doubled.
   - Height-dependent displacement: A shift of $+y$ units is added.
   
#table(
  columns: (1fr, 1.2fr, 1.5fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header([*Elevation*], [*Original Point* $(x, y)$], [*Transformed Point* $(x', y') = (2x+y, y)$]),
  [$y = 0$ (x-axis)], [$(1, 0)$], [$(2(1)+0, 0) = (2, 0)$ (Pure horizontal scaling)],
  [$y = 1$], [$(1, 1)$], [$(2(1)+1, 1) = (3, 1)$ (Scaled and shifted right by 1)],
  [$y = 2$], [$(1, 2)$], [$(2(1)+2, 2) = (4, 2)$ (Scaled and shifted right by 2)],
  [$y = -1$], [$(1, -1)$], [$(2(1)-1, -1) = (1, -1)$ (Shifted left by 1)]
)

Because horizontal displacement is directly proportional to height $y$, this transformation produces a classical *horizontal shear* coupled with horizontal dilation.

#pagebreak()

=== 6.3. Transformation of Grid Lines
- *Horizontal grid lines ($y = c$):*  
  Transform to $y' = c$ (horizontal lines).
- *Vertical grid lines ($x = k$):*  
  Under $T$, $x' = 2k + y$ and $y' = y$.  
  Substituting $y = y'$: $x' = 2k + y' ==> y' = x' - 2k$.  
  These are parallel straight lines with slope $m = 1$ (angle of $45^degree$).
- *Grid cells:*  
  Square cells of dimension $1 times 1$ transform into parallelograms with base 2 and perpendicular height 1.

---

== 7. Determinant and Area Scaling

In linear algebra, the determinant of a $2 times 2$ matrix represents the factor by which areas are scaled under the transformation.

For matrix $A = mat(2, 1; 0, 1)$:
$ det(A) = (2)(1) - (1)(0) = 2 - 0 = 2 $

=== Geometric Proof:
Consider the unit square $S$ formed by $bold(0), e_1, e_2, e_1+e_2$:
$ "Area"(S) = 1 times 1 = 1 $

Under transformation $T$, $S$ maps to parallelogram $P$ with vertices:
$ bold(0) = vec(0, 0), quad T(e_1) = vec(2, 0), quad T(e_2) = vec(1, 1), quad T(e_1 + e_2) = vec(3, 1) $

The area of parallelogram $P$ can be computed using the 2D cross product:
$ "Area"(P) = |T(e_1) times T(e_2)| = |(2)(1) - (0)(1)| = 2 $

Therefore:
$ "Area"(T(Omega)) = |det(A)| dot "Area"(Omega) = 2 dot "Area"(Omega) $
Every region in the plane has its area exactly doubled under transformation $A$. Furthermore, since $det(A) > 0$, the orientation of space is preserved (no reflection occurs).

---

== 8. Eigenvalue & Eigenvector Decomposition (M3 Extension)

To provide complete depth for the B.Tech M3 curriculum, we compute the eigensystem of $A$.

=== 8.1. Characteristic Equation
$ det(A - lambda I) = det mat(2 - lambda, 1; 0, 1 - lambda) = (2 - lambda)(1 - lambda) - (1)(0) = 0 $
$ (2 - lambda)(1 - lambda) = 0 $

The eigenvalues are:
$ lambda_1 = 2, quad lambda_2 = 1 $

=== 8.2. Eigenvectors
1. *For $lambda_1 = 2$:*
   $ (A - 2I) v_1 = mat(0, 1; 0, -1) vec(x, y) = vec(0, 0) ==> y = 0, quad x in RR $
   $ v_1 = vec(1, 0) $
   *Geometric Meaning:* The x-axis is an invariant direction along which vectors undergo pure elongation by a factor of 2.

2. *For $lambda_2 = 1$:*
   $ (A - I) v_2 = mat(1, 1; 0, 0) vec(x, y) = vec(0, 0) ==> x + y = 0 ==> x = -y $
   $ v_2 = vec(-1, 1) $
   *Geometric Meaning:* Along the line $y = -x$, vectors have eigenvalue $lambda = 1$, meaning their magnitude is unchanged ($A v_2 = 1 v_2$).

---

== 9. Summary & Conclusions

#block(
  fill: rgb("#0f172a"),
  inset: 14pt,
  radius: 6pt,
  width: 100%,
  [
    #text(weight: "bold", fill: rgb("#38bdf8"))[Key Technical Findings:]
    #text(fill: rgb("#ffffff"))[
      1. *Matrix as Function:* Matrix $A$ is an operator that deforms the entire plane while preserving linearity.
      2. *Basis Determination:* The columns of $A$, $[2, 0]^T$ and $[1, 1]^T$, uniquely govern the transformation of all vectors.
      3. *Exact Vector Mapping:* For $v = [1, 1]^T$, $A v = [3, 1]^T$, demonstrated algebraically and geometrically.
      4. *Geometric Mechanism:* A combination of horizontal stretch (factor 2) and horizontal shear ($+y$ displacement).
      5. *Area Scaling:* $det(A) = 2$, doubling all areas while preserving orientation and collinearity.
    ]
  ]
)
