#set page(
  paper: "a4",
  margin: (x: 1.8cm, top: 2.0cm, bottom: 2.0cm),
  header: align(right)[
    #text(size: 8pt, fill: rgb("#64748b"))[B.Tech Linear Algebra & Calculus (M3) • Video Animation Storyboard]
  ],
  footer: [
    #text(size: 8pt, fill: rgb("#64748b"))[
      Linear Transformations: Geometric & Algebraic Foundations
      #h(1fr)
      B.Tech Mathematics (M3)
    ]
  ]
)

#set text(font: "Helvetica", size: 10pt, fill: rgb("#1e293b"))
#set par(justify: true, leading: 0.65em)

// Document Title Block
#align(center)[
  #block(
    fill: rgb("#0f172a"),
    inset: 18pt,
    radius: 8pt,
    width: 100%,
    [
      #text(size: 11pt, weight: "bold", fill: rgb("#38bdf8"))[B.TECH LINEAR ALGEBRA & CALCULUS (M3) — INTERNAL ASSESSMENT]\
      #v(6pt)
      #text(size: 20pt, weight: "bold", fill: rgb("#ffffff"))[SIX-SCENE VIDEO STORYBOARD]\
      #v(4pt)
      #text(size: 13pt, fill: rgb("#94a3b8"))[Topic: Linear Transformations — Understanding How Matrices Reshape Space]\
      #v(6pt)
      #text(size: 9pt, fill: rgb("#cbd5e1"))[Resolution: 1920 × 1080 (1080p60) • Aspect Ratio: 16:9 • Duration: ~5:00 • Engine: Manim CE]
    ]
  )
]

#v(10pt)

== Production Overview & Design System

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    #block(stroke: 1pt + rgb("#e2e8f0"), inset: 10pt, radius: 4pt, fill: rgb("#f8fafc"))[
      #text(weight: "bold", fill: rgb("#0f172a"))[Visual & Aesthetic Standards]
      - *Style Inspiration:* 3Blue1Brown (*Essence of Linear Algebra*)
      - *Background:* Deep slate dark `#0B0F19` for maximum contrast
      - *Typography:* Modern sans-serif (Helvetica) with crisp Typst vector formulas
      - *Pedagogy:* Every animation communicates a mathematical truth; no superficial decoration
    ]
  ],
  [
    #block(stroke: 1pt + rgb("#e2e8f0"), inset: 10pt, radius: 4pt, fill: rgb("#f8fafc"))[
      #text(weight: "bold", fill: rgb("#0f172a"))[Color Key & Mathematical Mapping]
      - *Basis Vector $e_1$ ($hat(i)$):* Emerald Green (`#2ECC71`)
      - *Basis Vector $e_2$ ($hat(j)$):* Ruby Red (`#E74C3C`)
      - *Input Vector $v = [1, 1]^T$:* Amber Gold (`#F1C40F`)
      - *Transformed Vector $A v = [3, 1]^T$:* Electric Cyan (`#00E5FF`)
      - *Area / Transformed Cells:* Amethyst Purple (`#BB86FC`)
    ]
  ]
)

#v(12pt)

---

#v(10pt)

== Scene-by-Scene Detailed Storyboard

=== Scene 1: Hook & Introduction
*Timecode:* 0:00 – 0:35 (Duration: 32s) | *Target Emotion:* Curiosity & Intellectual Intrigue

#table(
  columns: (1.2fr, 2fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header(
    [*Dimension*],
    [*Specification & Content*]
  ),
  [Mathematical Goal], [Break student perception of vectors as static lists of numbers. Introduce coordinate grids dynamically.],
  [Visual Elements], [
    1. Dark coordinate plane fades in with subtle glowing grid lines.\
    2. Gold arrow $v$ originates at $(0,0)$ and sweeps to $(2.5, 1.5)$, $(-1.5, 2.0)$, and lands at $(1, 1)$.\
    3. Floating question card: _"What if a simple matrix could change the entire coordinate system?"_\
    4. Matrix preview $A = mat(2, 1; 0, 1)$ floats in; grid does a momentary subtle shear pulse teaser.\
    5. Title reveal: *LINEAR TRANSFORMATIONS: Understanding how matrices reshape space*.
  ],
  [On-Screen Formulas], [$v = [x, y]^T$, $A = mat(2, 1; 0, 1)$],
  [Audio / Voiceover], ["What happens to vectors and coordinate grids when we multiply them by a matrix? Let's stop thinking of matrices as static spreadsheets, and start seeing them as transformation machines."],
  [Technical Notes], [Manim `NumberPlane`, `always_redraw(Arrow)`, `apply_matrix(rate_func=there_and_back)`.]
)

#v(14pt)

=== Scene 2: Understanding the Concept
*Timecode:* 0:35 – 1:20 (Duration: 45s) | *Target Emotion:* Clarity, Structural Understanding

#table(
  columns: (1.2fr, 2fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header(
    [*Dimension*],
    [*Specification & Content*]
  ),
  [Mathematical Goal], [Define Vector, Matrix, and Linear Transformation. Establish the two algebraic axioms of linearity.],
  [Visual Elements], [
    1. Three distinct side-by-side concept cards: (1) Vector, (2) Matrix, (3) Linear Map.\
    2. Smooth transition to two primary linearity property containers with highlighted borders:\
       - *Property 1 (Additivity):* $T(u + v) = T(u) + T(v)$\
       - *Property 2 (Homogeneity):* $T(c v) = c T(v)$\
    3. Visual takeaway banner: If you know where basis vectors land, you know where *everything* lands!
  ],
  [On-Screen Formulas], [$v = vec(x, y)$, $A = mat(a, b; c, d)$, $T: RR^2 -> RR^2$, $T(u+v) = T(u) + T(v)$, $T(c v) = c T(v)$],
  [Audio / Voiceover], ["What makes a transformation linear? Two visual rules: the origin stays anchored, and grid lines remain straight and parallel. Mathematically, it preserves addition and scalar multiplication."],
  [Technical Notes], [Typst math SVG rendering, Manim `RoundedRectangle`, sequential `FadeIn(lag_ratio=0.25)`.]
)

#pagebreak()

=== Scene 3: Visual Intuition & The Basis Vectors
*Timecode:* 1:20 – 2:20 (Duration: 58s) | *Target Emotion:* Visual Wonder & The "Aha!" Epiphany

#table(
  columns: (1.2fr, 2fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header(
    [*Dimension*],
    [*Specification & Content*]
  ),
  [Mathematical Goal], [Demonstrate how standard basis vectors $e_1, e_2$ determine the entire plane under matrix $A$.],
  [Visual Elements], [
    1. Complete Cartesian grid. Standard basis vectors emerge: green $e_1 = (1,0)$ and red $e_2 = (0,1)$.\
    2. Blue unit square highlighted (Area = 1).\
    3. Matrix $A = mat(2, 1; 0, 1)$ presented with *Column 1 colored green* and *Column 2 colored red*.\
    4. Highlight $e_1$, then highlight $e_2$.\
    5. *The Big Transformation:* Grid deforms smoothly over 5 seconds into a parallelogram grid. $e_1$ elongates to $(2, 0)$, $e_2$ leans to $(1, 1)$, and the unit square morphs into a purple parallelogram of Area = 2.\
    6. Callout: The columns of matrix $A$ are literally the landing sites of the basis vectors!
  ],
  [On-Screen Formulas], [$A = mat(#text(fill: rgb("#2ECC71"))[2], #text(fill: rgb("#E74C3C"))[1]; #text(fill: rgb("#2ECC71"))[0], #text(fill: rgb("#E74C3C"))[1])$, $T(e_1) = vec(2, 0)$, $T(e_2) = vec(1, 1)$, $"Area" = det(A) = 2$],
  [Audio / Voiceover], ["Look at the columns of A. Don't read it horizontally; read it vertically! The first column is where e1 lands; the second column is where e2 lands. Once you track two arrows, the entire coordinate universe follows!"],
  [Technical Notes], [Synchronized `grid.animate.apply_matrix(MATRIX_A_3D)`, `Transform` on basis arrows and unit polygon.]
)

#v(14pt)

=== Scene 4: Step-by-Step Worked Example
*Timecode:* 2:20 – 3:45 (Duration: 80s) | *Target Emotion:* Confidence, Mastery, Complete Connection

#table(
  columns: (1.2fr, 2fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header(
    [*Dimension*],
    [*Specification & Content*]
  ),
  [Mathematical Goal], [Connect arithmetic matrix-vector multiplication with geometric vector displacement.],
  [Visual Elements], [
    1. Split screen layout: Coordinate plane on right; Algebraic blackboard on left.\
    2. Input vector $v = [1, 1]^T$ displayed on plane. Decomposed visually as $1 e_1 + 1 e_2$.\
    3. Calculation steps revealed sequentially on the blackboard (never jumping to the result):\
       - Step 1: $A v = mat(2, 1; 0, 1) vec(1, 1)$\
       - Step 2: Dot products $= vec(2(1) + 1(1), 0(1) + 1(1))$\
       - Step 3: Arithmetic addition $= vec(2 + 1, 0 + 1)$\
       - Step 4: Final vector result $= vec(3, 1)$ highlighted in electric cyan box.\
    4. Geometric movement: Vector $v$ sweeps smoothly across the plane to $(3, 1)$.\
    5. Tip-to-tail verification: Green $T(e_1)$ from $(0,0)$ to $(2,0)$ + Red $T(e_2)$ from $(2,0)$ to $(3,1)$.
  ],
  [On-Screen Formulas], [$A v = mat(2, 1; 0, 1) vec(1, 1) = vec(2(1)+1(1), 0(1)+1(1)) = vec(2+1, 0+1) = vec(3, 1)$],
  [Audio / Voiceover], ["Why did it land at (3, 1)? Because v was 1 e1 plus 1 e2! So T(v) is 1 T(e1) plus 1 T(e2). Take [2, 0] and tack on [1, 1] tip-to-tail. Algebra and geometry speak the exact same truth."],
  [Technical Notes], [Manim `DashedLine` coordinate projections, `SurroundingRectangle`, tip-to-tail `GrowArrow`.]
)

#pagebreak()

=== Scene 5: Geometric Interpretation & The Shear
*Timecode:* 3:45 – 4:35 (Duration: 50s) | *Target Emotion:* Deep Intuition & Mathematical Insight

#table(
  columns: (1.2fr, 2fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header(
    [*Dimension*],
    [*Specification & Content*]
  ),
  [Mathematical Goal], [Explain the coordinate equations $x' = 2x+y$ and $y' = y$. Explain horizontal shear and area scaling.],
  [Visual Elements], [
    1. Reference points on vertical line $x = 1$ at three heights: $P_0(1, 0)$, $P_1(1, 1)$, $P_2(1, 2)$.\
    2. Analytical panel showing coordinate equations: $cases(x' = 2x + y, y' = y)$.\
    3. Highlight 1: *Vertical invariance ($y' = y$)*: Horizontal lines stay at the same elevation.\
    4. Highlight 2: *Horizontal shear ($x' = 2x + y$)*: Points slide right proportionally to height $y$.\
    5. Animation: Vertical line $x=1$ shears into slanted line with slope 1 ($45^degree$). $P_0 -> (2,0)$, $P_1 -> (3,1)$, $P_2 -> (4,2)$.\
    6. Determinant invariant: $det(A) = 2(1) - 1(0) = 2$, doubling all 2D areas.
  ],
  [On-Screen Formulas], [$cases(x' = 2x + y, y' = 0x + 1y = y)$, $det(A) = 2 dot 1 - 1 dot 0 = 2$],
  [Audio / Voiceover], ["Look at y': it is completely unchanged. But in x', higher points slide further to the right. That progressive displacement is the textbook definition of a horizontal shear."],
  [Technical Notes], [Synchronized dots, line transformation under shear matrix, equation callouts.]
)

#v(14pt)

=== Scene 6: Summary & Credits
*Timecode:* 4:35 – 5:10 (Duration: 35s) | *Target Emotion:* Closure, Synthesis, Academic Rigor

#table(
  columns: (1.2fr, 2fr),
  stroke: 0.5pt + rgb("#cbd5e1"),
  table.header(
    [*Dimension*],
    [*Specification & Content*]
  ),
  [Mathematical Goal], [Reinforce the three foundational takeaways and conclude with the iconic conceptual thesis.],
  [Visual Elements], [
    1. Three structured summary cards:\
       - *1. Matrix as Transformation:* Dynamic function mapping $RR^2 -> RR^2$.\
       - *2. Columns as Basis Vectors:* $e_1 -> [2, 0]^T$ and $e_2 -> [1, 1]^T$ dictate all vectors.\
       - *3. Linearity Preserves Structure:* Origin anchored, lines remain straight, uniform spacing.\
    2. Iconic glowing thesis quote card:\
       #align(center)[_\"One matrix. Two basis vectors. An entire transformed plane.\"_]\
    3. Formal project credits card: Course info, tools used, 3Blue1Brown pedagogical attribution, AI disclosure.
  ],
  [On-Screen Formulas], [$"Takeaways 1, 2, 3"$, $"Thesis Quote"$, $"Course Metadata"$],
  [Audio / Voiceover], ["Remember: One matrix. Two basis vectors. An entire transformed plane. Good luck with your M3 engineering mathematics exams, and see you next time!"],
  [Technical Notes], [Smooth `FadeIn(scale=0.9)` on thesis quote, clean closing transition.]
)
