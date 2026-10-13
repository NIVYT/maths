import os
from builder_common import BASE_DIR, wrap, si

ch4 = """
<div class="header-card">
  <span class="badge">NCERT Chapter 4</span>
  <h1>Complex Numbers & Quadratic Equations</h1>
  <p>Demystifying the imaginary unit $i$, mastering the algebra of $a + ib$, polar form, and solving quadratics with negative discriminants.</p>
  <div class="stats-row">
    <span>[[CLOCK]] ~40 min read</span>
    <span>[[TARGET]] 5–6 marks in exam</span>
    <span>[[BOOK]] <a href="../kemh104.pdf">kemh104.pdf</a></span>
  </div>
</div>

<div class="toc">
  <h3>[[INFO]] What you will learn in this chapter</h3>
  <ol>
    <li><a href="#s1">Why Complex Numbers? The Birth of $i$</a></li>
    <li><a href="#s2">Powers of $i$ and Cyclic Properties</a></li>
    <li><a href="#s3">Algebra of Complex Numbers ($a + ib$)</a></li>
    <li><a href="#s4">Modulus, Conjugate & Multiplicative Inverse</a></li>
    <li><a href="#s5">Argand Plane & Polar Representation ($r, \\theta$)</a></li>
    <li><a href="#s6">Quadratic Equations with Complex Roots ($D < 0$)</a></li>
    <li><a href="#s7">Worked Examples — Easy to Hard</a></li>
    <li><a href="#s8">NCERT Key Exercise Questions Solved</a></li>
    <li><a href="#s9">Common Exam Traps & Pitfalls</a></li>
    <li><a href="#s10">Quick Self-Check Quiz</a></li>
  </ol>
</div>

<!-- SECTION 1 -->
<h2 class="section-title" id="s1">[[ZAP]] 1. Why Complex Numbers? The Birth of $i$</h2>

<div class="concept-box">
  <h4>The Problem that Real Numbers Couldn't Solve</h4>
  <p>Consider the elementary equation: $x^2 + 1 = 0 \\implies x^2 = -1$.</p>
  <p>Since the square of any real number is always non-negative ($x^2 \\ge 0$), no real number can satisfy this equation. To overcome this limitation, mathematicians introduced the <strong>imaginary unit</strong>, denoted by $i$ (iota), defined by:</p>
  <p>$$i = \\sqrt{-1} \\quad \\implies \\quad i^2 = -1$$</p>
</div>

<div class="definition">
  <strong>Definition: Complex Number</strong>
  <p>A number of the form $z = a + ib$, where $a, b \\in \\mathbb{R}$ and $i = \\sqrt{-1}$, is called a <strong>complex number</strong>.</p>
  <ul>
    <li>$a$ is the <strong>Real part</strong> of $z$, written as $\\text{Re}(z) = a$.</li>
    <li>$b$ is the <strong>Imaginary part</strong> of $z$, written as $\\text{Im}(z) = b$ (Note: $b$ is a real number, not including $i$!).</li>
    <li>If $b = 0$, $z = a$ is <em>purely real</em>.</li>
    <li>If $a = 0$ and $b \\ne 0$, $z = ib$ is <em>purely imaginary</em>.</li>
  </ul>
</div>

<!-- SECTION 2 -->
<h2 class="section-title" id="s2">[[ZAP]] 2. Powers of $i$ (The Cycle of 4)</h2>

<div class="concept-box">
  <h4>The Cyclic Pattern</h4>
  <p>The powers of $i$ repeat in a cycle of 4:</p>
  <ul>
    <li>$i^0 = 1$</li>
    <li>$i^1 = i$</li>
    <li>$i^2 = -1$</li>
    <li>$i^3 = i^2 \\cdot i = (-1)i = -i$</li>
    <li>$i^4 = (i^2)^2 = (-1)^2 = 1$</li>
  </ul>
  <p><strong>Master Formula for Any Power $n$:</strong> Divide $n$ by $4$. If $n = 4k + r$ (where $r \\in \\{0, 1, 2, 3\\}$ is the remainder):</p>
  <p>$$i^n = i^{4k + r} = (i^4)^k \\cdot i^r = (1)^k \\cdot i^r = i^r$$</p>
  <p><strong>Golden Property:</strong> The sum of any four consecutive powers of $i$ is ALWAYS ZERO:</p>
  <p>$$i^n + i^{n+1} + i^{n+2} + i^{n+3} = i^n(1 + i - 1 - i) = 0$$</p>
</div>

<!-- SECTION 3 -->
<h2 class="section-title" id="s3">[[ZAP]] 3. Algebra of Complex Numbers</h2>

<div class="concept-box">
  <h4>1. Equality of Two Complex Numbers</h4>
  <p>$$a_1 + ib_1 = a_2 + ib_2 \\iff a_1 = a_2 \\quad \\text{and} \\quad b_1 = b_2$$</p>
  <p>Real parts must equal real parts, and imaginary parts must equal imaginary parts!</p>
</div>

<div class="types-grid">
  <div class="type-card">
    <h5>Addition & Subtraction</h5>
    <p>$$(a + ib) \\pm (c + id) = (a \\pm c) + i(b \\pm d)$$</p>
    <p>Add/subtract real parts and imaginary parts separately.</p>
  </div>
  <div class="type-card">
    <h5>Multiplication (FOIL with $i^2 = -1$)</h5>
    <p>$$(a + ib)(c + id) = ac + iad + ibc + i^2 bd$$</p>
    <p>$$= (ac - bd) + i(ad + bc)$$</p>
  </div>
  <div class="type-card">
    <h5>Division (Conjugate Multiplication)</h5>
    <p>To compute $\\frac{a + ib}{c + id}$, multiply numerator and denominator by the conjugate of the denominator $(c - id)$:</p>
    <p>$$\\frac{a + ib}{c + id} \\times \\frac{c - id}{c - id} = \\frac{(ac + bd) + i(bc - ad)}{c^2 + d^2}$$</p>
  </div>
  <div class="type-card">
    <h5>Identities</h5>
    <p>All algebraic identities hold: $(z_1 \\pm z_2)^2 = z_1^2 \\pm 2z_1 z_2 + z_2^2$, $z_1^2 - z_2^2 = (z_1 - z_2)(z_1 + z_2)$, etc.</p>
  </div>
</div>

<!-- SECTION 4 -->
<h2 class="section-title" id="s4">[[ZAP]] 4. Modulus, Conjugate & Multiplicative Inverse</h2>

<div class="definition">
  <strong>Conjugate of a Complex Number</strong>
  <p>If $z = a + ib$, its conjugate is $\\bar{z} = a - ib$ (simply flip the sign of the imaginary part!).</p>
  <p>Properties: $\\overline{z_1 \\pm z_2} = \\bar{z}_1 \\pm \\bar{z}_2$, $\\overline{z_1 z_2} = \\bar{z}_1 \\bar{z}_2$, $\\overline{(\\bar{z})} = z$, and $\\mathbf{z \\bar{z} = a^2 + b^2 = |z|^2}$.</p>
</div>

<div class="definition">
  <strong>Modulus (Absolute Value) of a Complex Number</strong>
  <p>The modulus of $z = a + ib$ is the distance of point $(a, b)$ from the origin in the Argand plane:</p>
  <p>$$|z| = \\sqrt{a^2 + b^2} \\ge 0$$</p>
  <p>Properties: $|z_1 z_2| = |z_1||z_2|$, $\\left|\\frac{z_1}{z_2}\\right| = \\frac{|z_1|}{|z_2|}$, $|z| = |\\bar{z}| = |-z|$.</p>
</div>

<div class="concept-box">
  <h4>Multiplicative Inverse ($z^{-1}$)</h4>
  <p>The multiplicative inverse of non-zero $z$ is the number $z^{-1}$ such that $z \\cdot z^{-1} = 1$:</p>
  <p>$$z^{-1} = \\frac{1}{z} = \\frac{\\bar{z}}{z \\bar{z}} = \\frac{\\bar{z}}{|z|^2} = \\frac{a - ib}{a^2 + b^2}$$</p>
</div>

<!-- SECTION 5 -->
<h2 class="section-title" id="s5">[[ZAP]] 5. Argand Plane & Polar Representation</h2>

<div class="concept-box">
  <h4>The Argand Plane</h4>
  <p>Every complex number $z = a + ib$ uniquely corresponds to an ordered pair $(a, b)$ on a Cartesian coordinate plane:</p>
  <ul>
    <li>The horizontal axis is the <strong>Real axis</strong>.</li>
    <li>The vertical axis is the <strong>Imaginary axis</strong>.</li>
  </ul>
</div>

<div class="definition">
  <strong>Polar Form of a Complex Number</strong>
  <p>Let $r = |z| = \\sqrt{a^2 + b^2}$ and $\\theta = \\text{arg}(z)$. The polar representation is:</p>
  <p>$$z = r(\\cos \\theta + i\\sin \\theta)$$</p>
  <p>where $\\theta$ is the <strong>Principal Argument</strong>, restricted to the interval: $\\mathbf{-\\pi < \\theta \\le \\pi}$.</p>
</div>

<div class="types-grid">
  <div class="type-card">
    <h5>Step 1: Compute Acute Reference Angle $\\alpha$</h5>
    <p>$$\\tan \\alpha = \\left|\\frac{b}{a}\\right| \\implies \\alpha = \\tan^{-1}\\left|\\frac{b}{a}\\right|$$</p>
  </div>
  <div class="type-card">
    <h5>Step 2: Determine Quadrant & Assign $\\theta$</h5>
    <ul>
      <li><strong>Quadrant I ($a>0, b>0$):</strong> $\\theta = \\alpha$</li>
      <li><strong>Quadrant II ($a<0, b>0$):</strong> $\\theta = \\pi - \\alpha$</li>
      <li><strong>Quadrant III ($a<0, b<0$):</strong> $\\theta = -(\\pi - \\alpha) = -\\pi + \\alpha$</li>
      <li><strong>Quadrant IV ($a>0, b<0$):</strong> $\\theta = -\\alpha$</li>
    </ul>
  </div>
</div>

<!-- SECTION 6 -->
<h2 class="section-title" id="s6">[[ZAP]] 6. Quadratic Equations with Negative Discriminant</h2>

<div class="concept-box">
  <h4>Solving $ax^2 + bx + c = 0$ when $D < 0$</h4>
  <p>When the discriminant $D = b^2 - 4ac < 0$, the roots are not real, but complex conjugates:</p>
  <p>$$\\sqrt{D} = \\sqrt{-(4ac - b^2)} = i\\sqrt{4ac - b^2}$$</p>
  <p>$$x = \\frac{-b \\pm i\\sqrt{4ac - b^2}}{2a}$$</p>
</div>

<!-- SECTION 7 -->
<h2 class="section-title" id="s7">[[TARGET]] 7. Worked Examples — Easy to Hard</h2>

<!-- Ex 1 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 1: Simplifying Large Powers of $i$</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    Evaluate: (i) $i^{35}$, (ii) $i^{-39}$, (iii) $i^9 + i^{19}$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>(i) $i^{35}$:</strong> $35 = 4(8) + 3$. Thus $i^{35} = (i^4)^8 \\cdot i^3 = (1)^8 \\cdot (-i) = -i$.
    </div>
    <div class="step">
      <strong>(ii) $i^{-39}$:</strong> $\\frac{1}{i^{39}}$. Since $39 = 4(9) + 3$, $i^{39} = -i$. So $\\frac{1}{-i} = \\frac{i}{-i^2} = \\frac{i}{-(-1)} = i$.
    </div>
    <div class="step">
      <strong>(iii) $i^9 + i^{19}$:</strong> $i^9 = i^{4(2)+1} = i$. $i^{19} = i^{4(4)+3} = -i$. Sum $= i + (-i) = 0$.
    </div>
  </div>
</div>

<!-- Ex 2 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 2: Expressing in Standard $a + ib$ Form</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    Express $\\frac{5 + \\sqrt{2}i}{1 - \\sqrt{2}i}$ in the form $a + ib$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> Multiply numerator and denominator by conjugate of denominator $(1 + \\sqrt{2}i)$:
      $$\\frac{5 + \\sqrt{2}i}{1 - \\sqrt{2}i} \\times \\frac{1 + \\sqrt{2}i}{1 + \\sqrt{2}i} = \\frac{5 + 5\\sqrt{2}i + \\sqrt{2}i + (\\sqrt{2}i)^2}{1^2 - (\\sqrt{2}i)^2}$$
    </div>
    <div class="step">
      <strong>Step 2:</strong> Simplify: $(\\sqrt{2}i)^2 = 2i^2 = -2$, and denominator $= 1 - (-2) = 3$.
      $$\\frac{(5 - 2) + (5\\sqrt{2} + \\sqrt{2})i}{3} = \\frac{3 + 6\\sqrt{2}i}{3} = 1 + 2\\sqrt{2}i$$
    </div>
    <p><strong>Final Answer:</strong> $a = 1,\\; b = 2\\sqrt{2}$.</p>
  </div>
</div>

<!-- Ex 3 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 3: Multiplicative Inverse</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Find the multiplicative inverse of $z = 4 - 3i$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1:</strong> Find conjugate $\\bar{z} = 4 + 3i$.
    </div>
    <div class="step">
      <strong>Step 2:</strong> Find $|z|^2 = 4^2 + (-3)^2 = 16 + 9 = 25$.
    </div>
    <div class="step">
      <strong>Step 3:</strong> Compute inverse:
      $$z^{-1} = \\frac{\\bar{z}}{|z|^2} = \\frac{4 + 3i}{25} = \\frac{4}{25} + \\frac{3}{25}i$$
    </div>
  </div>
</div>

<!-- Ex 4 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 4: Converting to Polar Form</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Convert $z = -1 + i\\sqrt{3}$ into polar form.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Modulus $r$:</strong>
      $$r = |z| = \\sqrt{(-1)^2 + (\\sqrt{3})^2} = \\sqrt{1 + 3} = \\sqrt{4} = 2$$
    </div>
    <div class="step">
      <strong>Step 2: Acute angle $\\alpha$:</strong>
      $$\\tan \\alpha = \\left|\\frac{b}{a}\\right| = \\left|\\frac{\\sqrt{3}}{-1}\\right| = \\sqrt{3} \\implies \\alpha = \\frac{\\pi}{3}$$
    </div>
    <div class="step">
      <strong>Step 3: Principal Argument $\\theta$:</strong>
      Since $a = -1 < 0$ and $b = \\sqrt{3} > 0$, $z$ lies in <strong>Quadrant II</strong>.
      $$\\theta = \\pi - \\alpha = \\pi - \\frac{\\pi}{3} = \\frac{2\\pi}{3}$$
    </div>
    <div class="step">
      <strong>Step 4: Polar form:</strong>
      $$z = 2\\left(\\cos\\frac{2\\pi}{3} + i\\sin\\frac{2\\pi}{3}\\right)$$
    </div>
  </div>
</div>

<!-- Ex 5 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 5: Equality & Conjugate Application</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    If $x + iy = \\frac{a + ib}{a - ib}$, prove that $x^2 + y^2 = 1$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Method using Modulus:</strong>
      Take the modulus on both sides:
      $$|x + iy| = \\left|\\frac{a + ib}{a - ib}\\right|$$
    </div>
    <div class="step">
      <strong>Property of Modulus:</strong> $\\left|\\frac{z_1}{z_2}\\right| = \\frac{|z_1|}{|z_2|}$.
      $$\\sqrt{x^2 + y^2} = \\frac{|a + ib|}{|a - ib|} = \\frac{\\sqrt{a^2 + b^2}}{\\sqrt{a^2 + (-b)^2}} = \\frac{\\sqrt{a^2 + b^2}}{\\sqrt{a^2 + b^2}} = 1$$
    </div>
    <div class="step">
      <strong>Squaring both sides:</strong>
      $$x^2 + y^2 = 1^2 = 1$$
      <strong>Hence proved!</strong> (Much faster than expanding algebraically!)
    </div>
  </div>
</div>

<!-- Ex 6 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 6: Quadratic with Complex Coefficients</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    Solve the quadratic equation: $\\sqrt{2}x^2 + x + \\sqrt{2} = 0$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Compute discriminant:</strong>
      Here $a = \\sqrt{2}$, $b = 1$, $c = \\sqrt{2}$.
      $$D = b^2 - 4ac = 1^2 - 4(\\sqrt{2})(\\sqrt{2}) = 1 - 4(2) = 1 - 8 = -7$$
    </div>
    <div class="step">
      <strong>Step 2: Roots:</strong>
      Since $D = -7 < 0$, $\\sqrt{D} = \\sqrt{-7} = i\\sqrt{7}$.
      $$x = \\frac{-b \\pm \\sqrt{D}}{2a} = \\frac{-1 \\pm i\\sqrt{7}}{2\\sqrt{2}} = -\\frac{1}{2\\sqrt{2}} \\pm i\\frac{\\sqrt{7}}{2\\sqrt{2}}$$
    </div>
  </div>
</div>

<!-- SECTION 8 -->
<h2 class="section-title" id="s8">[[BOOK]] 8. NCERT Key Exercise Questions Solved</h2>

<div class="ncert-box">
  <h4>NCERT Exercise 4.1 — Question 11</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Find the multiplicative inverse of $-i$.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Let $z = -i = 0 - 1i$.</p>
        <p>Conjugate $\\bar{z} = 0 + 1i = i$.</p>
        <p>Modulus squared $|z|^2 = 0^2 + (-1)^2 = 1$.</p>
        <p>$$z^{-1} = \\frac{\\bar{z}}{|z|^2} = \\frac{i}{1} = i$$</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 4.2 / Polar Form Problem</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Convert $z = -1 - i$ into polar form.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>$r = \\sqrt{(-1)^2 + (-1)^2} = \\sqrt{2}$.</p>
        <p>$\\tan \\alpha = |-1 / -1| = 1 \\implies \\alpha = \\frac{\\pi}{4}$.</p>
        <p>Since both $a < 0$ and $b < 0$, $z$ is in <strong>Quadrant III</strong>:</p>
        <p>$$\\theta = -(\\pi - \\alpha) = -\\left(\\pi - \\frac{\\pi}{4}\\right) = -\\frac{3\\pi}{4}$$</p>
        <p>Polar form: $z = \\sqrt{2}\\left(\\cos\\left(-\\frac{3\\pi}{4}\\right) + i\\sin\\left(-\\frac{3\\pi}{4}\\right)\\right)$.</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Miscellaneous Exercise — Question 5</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Convert $\\frac{1 + 7i}{(2 - i)^2}$ into polar form.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>First expand denominator: $(2 - i)^2 = 4 - 4i + i^2 = 3 - 4i$.</p>
        <p>Simplify fraction: $\\frac{1 + 7i}{3 - 4i} \\times \\frac{3 + 4i}{3 + 4i} = \\frac{3 + 4i + 21i + 28i^2}{9 - 16i^2} = \\frac{-25 + 25i}{25} = -1 + i$.</p>
        <p>$r = \\sqrt{(-1)^2 + 1^2} = \\sqrt{2}$.</p>
        <p>$\\tan \\alpha = 1 \\implies \\alpha = \\frac{\\pi}{4}$. In Q2: $\\theta = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4}$.</p>
        <p>Polar form: $\\sqrt{2}\\left(\\cos\\frac{3\\pi}{4} + i\\sin\\frac{3\\pi}{4}\\right)$.</p>
      </div>
    </details>
  </div>
</div>

<!-- SECTION 9 -->
<h2 class="section-title" id="s9">[[ALERT]] 9. Common Exam Traps & Pitfalls</h2>

<div class="trap-card">
  <h4>[[ALERT]] Trap 1: The False Identity $\\sqrt{a} \\sqrt{b} = \\sqrt{ab}$</h4>
  <p>The rule $\\sqrt{a} \\sqrt{b} = \\sqrt{ab}$ is ONLY valid when at least one of $a$ or $b$ is non-negative! If both are negative: $\\sqrt{-1} \\sqrt{-1} = i \\cdot i = -1$. But $\\sqrt{(-1)(-1)} = \\sqrt{1} = 1$. Concluding that $-1 = 1$ is a catastrophic logical fallacy!</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 2: Incorrect Quadrant for Principal Argument</h4>
  <p>Many students compute $\\theta = \\tan^{-1}(b/a)$ blindly. For $-1 - i$, $\\frac{-1}{-1} = 1$, giving $\\theta = \\pi/4$. But $-1 - i$ is in Quadrant III, where $\\pi/4$ is in Quadrant I! Always sketch the point first to identify the quadrant.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 3: Imaginary Part Does NOT Include $i$</h4>
  <p>For $z = 3 + 4i$, $\\text{Im}(z) = 4$, NOT $4i$. Writing $\\text{Im}(z) = 4i$ will lose marks.</p>
</div>

<!-- SECTION 10 -->
<h2 class="section-title" id="s10">[[QUIZ]] 10. Quick Self-Check Quiz</h2>

<div class="quiz-card">
  <p><strong>Q1:</strong> What is the value of $i^{100} + i^{101} + i^{102} + i^{103}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">0. The sum of four consecutive powers of $i$ is always zero ($1 + i - 1 - i = 0$).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q2:</strong> What is the conjugate of the complex number $5$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">5. Since $5 = 5 + 0i$, its conjugate is $5 - 0i = 5$. A real number is its own conjugate!</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q3:</strong> What is the modulus of $\\frac{1 + i}{1 - i}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">1. $|(1+i)/(1-i)| = |1+i| / |1-i| = \\sqrt{2}/\\sqrt{2} = 1$. (Also, $(1+i)/(1-i) = i$, and $|i| = 1$).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q4:</strong> In which quadrant does the principal argument of $-3 - 4i$ lie?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Quadrant III (both real and imaginary parts are negative). The argument is in $(-\\pi, -\\pi/2)$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q5:</strong> Solve for real $x, y$: $(x + 2y) + i(2x - 3y) = 5 - 4i$.</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Equating parts: $x + 2y = 5$ and $2x - 3y = -4$. Multiply first eq by 2: $2x + 4y = 10$. Subtract: $7y = 14 \\implies y = 2$. Then $x = 5 - 2(2) = 1$. So $x = 1, y = 2$.</div></details>
</div>
"""

out = wrap("Complex Numbers", 4, "Chapter_3_Trigonometric_Functions.html", "Chapter_5_Linear_Inequalities.html", ch4)
with open(os.path.join(BASE_DIR, "Chapter_4_Complex_Numbers.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Chapter 4 written successfully!")
print("File size:", os.path.getsize(os.path.join(BASE_DIR, "Chapter_4_Complex_Numbers.html")), "bytes")
