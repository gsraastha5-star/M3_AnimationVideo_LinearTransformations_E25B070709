# VOICE-OVER RECORDING SCRIPT
## Project: Linear Transformations – Reshaping Space with Matrices
**Course:** B.Tech Linear Algebra & Calculus (M3) — Internal Assessment  
**Narrator Style:** Student explaining to another student (friendly, conversational, natural pace, clear English)  
**Total Video Duration:** 3 minutes 55 seconds (234.8s)  
**Silent Video for Practice & Sync:** `output/final_linear_transformations_silent_1080p.mp4`

---

## 🎙️ Recording Instructions
1. **How to record:** You can record all in one take, or record scene by scene using **Voice Memos** on your Mac or iPhone.
2. **Syncing:** Open `output/final_linear_transformations_silent_1080p.mp4` in QuickTime and play it while speaking to match the visual pacing.
3. **Pacing:** Speak at a comfortable, natural pace (~135 words per minute). Don't rush; the animations have built-in breathing room.
4. **Sending to me:** Save your recording as `voiceover.mp3`, `voiceover.m4a`, or `voiceover.wav` on your Desktop (or inside the `math_video` folder), then tell me and I will instantly merge it into the video!

---

### SCENE 1: HOOK & INTRODUCTION
- **Timecode in Video:** `0:00 – 0:31` (Duration: 30.9 seconds)
- **What's happening on screen:** Coordinate grid draws; gold vector moves to (2.5, 1.5), (-1.5, 2.0), then lands at (1, 1). Question banner appears, grid does a subtle flex, then the title card displays: *LINEAR TRANSFORMATIONS: Understanding how matrices reshape space*.

> *"Welcome! Today we are exploring one of the most powerful and visual ideas in linear algebra: Linear Transformations.*  
> *Usually, we are taught to see vectors as simple arrows or coordinate pairs on a plane.*  
> *But what actually happens to vectors and coordinate grids when we multiply them by a matrix?*  
> *Let's move beyond static tables of numbers, and discover how matrices act as dynamic machines that reshape space."*

---

### SCENE 2: UNDERSTANDING THE CONCEPT
- **Timecode in Video:** `0:31 – 1:02` (Duration: 30.8 seconds)
- **What's happening on screen:** Three cards appear: 1. Vector, 2. Matrix, 3. Linear Map. Then transitions to the two linearity property boxes: Property 1 (Additivity) and Property 2 (Homogeneity).

> *"Let's ground our intuition with three key concepts: a vector with magnitude and direction, a matrix as a geometric transformation machine, and a linear map.*  
> *What makes a transformation linear? Two visual rules: the origin stays anchored at (0, 0), and all grid lines remain straight and parallel.*  
> *Mathematically, this satisfies two properties:*  
> *Additivity: T of u plus v equals T of u plus T of v;*  
> *and Homogeneity: T of c times v equals c times T of v.*  
> *Where the basis vectors go, the entire space must follow."*

---

### SCENE 3: VISUAL INTUITION & BASIS VECTORS
- **Timecode in Video:** `1:02 – 1:40` (Duration: 38.7 seconds)
- **What's happening on screen:** Standard basis vectors appear: green e₁ at (1, 0) and red e₂ at (0, 1) framing the blue unit square (area = 1). Matrix A = [[2,1],[0,1]] appears with Column 1 green and Column 2 red. The grid smoothly deforms over 5 seconds into tilted parallelograms!

> *"Here is our standard Cartesian grid with basis vectors: green is e-one at (1, 0), red is e-two at (0, 1), framing our unit square.*  
> *Now look at our matrix: A equals [[2, 1], [0, 1]]. Notice the columns!*  
> *Column one is [2, 0], and column two is [1, 1].*  
> *As the matrix acts on the plane, e-one stretches along the x-axis to (2, 0), e-two leans sideways to (1, 1), and the square grid shears into a parallelogram grid of area 2.*  
> *The columns literally tell us where the basis vectors land!"*

---

### SCENE 4: STEP-BY-STEP WORKED EXAMPLE
- **Timecode in Video:** `1:40 – 2:41` (Duration: 60.7 seconds)
- **What's happening on screen:** Vector v = [1, 1]ᵀ is on the right. Blackboard on the left shows step-by-step matrix multiplication: row dot products, then intermediate sum [2+1, 0+1]ᵀ, then final [3, 1]ᵀ. Then vector v glides to (3, 1). Tip-to-tail verification shows 1·T(e₁) + 1·T(e₂) = [2,0] + [1,1] = [3,1].

> *"Let's test this with a worked example: vector v equals [1, 1].*  
> *Notice that v is simply one times e-one plus one times e-two.*  
> *Now, we compute A times v algebraically, step by step.*  
> *For the top row, the dot product is 2 times 1 plus 1 times 1, which equals 2 plus 1, giving 3.*  
> *For the bottom row, 0 times 1 plus 1 times 1 equals 1.*  
> *Our calculated result is the vector [3, 1].*  
> *Now watch the geometry!*  
> *As the transformation is applied, vector v sweeps across the grid and lands at coordinates (3, 1).*  
> *Why? Because T of v equals 1 times T of e-one plus 1 times T of e-two:*  
> *[2, 0] plus [1, 1] equals [3, 1].*  
> *Algebra and geometry reveal the exact same truth!"*

---

### SCENE 5: GEOMETRIC INTERPRETATION & THE SHEAR
- **Timecode in Video:** `2:41 – 3:21` (Duration: 39.9 seconds)
- **What's happening on screen:** Three dots on line x = 1 at heights y = 0, 1, 2. Coordinate equations x' = 2x+y and y' = y. Grid shears: vertical line tilts to 45°, dot at (1,0) -> (2,0), dot at (1,1) -> (3,1), dot at (1,2) -> (4,2). Determinant invariant det(A) = 2.

> *"Let's look closely at the coordinate equations: x prime equals 2x plus y, and y prime equals y.*  
> *Notice that y prime is completely unchanged. Every horizontal line stays at its original height.*  
> *Meanwhile, x prime scales by 2, plus an additional shift equal to y.*  
> *Points higher up shift further to the right. That progressive displacement is what creates the shear effect.*  
> *Yet, the origin remains fixed, straight lines stay straight, and all areas are exactly doubled, because the determinant of A is 2."*

---

### SCENE 6: SUMMARY & CREDITS
- **Timecode in Video:** `3:21 – 3:55` (Duration: 33.8 seconds)
- **What's happening on screen:** Three takeaway cards appear. Then the glowing quote card: *"One matrix. Two basis vectors. An entire transformed plane."* Finally, project credits card.

> *"Here are the three big takeaways:*  
> *First: A matrix defines how vectors transform space.*  
> *Second: The columns of a matrix describe the transformed basis vectors, determining the entire plane.*  
> *Third: Linear transformations preserve straight lines and the origin.*  
> *Always remember:*  
> *One matrix. Two basis vectors. An entire transformed plane.*  
> *Good luck with your B-Tech mathematics assessment!"*
