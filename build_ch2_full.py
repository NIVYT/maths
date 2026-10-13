import os
from builder_common import BASE_DIR, wrap, si

ch2 = """
<div class="header-card">
  <span class="badge">NCERT Chapter 2</span>
  <h1>Relations & Functions</h1>
  <p>From ordered pairs and arrow diagrams to mastering domains, ranges, and standard functions for Class 11 exams.</p>
  <div class="stats-row">
    <span>[[CLOCK]] ~45 min read</span>
    <span>[[TARGET]] 6–8 marks in exam</span>
    <span>[[BOOK]] <a href="../kemh102.pdf">kemh102.pdf</a></span>
  </div>
</div>

<div class="toc">
  <h3>[[INFO]] What you will learn in this chapter</h3>
  <ol>
    <li><a href="#s1">Cartesian Product of Sets — Ordered pairs & $A \\times B$</a></li>
    <li><a href="#s2">Relations — Concept, Domain, Codomain, Range & Arrow Diagrams</a></li>
    <li><a href="#s3">Functions Explained — Why every function is a relation, but not vice-versa</a></li>
    <li><a href="#s4">7 Standard Real Functions & Their Graphs (Modulus, Signum, GIF, etc.)</a></li>
    <li><a href="#s5">Algebra of Real Functions — Addition, Subtraction, Multiplication & Division</a></li>
    <li><a href="#s6">How to Find Domain & Range (The Complete Checklist)</a></li>
    <li><a href="#s7">Worked Examples — Easy to Hard</a></li>
    <li><a href="#s8">NCERT Key Exercise Questions Solved</a></li>
    <li><a href="#s9">Common Exam Traps & Pitfalls</a></li>
    <li><a href="#s10">Quick Self-Check Quiz</a></li>
  </ol>
</div>

<!-- SECTION 1 -->
<h2 class="section-title" id="s1">[[ZAP]] 1. Cartesian Product of Sets</h2>

<div class="definition">
  <strong>Definition: Ordered Pair</strong>
  <p>An ordered pair consists of two elements written in a specific order: $(a, b)$, where $a$ is the first element and $b$ is the second element. Note that $(a, b) \\ne (b, a)$ unless $a = b$.</p>
</div>

<div class="concept-box">
  <h4>Equality of Ordered Pairs</h4>
  <p>Two ordered pairs are equal <strong>if and only if</strong> their corresponding first and second elements are equal:</p>
  <p>$$(x_1, y_1) = (x_2, y_2) \\iff x_1 = x_2 \\text{ and } y_1 = y_2$$</p>
  <p><strong>Classic Exam Question:</strong> If $(x + 1, y - 2) = (3, 1)$, find $x$ and $y$.</p>
  <p>Comparing coordinates: $x + 1 = 3 \\implies x = 2$; and $y - 2 = 1 \\implies y = 3$.</p>
</div>

<div class="definition">
  <strong>Definition: Cartesian Product $A \\times B$</strong>
  <p>Given two non-empty sets $A$ and $B$, the Cartesian product $A \\times B$ is the set of <strong>all ordered pairs</strong> $(a, b)$ such that $a \\in A$ and $b \\in B$.</p>
  <p>$$A \\times B = \\{(a, b) : a \\in A, b \\in B\\}$$</p>
</div>

<div class="concept-box">
  <h4>Crucial Properties of Cartesian Products</h4>
  <ul>
    <li><strong>Cardinality Rule:</strong> If $n(A) = p$ and $n(B) = q$, then $n(A \\times B) = p \\cdot q$.</li>
    <li><strong>Non-Commutative:</strong> In general, $A \\times B \\ne B \\times A$ unless $A = B$.</li>
    <li><strong>Empty Set Product:</strong> If either $A = \\phi$ or $B = \\phi$, then $A \\times B = \\phi$.</li>
    <li><strong>Ordered Triplet:</strong> $A \\times A \\times A = \\{(a, b, c) : a, b, c \\in A\\}$. $(a, b, c)$ is called an ordered triplet.</li>
    <li><strong>Geometric Meaning:</strong> $\\mathbb{R} \\times \\mathbb{R} = \\mathbb{R}^2$ represents the coordinates of all points in the 2D Cartesian plane. $\\mathbb{R} \\times \\mathbb{R} \\times \\mathbb{R} = \\mathbb{R}^3$ represents 3D space!</li>
  </ul>
</div>

<!-- SECTION 2 -->
<h2 class="section-title" id="s2">[[ZAP]] 2. Relations: Connecting Two Sets</h2>

<div class="concept-box">
  <h4>Intuition: What is a Relation?</h4>
  <p>In English, a relation is a connection between people (e.g., "is brother of", "is taller than"). In mathematics, a relation between two sets $A$ and $B$ is simply a rule or condition that pairs certain elements of $A$ with elements of $B$.</p>
</div>

<div class="definition">
  <strong>Formal Definition of Relation</strong>
  <p>A relation $R$ from set $A$ to set $B$ is simply any <strong>subset of the Cartesian product</strong> $A \\times B$. That is, $R \\subseteq A \\times B$.</p>
</div>

<div class="concept-box">
  <h4>How Many Relations Can Exist?</h4>
  <p>Since any relation $R$ from $A$ to $B$ is a subset of $A \\times B$, and $A \\times B$ has $p \\cdot q$ elements:</p>
  <p>$$\\text{Total number of relations from } A \\text{ to } B = 2^{n(A) \\cdot n(B)} = 2^{pq}$$</p>
  <p><strong>Example:</strong> If $n(A) = 2$ and $n(B) = 3$, there are $2^{2 \\times 3} = 2^6 = 64$ possible relations!</p>
</div>

<div class="types-grid">
  <div class="type-card">
    <h5>Domain of $R$</h5>
    <p>The set of all <strong>first elements</strong> of the ordered pairs in $R$.</p>
    <p>$$\\text{Domain} = \\{a \\in A : (a, b) \\in R\\}$$</p>
  </div>
  <div class="type-card">
    <h5>Range of $R$</h5>
    <p>The set of all <strong>second elements</strong> actually used in $R$.</p>
    <p>$$\\text{Range} = \\{b \\in B : (a, b) \\in R\\}$$</p>
  </div>
  <div class="type-card">
    <h5>Codomain of $R$</h5>
    <p>The entire target set $B$, whether all elements are matched or not. Always: $\\mathbf{\\text{Range} \\subseteq \\text{Codomain}}$.</p>
  </div>
  <div class="type-card">
    <h5>Arrow Diagram</h5>
    <p>Visual depiction: Draw two ellipses for $A$ and $B$, write elements inside, and draw directed arrows from $a$ to $b$ whenever $(a, b) \\in R$.</p>
  </div>
</div>

<!-- SECTION 3 -->
<h2 class="section-title" id="s3">[[ZAP]] 3. Functions: The Special Relation</h2>

<div class="concept-box">
  <h4>The Vending Machine Metaphor</h4>
  <p>Think of a function like a reliable vending machine:</p>
  <ul>
    <li>Every valid button you press (every input in the Domain) must produce a snack (an output).</li>
    <li>When you press button "A1", you must get <strong>exactly one</strong> predictable item — never two different items simultaneously. If pressing button 1 gives a soda today and chips tomorrow at random, the machine is broken!</li>
  </ul>
</div>

<div class="definition">
  <strong>Formal Definition of a Function</strong>
  <p>A relation $f$ from set $A$ to set $B$ is called a <strong>function</strong> if:</p>
  <ol>
    <li>Every element of $A$ has an image in $B$. (No orphan inputs).</li>
    <li>Each element of $A$ has <strong>one and only one</strong> image in $B$. (No ambiguous multi-outputs).</li>
  </ol>
  <p>We write $f: A \\to B$, and if $(x, y) \\in f$, we write $y = f(x)$, where $y$ is the <em>image</em> of $x$ under $f$, and $x$ is the <em>pre-image</em> of $y$.</p>
</div>

<div class="concept-box">
  <h4>Summary: Is It a Function or Not?</h4>
  <ul>
    <li><strong>Many inputs to one output:</strong> ALLOWED! (e.g. $(-2)^2 = 4$ and $(2)^2 = 4$; two inputs can share the same image).</li>
    <li><strong>One input to multiple outputs:</strong> FORBIDDEN! If an input $x$ points to both $y_1$ and $y_2$ ($y_1 \\ne y_2$), it is NOT a function.</li>
    <li><strong>Leftover elements in set $A$:</strong> FORBIDDEN! Every element in $A$ must be mapped.</li>
    <li><strong>Leftover elements in set $B$:</strong> ALLOWED! Codomain can have elements that aren't mapped to anything.</li>
    <li><strong>Vertical Line Test:</strong> If any vertical line intersects the graph of a curve at more than one point, the curve is NOT a function of $x$.</li>
  </ul>
</div>

<!-- SECTION 4 -->
<h2 class="section-title" id="s4">[[ZAP]] 4. Standard Real Functions & Their Graphs</h2>

<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Function Name</th>
        <th>Formula $f(x)$</th>
        <th>Domain</th>
        <th>Range</th>
        <th>Key Characteristics</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Identity Function</strong></td>
        <td>$f(x) = x$</td>
        <td>$\\mathbb{R}$</td>
        <td>$\\mathbb{R}$</td>
        <td>Straight line through origin at $45^\\circ$ angle ($y = x$).</td>
      </tr>
      <tr>
        <td><strong>Constant Function</strong></td>
        <td>$f(x) = c$</td>
        <td>$\\mathbb{R}$</td>
        <td>$\\{c\\}$</td>
        <td>Horizontal line parallel to the x-axis at height $y = c$.</td>
      </tr>
      <tr>
        <td><strong>Square Function</strong></td>
        <td>$f(x) = x^2$</td>
        <td>$\\mathbb{R}$</td>
        <td>$[0, \\infty)$</td>
        <td>Parabola opening upwards with vertex at $(0, 0)$.</td>
      </tr>
      <tr>
        <td><strong>Cube Function</strong></td>
        <td>$f(x) = x^3$</td>
        <td>$\\mathbb{R}$</td>
        <td>$\\mathbb{R}$</td>
        <td>S-shaped curve passing through origin.</td>
      </tr>
      <tr>
        <td><strong>Reciprocal Function</strong></td>
        <td>$f(x) = 1/x$</td>
        <td>$\\mathbb{R} \\setminus \\{0\\}$</td>
        <td>$\\mathbb{R} \\setminus \\{0\\}$</td>
        <td>Rectangular hyperbola in 1st and 3rd quadrants; never touches axes.</td>
      </tr>
      <tr>
        <td><strong>Modulus Function</strong></td>
        <td>$f(x) = |x|$</td>
        <td>$\\mathbb{R}$</td>
        <td>$[0, \\infty)$</td>
        <td>V-shaped graph: $x$ for $x \\ge 0$, $-x$ for $x < 0$. Always non-negative.</td>
      </tr>
      <tr>
        <td><strong>Signum Function</strong></td>
        <td>$\\text{sgn}(x)$</td>
        <td>$\\mathbb{R}$</td>
        <td>$\\{-1, 0, 1\\}$</td>
        <td>Outputs $1$ if $x > 0$, $0$ if $x = 0$, and $-1$ if $x < 0$. Discontinuous at $0$.</td>
      </tr>
      <tr>
        <td><strong>Greatest Integer Function (GIF)</strong></td>
        <td>$f(x) = [x]$</td>
        <td>$\\mathbb{R}$</td>
        <td>$\\mathbb{Z}$ (Integers)</td>
        <td>Step function ("Floor"): outputs greatest integer $\\le x$. E.g. $[2.9]=2, [-1.2]=-2$.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="concept-box">
  <h4>Deep Dive: Greatest Integer Function $[x]$</h4>
  <p>The greatest integer function rounds any real number <strong>DOWN</strong> to the nearest integer on the number line:</p>
  <ul>
    <li>$[3.7] = 3$</li>
    <li>$[4.0] = 4$</li>
    <li>$[0.85] = 0$</li>
    <li>$[-0.4] = -1$ (Careful! Round down to the left on the number line!)</li>
    <li>$[-2.8] = -3$</li>
  </ul>
</div>

<!-- SECTION 5 -->
<h2 class="section-title" id="s5">[[ZAP]] 5. Algebra of Real Functions</h2>

<div class="concept-box">
  <h4>Operations on Real Functions</h4>
  <p>Let $f: X \\to \\mathbb{R}$ and $g: X \\to \\mathbb{R}$ be two real functions. Their domain for basic operations is the <strong>intersection</strong> of their domains: $D_f \\cap D_g$.</p>
  <ul>
    <li><strong>Addition:</strong> $(f + g)(x) = f(x) + g(x)$, domain $D_f \\cap D_g$.</li>
    <li><strong>Subtraction:</strong> $(f - g)(x) = f(x) - g(x)$, domain $D_f \\cap D_g$.</li>
    <li><strong>Scalar Multiplication:</strong> $(c \\cdot f)(x) = c \\cdot f(x)$, domain $D_f$.</li>
    <li><strong>Multiplication (Product):</strong> $(f \\cdot g)(x) = f(x) \\cdot g(x)$, domain $D_f \\cap D_g$.</li>
    <li><strong>Quotient (Division):</strong> $\\left(\\frac{f}{g}\\right)(x) = \\frac{f(x)}{g(x)}$, domain $\\{x \\in D_f \\cap D_g : g(x) \\ne 0\\}$.</li>
  </ul>
</div>

<!-- SECTION 6 -->
<h2 class="section-title" id="s6">[[ZAP]] 6. Systematic Guide: Finding Domain & Range</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>Rule 1: Denominators Cannot Be Zero</h5>
    <p>For $f(x) = \\frac{P(x)}{Q(x)}$, set $Q(x) \\ne 0$. Exclude roots of $Q(x)$ from $\\mathbb{R}$.</p>
    <p>Example: $f(x) = \\frac{1}{x - 3} \\implies \\text{Domain} = \\mathbb{R} \\setminus \\{3\\}$.</p>
  </div>
  <div class="type-card">
    <h5>Rule 2: Expressions Inside Even Roots $\\ge 0$</h5>
    <p>For $f(x) = \\sqrt{g(x)}$, require $g(x) \\ge 0$.</p>
    <p>Example: $f(x) = \\sqrt{9 - x^2} \\implies 9 - x^2 \\ge 0 \\implies x^2 \\le 9 \\implies -3 \\le x \\le 3$.</p>
  </div>
  <div class="type-card">
    <h5>Rule 3: Square Root in Denominator</h5>
    <p>For $f(x) = \\frac{1}{\\sqrt{g(x)}}$, require strict inequality $g(x) > 0$.</p>
  </div>
  <div class="type-card">
    <h5>How to Find Range: Two Reliable Methods</h5>
    <p><strong>Method A (Express $x$ in terms of $y$):</strong> Let $y = f(x)$, solve for $x = g(y)$, find values of $y$ for which real $x$ exists.</p>
    <p><strong>Method B (Inequality chaining):</strong> Start with known bounds (e.g. $x^2 \\ge 0$ or $-3 \\le x \\le 3$) and build $y$.</p>
  </div>
</div>

<!-- SECTION 7 -->
<h2 class="section-title" id="s7">[[TARGET]] 7. Worked Examples — Easy to Hard</h2>

<!-- Ex 1 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 1: Equality of Ordered Pairs</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    If $\\left(\\frac{x}{3} + 1, y - \\frac{2}{3}\\right) = \\left(\\frac{5}{3}, \\frac{1}{3}\\right)$, find the values of $x$ and $y$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> Equate corresponding components.
      $$\\frac{x}{3} + 1 = \\frac{5}{3} \\quad \\text{and} \\quad y - \\frac{2}{3} = \\frac{1}{3}$$
    </div>
    <div class="step">
      <strong>Step 2:</strong> Solve for $x$: $\\frac{x}{3} = \\frac{5}{3} - 1 = \\frac{2}{3} \\implies x = 2$.
    </div>
    <div class="step">
      <strong>Step 3:</strong> Solve for $y$: $y = \\frac{1}{3} + \\frac{2}{3} = \\frac{3}{3} = 1$.
    </div>
    <p><strong>Final Answer:</strong> $x = 2,\\; y = 1$.</p>
  </div>
</div>

<!-- Ex 2 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 2: Elements of Cartesian Product & Number of Relations</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    Let $A = \\{1, 2\\}$ and $B = \\{3, 4\\}$. Write $A \\times B$. How many relations are there from $A$ to $B$? Write three such relations.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> Form all ordered pairs:
      $$A \\times B = \\{(1, 3), (1, 4), (2, 3), (2, 4)\\}$$
    </div>
    <div class="step">
      <strong>Step 2:</strong> Find total relations:
      Since $n(A \\times B) = 4$, the number of subsets of $A \\times B$ is $2^4 = 16$. Hence, there are 16 relations.
    </div>
    <div class="step">
      <strong>Step 3:</strong> Three examples of relations:
      $R_1 = \\phi$ (empty relation),
      $R_2 = \\{(1, 3), (2, 4)\\}$,
      $R_3 = A \\times B$ (universal relation).
    </div>
  </div>
</div>

<!-- Ex 3 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 3: Ordered Triplet $P \\times P \\times P$</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    If $P = \\{-1, 1\\}$, form the set $P \\times P \\times P$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> First compute $P \\times P$:
      $$P \\times P = \\{(-1, -1), (-1, 1), (1, -1), (1, 1)\\}$$
    </div>
    <div class="step">
      <strong>Step 2:</strong> Combine each pair with each element of $P$:
      $$P \\times P \\times P = \\{(-1,-1,-1), (-1,-1,1), (-1,1,-1), (-1,1,1), (1,-1,-1), (1,-1,1), (1,1,-1), (1,1,1)\\}$$
    </div>
    <p>Total elements: $2 \\times 2 \\times 2 = 8$.</p>
  </div>
</div>

<!-- Ex 4 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 4: Relation Domain, Range, and Arrow Diagram</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Let $A = \\{1, 2, 3, 4, 5, 6\\}$. Define a relation $R$ from $A$ to $A$ by $R = \\{(x, y) : y = x + 1\\}$.<br>
    (i) Write $R$ in roster form. (ii) Write down its domain, codomain, and range.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> Substitute values of $x \\in A$ such that $y = x + 1 \\in A$:
      <ul>
        <li>$x = 1 \\implies y = 2$</li>
        <li>$x = 2 \\implies y = 3$</li>
        <li>$x = 3 \\implies y = 4$</li>
        <li>$x = 4 \\implies y = 5$</li>
        <li>$x = 5 \\implies y = 6$</li>
        <li>$x = 6 \\implies y = 7 \\notin A$ (cannot include!)</li>
      </ul>
      Roster form: $R = \\{(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)\\}$.
    </div>
    <div class="step">
      <strong>Step 2:</strong> Determine Domain, Range, and Codomain:
      $$\\text{Domain} = \\{1, 2, 3, 4, 5\\}$$
      $$\\text{Range} = \\{2, 3, 4, 5, 6\\}$$
      $$\\text{Codomain} = A = \\{1, 2, 3, 4, 5, 6\\}$$
    </div>
  </div>
</div>

<!-- Ex 5 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 5: Testing if a Piecewise Relation is a Function</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    The relation $f$ is defined by:
    $$f(x) = \\begin{cases} x^2, & 0 \\le x \\le 3 \\\\ 3x, & 3 \\le x \\le 10 \\end{cases}$$
    The relation $g$ is defined by:
    $$g(x) = \\begin{cases} x^2, & 0 \\le x \\le 2 \\\\ 3x, & 2 \\le x \\le 10 \\end{cases}$$
    Show that $f$ is a function and $g$ is not a function.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>For relation $f$:</strong> The overlap occurs at $x = 3$.
      From first piece: $f(3) = 3^2 = 9$.
      From second piece: $f(3) = 3(3) = 9$.
      Both definitions yield the exact same value $9$ at the boundary. For every other $x \\in [0, 10]$, $x$ belongs to only one piece and has a unique output. Thus, each input has exactly one image. <strong>$f$ is a function!</strong>
    </div>
    <div class="step">
      <strong>For relation $g$:</strong> The overlap occurs at $x = 2$.
      From first piece: $g(2) = 2^2 = 4$.
      From second piece: $g(2) = 3(2) = 6$.
      Here, the single input $x = 2$ gives <strong>two distinct outputs</strong> ($4$ and $6$). This violates the uniqueness condition of a function. <strong>$g$ is NOT a function!</strong>
    </div>
  </div>
</div>

<!-- Ex 6 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 6: Domain and Range of Radical Function $\\sqrt{9 - x^2}$</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    Find the domain and range of the real-valued function $f(x) = \\sqrt{9 - x^2}$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Domain</strong>
      For $f(x)$ to be a real number, the term under the square root must be non-negative:
      $$9 - x^2 \\ge 0 \\implies x^2 \\le 9 \\implies -3 \\le x \\le 3$$
      $$\\mathbf{\\text{Domain} = [-3, 3]}$$
    </div>
    <div class="step">
      <strong>Step 2: Range</strong>
      Let $y = \\sqrt{9 - x^2}$.
      Since the square root symbol represents the principal (positive) square root: $y \\ge 0$.
      Squaring both sides: $y^2 = 9 - x^2 \\implies x^2 = 9 - y^2$.
      Since $x \\in [-3, 3]$, we know $x^2 \\ge 0$, which gives:
      $$9 - y^2 \\ge 0 \\implies y^2 \\le 9 \\implies -3 \\le y \\le 3$$
      Combining with $y \\ge 0$:
      $$0 \\le y \\le 3$$
      $$\\mathbf{\\text{Range} = [0, 3]}$$
    </div>
  </div>
</div>

<!-- Ex 7 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 7: Domain of a Rational Function</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    Find the domain of the function:
    $$f(x) = \\frac{x^2 + 2x + 1}{x^2 - 8x + 12}$$
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> The numerator is a polynomial defined for all $x \\in \\mathbb{R}$.
    </div>
    <div class="step">
      <strong>Step 2:</strong> For a rational function, division by zero is undefined. Hence, we must find where the denominator equals zero:
      $$x^2 - 8x + 12 = 0 \\implies (x - 2)(x - 6) = 0 \\implies x = 2 \\text{ or } x = 6$$
    </div>
    <div class="step">
      <strong>Step 3:</strong> Exclude these values from $\\mathbb{R}$:
      $$\\mathbf{\\text{Domain} = \\mathbb{R} \\setminus \\{2, 6\\} = (-\\infty, 2) \\cup (2, 6) \\cup (6, \\infty)}$$
    </div>
  </div>
</div>

<!-- Ex 8 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 8: Algebra of Functions</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Let $f(x) = \\sqrt{x}$ and $g(x) = x$. Find $(f + g)(x)$, $(f - g)(x)$, $(f \\cdot g)(x)$ and $\\left(\\frac{f}{g}\\right)(x)$ along with their domains.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Domains of individual functions:</strong>
      Domain of $f$ is $[0, \\infty)$ because $x$ is under a square root.
      Domain of $g$ is $\\mathbb{R}$.
      Their intersection is $D_f \\cap D_g = [0, \\infty)$.
    </div>
    <div class="step">
      <strong>Sum, Difference, Product:</strong>
      <ul>
        <li>$(f + g)(x) = \\sqrt{x} + x$, Domain: $[0, \\infty)$</li>
        <li>$(f - g)(x) = \\sqrt{x} - x$, Domain: $[0, \\infty)$</li>
        <li>$(f \\cdot g)(x) = \\sqrt{x} \\cdot x = x^{3/2}$, Domain: $[0, \\infty)$</li>
      </ul>
    </div>
    <div class="step">
      <strong>Quotient:</strong>
      $\\left(\\frac{f}{g}\\right)(x) = \\frac{\\sqrt{x}}{x} = \\frac{1}{\\sqrt{x}}$.
      Since denominator $g(x) = x \\ne 0$, we must exclude $0$.
      Domain of $\\frac{f}{g}$ is $(0, \\infty)$.
    </div>
  </div>
</div>

<!-- SECTION 8 -->
<h2 class="section-title" id="s8">[[BOOK]] 8. NCERT Key Exercise Questions Solved</h2>

<div class="ncert-box">
  <h4>NCERT Exercise 2.1 — Question 5 & 7</h4>
  <div class="ncert-q">
    <strong>Q:</strong> If $A \\times B$ has 6 elements and three of them are $(1, 4), (2, 6), (3, 4)$, find the sets $A$ and $B$, and the remaining elements of $A \\times B$.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>First elements belong to $A$: $\\{1, 2, 3\\} \\subseteq A$.</p>
        <p>Second elements belong to $B$: $\\{4, 6\\} \\subseteq B$.</p>
        <p>Since $n(A \\times B) = n(A) \\cdot n(B) = 6$, and $|\\{1, 2, 3\\}| = 3$, $|\\{4, 6\\}| = 2$, we have $3 \\times 2 = 6$.</p>
        <p>Therefore, $A = \\{1, 2, 3\\}$ and $B = \\{4, 6\\}$.</p>
        <p>The full set $A \\times B = \\{(1, 4), (1, 6), (2, 4), (2, 6), (3, 4), (3, 6)\\}$.</p>
        <p>Remaining elements: $\\{(1, 6), (2, 4), (3, 6)\\}$.</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 2.2 — Question 2</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Define a relation $R$ on the set $\\mathbb{N}$ of natural numbers by $R = \\{(x, y) : y = x + 5,\\; x \\text{ is a natural number less than } 4,\\; x, y \\in \\mathbb{N}\\}$. Depict this relationship using roster form. Write down the domain and the range.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Natural numbers less than 4 are $x \\in \\{1, 2, 3\\}$.</p>
        <p>For $x = 1 \\implies y = 1 + 5 = 6$.</p>
        <p>For $x = 2 \\implies y = 2 + 5 = 7$.</p>
        <p>For $x = 3 \\implies y = 3 + 5 = 8$.</p>
        <p><strong>Roster form:</strong> $R = \\{(1, 6), (2, 7), (3, 8)\\}$.</p>
        <p><strong>Domain:</strong> $\\{1, 2, 3\\}$.</p>
        <p><strong>Range:</strong> $\\{6, 7, 8\\}$.</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 2.3 — Question 2</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Find the domain and range of the following real functions:<br>
    (i) $f(x) = -|x|$<br>
    (ii) $f(x) = \\sqrt{9 - x^2}$
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p><strong>(i) For $f(x) = -|x|$:</strong></p>
        <p>Domain: Since $|x|$ is defined for all real numbers, <strong>Domain = $\\mathbb{R}$</strong>.</p>
        <p>Range: For all $x \\in \\mathbb{R}$, $|x| \\ge 0$. Multiplying by $-1$ reverses the inequality: $-|x| \\le 0$. Hence, <strong>Range = $(-\\infty, 0]$</strong>.</p>
        <p><strong>(ii) For $f(x) = \\sqrt{9 - x^2}$:</strong></p>
        <p>Domain: $9 - x^2 \\ge 0 \\implies x^2 \\le 9 \\implies -3 \\le x \\le 3$. <strong>Domain = $[-3, 3]$</strong>.</p>
        <p>Range: At $x = \\pm 3$, $f(x) = 0$. At $x = 0$, $f(x) = \\sqrt{9} = 3$. Hence, <strong>Range = $[0, 3]$</strong>.</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Miscellaneous Exercise — Question 11 & 12</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Let $A = \\{9, 10, 11, 12, 13\\}$ and let $f: A \\to \\mathbb{N}$ be defined by $f(n) = \\text{the highest prime factor of } n$. Find the range of $f$.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Find prime factorisation of each element in $A$:</p>
        <ul>
          <li>$9 = 3^2 \\implies$ highest prime factor is $3$.</li>
          <li>$10 = 2 \\times 5 \\implies$ highest prime factor is $5$.</li>
          <li>$11 = 11 \\implies$ highest prime factor is $11$.</li>
          <li>$12 = 2^2 \\times 3 \\implies$ highest prime factor is $3$.</li>
          <li>$13 = 13 \\implies$ highest prime factor is $13$.</li>
        </ul>
        <p>The set of outputs is $\\{3, 5, 11, 3, 13\\}$.</p>
        <p><strong>Range of $f = \\{3, 5, 11, 13\\}$.</strong></p>
      </div>
    </details>
  </div>
</div>

<!-- SECTION 9 -->
<h2 class="section-title" id="s9">[[ALERT]] 9. Common Exam Traps & Pitfalls</h2>

<div class="trap-card">
  <h4>[[ALERT]] Trap 1: Confusing Codomain and Range</h4>
  <p>If $f: A \\to B$, the codomain is <strong>always the entire set $B$</strong>. The range is only the subset of elements in $B$ that actually get hit by an arrow. Range $\\subseteq$ Codomain. They are equal only if every element in $B$ has a preimage (onto function).</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 2: Square Root Output is Never Negative</h4>
  <p>In real functions, $\\sqrt{x}$ denotes the <em>principal (positive) square root</em>. So $\\sqrt{4} = 2$, NOT $\\pm 2$. If someone writes $\\text{Range of } \\sqrt{9 - x^2} = [-3, 3]$, they lose all marks! The range is $[0, 3]$.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 3: Greatest Integer of Negative Numbers</h4>
  <p>Students often write $[-2.3] = -2$. That is WRONG! $[-2.3]$ rounds DOWN (to the left) on the number line, so $[-2.3] = -3$. Remember: $[x] \\le x$. Since $-2 > -2.3$, it cannot be $-2$.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 4: Forgetting the Overlap Check in Piecewise Functions</h4>
  <p>When asked if a split relation is a function, always evaluate both formulas at the boundary point! If they disagree, the single input has two different images and it fails to be a function.</p>
</div>

<!-- SECTION 10 -->
<h2 class="section-title" id="s10">[[QUIZ]] 10. Quick Self-Check Quiz</h2>

<div class="quiz-card">
  <p><strong>Q1:</strong> If set $A$ has 3 elements and set $B$ has 2 elements, how many non-empty relations can be defined from $A$ to $B$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Total relations = $2^{3 \\times 2} = 2^6 = 64$. Non-empty relations = $64 - 1 = 63$ (excluding $\\phi$).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q2:</strong> Is $y^2 = x$ a function of $x$? Why or why not?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">No. For $x = 4$, $y = \\pm 2$. A single input gives two different outputs ($2$ and $-2$), failing the vertical line test.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q3:</strong> What is the value of $\\text{sgn}(-7) + [3.8] - [-1.1]$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$\\text{sgn}(-7) = -1$, $[3.8] = 3$, and $[-1.1] = -2$. Thus, $(-1) + 3 - (-2) = -1 + 3 + 2 = 4$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q4:</strong> What is the domain of $f(x) = \\frac{1}{\\sqrt{x - 5}}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Since the square root is in the denominator, $x - 5$ must be strictly positive: $x - 5 > 0 \\implies x > 5$. Domain is $(5, \\infty)$. (Note: open bracket at 5 because division by zero is undefined).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q5:</strong> If $f(x) = x^2$, evaluate $\\frac{f(1.1) - f(1)}{1.1 - 1}$.</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$\\frac{(1.1)^2 - 1^2}{0.1} = \\frac{1.21 - 1}{0.1} = \\frac{0.21}{0.1} = 2.1$.</div></details>
</div>
"""

out = wrap("Relations and Functions", 2, "Chapter_1_Sets.html", "Chapter_3_Trigonometric_Functions.html", ch2)
with open(os.path.join(BASE_DIR, "Chapter_2_Relations_and_Functions.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Chapter 2 written successfully!")
print("File size:", os.path.getsize(os.path.join(BASE_DIR, "Chapter_2_Relations_and_Functions.html")), "bytes")
