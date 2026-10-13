import os
from builder_common import BASE_DIR, wrap, si

ch7 = """
<div class="header-card">
  <span class="badge">NCERT Chapter 7</span>
  <h1>Binomial Theorem</h1>
  <p>Expand any power $(a + b)^n$ effortlessly: from Pascal's triangle to the general term, middle terms, and divisibility proofs.</p>
  <div class="stats-row">
    <span>[[CLOCK]] ~40 min read</span>
    <span>[[TARGET]] 4–6 marks in exam</span>
    <span>[[BOOK]] <a href="../kemh107.pdf">kemh107.pdf</a></span>
  </div>
</div>

<div class="toc">
  <h3>[[INFO]] What you will learn in this chapter</h3>
  <ol>
    <li><a href="#s1">Introduction & The Geometry of Pascal's Triangle</a></li>
    <li><a href="#s2">The Binomial Theorem Statement & Core Formula</a></li>
    <li><a href="#s3">Important Special Expansions & Coefficient Properties</a></li>
    <li><a href="#s4">General Term Formula ($T_{r+1}$)</a></li>
    <li><a href="#s5">Finding the Middle Term(s) (Even vs Odd $n$)</a></li>
    <li><a href="#s6">Term Independent of $x$ & Divisibility Proofs</a></li>
    <li><a href="#s7">Worked Examples — Easy to Hard</a></li>
    <li><a href="#s8">NCERT Key Exercise Questions Solved</a></li>
    <li><a href="#s9">Common Exam Traps & Pitfalls</a></li>
    <li><a href="#s10">Quick Self-Check Quiz</a></li>
  </ol>
</div>

<!-- SECTION 1 -->
<h2 class="section-title" id="s1">[[ZAP]] 1. Pascal's Triangle & Motivation</h2>

<div class="concept-box">
  <h4>Why We Need the Binomial Theorem</h4>
  <p>We all know $(a + b)^2 = a^2 + 2ab + b^2$ and $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$. But what if an exam asks you to calculate $(a + b)^{10}$ or evaluate $(99)^5$? Multiplying brackets 10 times by hand would take hours. The Binomial Theorem gives an exact algebraic shortcut for any power $n$.</p>
</div>

<div class="concept-box">
  <h4>Pascal's Triangle Pattern</h4>
  <p>Arranging the coefficients of $(a+b)^n$ for $n = 0, 1, 2, 3, 4, 5$ produces a triangle where each number is the sum of the two numbers directly above it:</p>
  <pre style="background:#0f172a; color:#7dd3fc; padding:1rem; border-radius:8px; font-family:monospace; line-height:1.6; font-size:0.95rem;">
n = 0:                  1
n = 1:               1     1
n = 2:            1     2     1
n = 3:         1     3     3     1
n = 4:      1     4     6     4     1
n = 5:   1     5    10    10     5     1
  </pre>
  <p>Notice that row $n$ consists of combinations: $^nC_0, ^nC_1, ^nC_2, \\dots, ^nC_n$.</p>
  <p>Because $^nC_r + ^nC_{r-1} = ^{n+1}C_r$, every entry is the sum of the two above it!</p>
</div>

<!-- SECTION 2 -->
<h2 class="section-title" id="s2">[[ZAP]] 2. The Binomial Theorem Statement</h2>

<div class="definition">
  <strong>Theorem: Binomial Theorem for Any Positive Integer $n$</strong>
  <p>$$(a + b)^n = ^nC_0 a^n + ^nC_1 a^{n-1}b + ^nC_2 a^{n-2}b^2 + \\dots + ^nC_r a^{n-r}b^r + \\dots + ^nC_n b^n$$</p>
  <p>In summation sigma notation:</p>
  <p>$$(a + b)^n = \\sum_{k=0}^n {^nC_k} a^{n-k} b^k$$</p>
</div>

<div class="concept-box">
  <h4>3 Golden Observations You Must Remember</h4>
  <ol>
    <li><strong>Number of Terms:</strong> The expansion of $(a + b)^n$ contains exactly $\\mathbf{n + 1}$ terms. (E.g. $(x+y)^7$ has $7 + 1 = 8$ terms).</li>
    <li><strong>Conservation of Powers:</strong> In every single term, the power of $a$ decreases from $n$ to $0$, the power of $b$ increases from $0$ to $n$, and the sum of exponents is ALWAYS $n$: $(n - r) + r = n$.</li>
    <li><strong>Symmetry of Coefficients:</strong> Coefficients of terms equidistant from the beginning and end are equal, because $^nC_r = ^nC_{n - r}$.</li>
  </ol>
</div>

<!-- SECTION 3 -->
<h2 class="section-title" id="s3">[[ZAP]] 3. Special Expansions & Coefficient Identities</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>Expansion of $(a - b)^n$</h5>
    <p>Replace $b$ with $(-b)$. The signs alternate strictly ($+$, $-$, $+$, $-$, ...):</p>
    <p>$$(a - b)^n = ^nC_0 a^n - ^nC_1 a^{n-1}b + ^nC_2 a^{n-2}b^2 - \\dots + (-1)^n ^nC_n b^n$$</p>
  </div>
  <div class="type-card">
    <h5>Expansion of $(1 + x)^n$</h5>
    <p>Set $a = 1$ and $b = x$:</p>
    <p>$$(1 + x)^n = 1 + ^nC_1 x + ^nC_2 x^2 + ^nC_3 x^3 + \\dots + ^nC_n x^n$$</p>
  </div>
  <div class="type-card">
    <h5>Sum of All Binomial Coefficients</h5>
    <p>Plug $x = 1$ into $(1 + x)^n$:</p>
    <p>$$^nC_0 + ^nC_1 + ^nC_2 + \\dots + ^nC_n = (1 + 1)^n = \\mathbf{2^n}$$</p>
  </div>
  <div class="type-card">
    <h5>Sum of Odd = Sum of Even Coefficients</h5>
    <p>Plug $x = -1$ into $(1 + x)^n$:</p>
    <p>$$^nC_0 + ^nC_2 + ^nC_4 + \\dots = ^nC_1 + ^nC_3 + ^nC_5 + \\dots = \\mathbf{2^{n-1}}$$</p>
  </div>
</div>

<!-- SECTION 4 -->
<h2 class="section-title" id="s4">[[ZAP]] 4. The General Term Formula ($T_{r+1}$)</h2>

<div class="definition">
  <strong>The General Term Formula</strong>
  <p>The $(r + 1)$-th term in the expansion of $(a + b)^n$ is denoted by $T_{r+1}$:</p>
  <p>$$\\mathbf{T_{r+1} = ^nC_r \\cdot a^{n - r} \\cdot b^r}$$</p>
</div>

<div class="concept-box">
  <h4>Crucial Off-By-One Warning!</h4>
  <p>Remember that the index $r$ is always <strong>ONE LESS</strong> than the term number:</p>
  <ul>
    <li>1st term: $r = 0 \\implies T_1 = ^nC_0 a^n b^0$</li>
    <li>4th term: $r = 3 \\implies T_4 = ^nC_3 a^{n-3} b^3$</li>
    <li>10th term: $r = 9 \\implies T_{10} = ^nC_9 a^{n-9} b^9$</li>
  </ul>
</div>

<!-- SECTION 5 -->
<h2 class="section-title" id="s5">[[ZAP]] 5. Finding Middle Terms</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>Case 1: When $n$ is EVEN</h5>
    <p>The total number of terms $(n + 1)$ is ODD. Therefore, there is <strong>EXACTLY ONE</strong> middle term:</p>
    <p>$$\\text{Middle Term} = T_{\\frac{n}{2} + 1}$$</p>
    <p><em>Example:</em> For $(x + y)^8$, $n = 8$ is even. Middle term is $T_{8/2 + 1} = T_5$.</p>
  </div>
  <div class="type-card">
    <h5>Case 2: When $n$ is ODD</h5>
    <p>The total number of terms $(n + 1)$ is EVEN. Therefore, there are <strong>TWO</strong> middle terms:</p>
    <p>$$\\text{Middle Terms} = T_{\\frac{n + 1}{2}} \\quad \\text{and} \\quad T_{\\frac{n + 3}{2}}$$</p>
    <p><em>Example:</em> For $(x + y)^7$, $n = 7$ is odd. Middle terms are $T_4$ and $T_5$.</p>
  </div>
</div>

<!-- SECTION 6 -->
<h2 class="section-title" id="s6">[[ZAP]] 6. Term Independent of $x$ & Divisibility Proofs</h2>

<div class="concept-box">
  <h4>1. Term Independent of $x$ (Constant Term)</h4>
  <p>To find the term containing no $x$ (i.e. $x^0$):</p>
  <ol>
    <li>Write out the general term $T_{r+1} = ^nC_r a^{n-r} b^r$.</li>
    <li>Collect all powers of $x$ into a single exponent: $x^{f(r)}$.</li>
    <li>Set the exponent $f(r) = 0$ and solve for integer $r$.</li>
    <li>Substitute that $r$ back into $T_{r+1}$ to obtain the numerical constant value.</li>
  </ol>
</div>

<div class="concept-box">
  <h4>2. Divisibility Questions</h4>
  <p>To prove an expression like $9^{n+1} - 8n - 9$ is divisible by $64$ ($= 8^2$):</p>
  <p>Write base $9$ as $(1 + 8)$ and expand using Binomial Theorem:</p>
  <p>$$9^{n+1} = (1 + 8)^{n+1} = ^{n+1}C_0 + ^{n+1}C_1(8) + ^{n+1}C_2(8)^2 + ^{n+1}C_3(8)^3 + \\dots$$</p>
  <p>$$= 1 + (n + 1)(8) + 64 \\cdot \\left[^{n+1}C_2 + ^{n+1}C_3(8) + \\dots\\right]$$</p>
  <p>$$= 1 + 8n + 8 + 64k = 8n + 9 + 64k$$</p>
  <p>Subtracting $8n + 9$: $9^{n+1} - 8n - 9 = 64k$, which is clearly divisible by $64$!</p>
</div>

<!-- SECTION 7 -->
<h2 class="section-title" id="s7">[[TARGET]] 7. Worked Examples — Easy to Hard</h2>

<!-- Ex 1 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 1: Full Expansion of a Binomial</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    Expand $\\left(x^2 + \\frac{3}{x}\\right)^4$, $x \\ne 0$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Write expansion with $n = 4$:</strong>
      $$\\left(x^2 + \\frac{3}{x}\\right)^4 = ^4C_0 (x^2)^4 + ^4C_1 (x^2)^3\\left(\\frac{3}{x}\\right) + ^4C_2 (x^2)^2\\left(\\frac{3}{x}\\right)^2 + ^4C_3 (x^2)\\left(\\frac{3}{x}\\right)^3 + ^4C_4 \\left(\\frac{3}{x}\\right)^4$$
    </div>
    <div class="step">
      <strong>Step 2: Evaluate coefficients and powers:</strong>
      <ul>
        <li>$^4C_0 (x^2)^4 = 1 \\cdot x^8 = x^8$</li>
        <li>$^4C_1 (x^2)^3 \\left(\\frac{3}{x}\\right) = 4 x^6 \\left(\\frac{3}{x}\\right) = 12 x^5$</li>
        <li>$^4C_2 (x^2)^2 \\left(\\frac{9}{x^2}\\right) = 6 x^4 \\left(\\frac{9}{x^2}\\right) = 54 x^2$</li>
        <li>$^4C_3 (x^2) \\left(\\frac{27}{x^3}\\right) = 4 x^2 \\left(\\frac{27}{x^3}\\right) = \\frac{108}{x}$</li>
        <li>$^4C_4 \\left(\\frac{81}{x^4}\\right) = \\frac{81}{x^4}$</li>
      </ul>
    </div>
    <p><strong>Final Expansion:</strong> $x^8 + 12x^5 + 54x^2 + \\frac{108}{x} + \\frac{81}{x^4}$.</p>
  </div>
</div>

<!-- Ex 2 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 2: Evaluating Numerical Power $(98)^5$</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    Using binomial theorem, evaluate $(98)^5$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Write $98$ as $(100 - 2)$:</strong>
      $$(98)^5 = (100 - 2)^5 = ^5C_0(100)^5 - ^5C_1(100)^4(2) + ^5C_2(100)^3(2^2) - ^5C_3(100)^2(2^3) + ^5C_4(100)(2^4) - ^5C_5(2^5)$$
    </div>
    <div class="step">
      <strong>Step 2: Calculate each term:</strong>
      <ul>
        <li>$= 10,000,000,000$</li>
        <li>$- 5 \\times 100,000,000 \\times 2 = -1,000,000,000$</li>
        <li>$+ 10 \\times 1,000,000 \\times 4 = +40,000,000$</li>
        <li>$- 10 \\times 10,000 \\times 8 = -800,000$</li>
        <li>$+ 5 \\times 100 \\times 16 = +8,000$</li>
        <li>$- 32$</li>
      </ul>
    </div>
    <div class="step">
      <strong>Step 3: Combine:</strong>
      $$10,040,008,000 - 1,000,800,032 = 9,039,207,968$$
    </div>
  </div>
</div>

<!-- Ex 3 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 3: Finding a Specific Term ($13\\text{th}$ Term)</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Find the $13\\text{th}$ term in the expansion of $\\left(9x - \\frac{1}{3\\sqrt{x}}\\right)^{18}$, $x \\ne 0$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Formula for $T_{13}$ ($r = 12$):</strong>
      $$T_{13} = T_{12 + 1} = ^{18}C_{12} (9x)^{18 - 12} \\left(-\\frac{1}{3\\sqrt{x}}\\right)^{12}$$
    </div>
    <div class="step">
      <strong>Step 2: Simplify powers:</strong>
      Notice $(-1)^{12} = +1$.
      $$(9x)^6 = (3^2)^6 x^6 = 3^{12} x^6$$
      $$\\left(\\frac{1}{3\\sqrt{x}}\\right)^{12} = \\frac{1}{3^{12} (x^{1/2})^{12}} = \\frac{1}{3^{12} x^6}$$
    </div>
    <div class="step">
      <strong>Step 3: Cancel factors:</strong>
      $$T_{13} = ^{18}C_{12} \\cdot 3^{12} x^6 \\cdot \\frac{1}{3^{12} x^6} = ^{18}C_{12} = ^{18}C_6$$
      $$= \\frac{18 \\times 17 \\times 16 \\times 15 \\times 14 \\times 13}{6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1} = 18,564$$
    </div>
  </div>
</div>

<!-- Ex 4 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 4: Term Independent of $x$</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    Find the term independent of $x$ in the expansion of $\\left(\\frac{3x^2}{2} - \\frac{1}{3x}\\right)^9$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Write General Term $T_{r+1}$:</strong>
      $$T_{r+1} = ^9C_r \\left(\\frac{3x^2}{2}\\right)^{9-r} \\left(-\\frac{1}{3x}\\right)^r$$
      $$= ^9C_r \\left(\\frac{3}{2}\\right)^{9-r} \\left(-\\frac{1}{3}\\right)^r (x^2)^{9-r} (x^{-1})^r$$
      $$= ^9C_r \\left(\\frac{3}{2}\\right)^{9-r} \\left(-\\frac{1}{3}\\right)^r x^{18 - 2r - r} = ^9C_r \\left(\\frac{3}{2}\\right)^{9-r} \\left(-\\frac{1}{3}\\right)^r x^{18 - 3r}$$
    </div>
    <div class="step">
      <strong>Step 2: Set power of $x$ to $0$:</strong>
      $$18 - 3r = 0 \\implies 3r = 18 \\implies r = 6$$
    </div>
    <div class="step">
      <strong>Step 3: Calculate $T_7$:</strong>
      $$T_7 = ^9C_6 \\left(\\frac{3}{2}\\right)^{9-6} \\left(-\\frac{1}{3}\\right)^6 = ^9C_3 \\left(\\frac{3}{2}\\right)^3 \\left(\\frac{1}{3^6}\\right)$$
      $$= 84 \\times \\frac{27}{8} \\times \\frac{1}{729} = 84 \\times \\frac{1}{8 \\times 27} = \\frac{84}{216} = \\frac{7}{18}$$
    </div>
    <p><strong>Final Answer:</strong> $\\frac{7}{18}$ (the 7th term).</p>
  </div>
</div>

<!-- Ex 5 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 5: Finding Middle Term</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Find the middle term in the expansion of $\\left(\\frac{x}{3} + 9y\\right)^{10}$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Identify middle term index:</strong>
      Here $n = 10$ is even. There is 1 middle term:
      $$\\text{Middle term} = T_{\\frac{10}{2} + 1} = T_6 \\quad (\\text{so } r = 5)$$
    </div>
    <div class="step">
      <strong>Step 2: Evaluate $T_6$:</strong>
      $$T_6 = ^{10}C_5 \\left(\\frac{x}{3}\\right)^{10-5} (9y)^5 = ^{10}C_5 \\frac{x^5}{3^5} \\cdot (3^2)^5 y^5 = ^{10}C_5 \\frac{x^5}{3^5} \\cdot 3^{10} y^5$$
      $$= ^{10}C_5 \\cdot 3^5 x^5 y^5 = 252 \\times 243 \\times x^5 y^5 = 61,236 x^5 y^5$$
    </div>
  </div>
</div>

<!-- SECTION 8 -->
<h2 class="section-title" id="s8">[[BOOK]] 8. NCERT Key Exercise Questions Solved</h2>

<div class="ncert-box">
  <h4>NCERT Exercise 7.1 — Question 10</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Using Binomial Theorem, indicate which number is larger: $(1.1)^{10000}$ or $1000$.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Write $1.1 = (1 + 0.1)$. Expand first two terms of $(1 + 0.1)^{10000}$:</p>
        <p>$$(1 + 0.1)^{10000} = ^{10000}C_0 + ^{10000}C_1(0.1) + \\text{other positive terms}$$</p>
        <p>$$= 1 + 10000(0.1) + \\text{positive terms}$$</p>
        <p>$$= 1 + 1000 + \\text{positive terms} = 1001 + \\text{positive terms} > 1000$$</p>
        <p><strong>Conclusion: $(1.1)^{10000}$ is strictly larger than $1000$.</strong></p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 7.1 — Question 11</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Find $(a + b)^4 - (a - b)^4$. Hence, evaluate $(\\sqrt{3} + \\sqrt{2})^4 - (\\sqrt{3} - \\sqrt{2})^4$.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>$(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$.</p>
        <p>$(a - b)^4 = a^4 - 4a^3b + 6a^2b^2 - 4ab^3 + b^4$.</p>
        <p>Subtracting: $(a + b)^4 - (a - b)^4 = 2[4a^3b + 4ab^3] = 8ab(a^2 + b^2)$.</p>
        <p>Substitute $a = \\sqrt{3}$ and $b = \\sqrt{2}$:</p>
        <p>$$8(\\sqrt{3})(\\sqrt{2})((\\sqrt{3})^2 + (\\sqrt{2})^2) = 8\\sqrt{6}(3 + 2) = 8\\sqrt{6}(5) = 40\\sqrt{6}$$</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 7.1 — Question 13</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Show that $9^{n+1} - 8n - 9$ is divisible by 64, whenever $n$ is a positive integer.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Write $9 = 1 + 8$:</p>
        <p>$$9^{n+1} = (1 + 8)^{n+1} = ^{n+1}C_0 + ^{n+1}C_1(8) + ^{n+1}C_2(8^2) + ^{n+1}C_3(8^3) + \\dots + ^{n+1}C_{n+1}(8^{n+1})$$</p>
        <p>$$= 1 + (n+1)8 + 64[^{n+1}C_2 + ^{n+1}C_3(8) + \\dots]$$</p>
        <p>$$= 1 + 8n + 8 + 64k = 8n + 9 + 64k$$</p>
        <p>$$9^{n+1} - 8n - 9 = 64k$$</p>
        <p>Since $k$ is an integer, $9^{n+1} - 8n - 9$ is divisible by 64. <strong>Hence proved!</strong></p>
      </div>
    </details>
  </div>
</div>

<!-- SECTION 9 -->
<h2 class="section-title" id="s9">[[ALERT]] 9. Common Exam Traps & Pitfalls</h2>

<div class="trap-card">
  <h4>[[ALERT]] Trap 1: The Off-By-One Error in $T_{r+1}$</h4>
  <p>To find the 5th term, DO NOT set $r = 5$! The 5th term is $T_{4+1}$, so $r = 4$. Setting $r = 5$ gives the 6th term and earns zero marks.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 2: Middle Term Index When $n$ is Odd</h4>
  <p>When $n = 9$ (odd), students think the middle term is $9/2 = 4.5$. Remember: an expansion with $n=9$ has $9+1 = 10$ terms, so there are TWO middle terms: the 5th and 6th terms ($T_{(9+1)/2} = T_5$ and $T_{(9+3)/2} = T_6$).</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 3: Dropping the Negative Sign in Alternating Expansions</h4>
  <p>In $(x - 2y)^6$, the second term $b$ is $(-2y)$. When taking $b^r$, remember $(-2y)^r = (-1)^r 2^r y^r$. If $r$ is odd, the term is negative!</p>
</div>

<!-- SECTION 10 -->
<h2 class="section-title" id="s10">[[QUIZ]] 10. Quick Self-Check Quiz</h2>

<div class="quiz-card">
  <p><strong>Q1:</strong> How many terms are there in the expansion of $(2x - 3y)^{14}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$14 + 1 = 15$ terms.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q2:</strong> What is the sum of coefficients in the expansion of $(1 - x)^{10}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Put $x = 1$: $(1 - 1)^{10} = 0^{10} = 0$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q3:</strong> Which term is the middle term in the expansion of $(x + a)^{12}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Since $n = 12$ is even, the middle term is $T_{12/2 + 1} = T_7$ (the 7th term).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q4:</strong> What is the coefficient of $x^0$ (constant term) in $(x + 1/x)^2$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$(x + 1/x)^2 = x^2 + 2(x)(1/x) + 1/x^2 = x^2 + 2 + 1/x^2$. The constant term is $2$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q5:</strong> What is the value of $^{15}C_0 + ^{15}C_1 + ^{15}C_2 + \dots + ^{15}C_{15}$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$2^{15} = 32,768$.</div></details>
</div>
"""

out = wrap("Binomial Theorem", 7, "Chapter_6_Permutations_and_Combinations.html", None, ch7)
with open(os.path.join(BASE_DIR, "Chapter_7_Binomial_Theorem.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Chapter 7 written successfully!")
print("File size:", os.path.getsize(os.path.join(BASE_DIR, "Chapter_7_Binomial_Theorem.html")), "bytes")
