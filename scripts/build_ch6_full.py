import os
from builder_common import BASE_DIR, wrap, si

ch6 = """
<div class="header-card">
  <span class="badge">NCERT Chapter 6</span>
  <h1>Permutations & Combinations</h1>
  <p>Learn the art of counting without listing: from the fundamental counting principle and factorials to arrangements and selections.</p>
  <div class="stats-row">
    <span>[[CLOCK]] ~50 min read</span>
    <span>[[TARGET]] 6–8 marks in exam</span>
    <span>[[BOOK]] <a href="../kemh106.pdf">kemh106.pdf</a></span>
  </div>
</div>

<div class="toc">
  <h3>[[INFO]] What you will learn in this chapter</h3>
  <ol>
    <li><a href="#s1">Fundamental Principles of Counting (Multiplication & Addition)</a></li>
    <li><a href="#s2">Factorial Notation & Why $0! = 1$</a></li>
    <li><a href="#s3">Permutations ($^nP_r$) — When Order Matters</a></li>
    <li><a href="#s4">Permutations of Identical Objects (Multiset Formula)</a></li>
    <li><a href="#s5">Key Arrangement Strategies: Tie-Together & Gap Methods</a></li>
    <li><a href="#s6">Combinations ($^nC_r$) — When Order Does NOT Matter</a></li>
    <li><a href="#s7">Core Identities of $^nC_r$ & Geometric Applications</a></li>
    <li><a href="#s8">Worked Examples — Easy to Hard</a></li>
    <li><a href="#s9">NCERT Key Exercise Questions Solved</a></li>
    <li><a href="#s10">Common Exam Traps & Quick Self-Check Quiz</a></li>
  </ol>
</div>

<!-- SECTION 1 -->
<h2 class="section-title" id="s1">[[ZAP]] 1. Fundamental Principles of Counting</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>The Multiplication Principle (AND)</h5>
    <p>If an event can occur in $m$ different ways, following which a second event can occur in $n$ different ways, then the total number of ways both events can occur in sequence is:</p>
    <p>$$\\mathbf{m \\times n}$$</p>
    <p><em>Example:</em> You have 3 shirts and 2 pants. Total outfits $= 3 \\times 2 = 6$.</p>
  </div>
  <div class="type-card">
    <h5>The Addition Principle (OR)</h5>
    <p>If event $A$ can occur in $m$ ways and event $B$ can occur in $n$ ways, and they <strong>cannot occur simultaneously</strong> (mutually exclusive), then either $A$ OR $B$ can occur in:</p>
    <p>$$\\mathbf{m + n} \\quad \\text{ways}$$</p>
    <p><em>Example:</em> You can choose 1 coffee out of 4 kinds OR 1 tea out of 3 kinds $= 4 + 3 = 7$ choices.</p>
  </div>
</div>

<div class="concept-box">
  <h4>Repetition Allowed vs Repetition Not Allowed</h4>
  <p>Consider forming a 3-digit number using digits $\\{1, 2, 3, 4, 5\\}$:</p>
  <ul>
    <li><strong>When repetition IS allowed:</strong> Each of the 3 positions has 5 choices: $5 \\times 5 \\times 5 = 5^3 = 125$ numbers.</li>
    <li><strong>When repetition is NOT allowed:</strong> 1st digit has 5 choices, 2nd has 4 choices, 3rd has 3 choices: $5 \\times 4 \\times 3 = 60$ numbers.</li>
  </ul>
</div>

<!-- SECTION 2 -->
<h2 class="section-title" id="s2">[[ZAP]] 2. Factorial Notation & Why $0! = 1$</h2>

<div class="definition">
  <strong>Definition: Factorial Notation ($n!$)</strong>
  <p>For any positive integer $n$, the product of the first $n$ natural numbers is denoted by $n!$ (read "$n$ factorial"):</p>
  <p>$$n! = n \\times (n - 1) \\times (n - 2) \\times \\dots \\times 3 \\times 2 \\times 1$$</p>
  <p>Recursive property: $n! = n \\times (n - 1)!$.</p>
</div>

<div class="concept-box">
  <h4>Values of First Few Factorials (Memorize These!)</h4>
  <p>$$0! = 1, \\quad 1! = 1, \\quad 2! = 2, \\quad 3! = 6, \\quad 4! = 24, \\quad 5! = 120, \\quad 6! = 720, \\quad 7! = 5040$$</p>
  <h4>Why is $0! = 1$?</h4>
  <p>Using the identity $(n - 1)! = \\frac{n!}{n}$, plug in $n = 1$:</p>
  <p>$$(1 - 1)! = \\frac{1!}{1} \\implies 0! = \\frac{1}{1} = 1$$</p>
  <p><em>Intuitive reason:</em> There is exactly 1 way to arrange zero objects: leave the space empty!</p>
</div>

<!-- SECTION 3 -->
<h2 class="section-title" id="s3">[[ZAP]] 3. Permutations ($^nP_r$) — Order Matters!</h2>

<div class="definition">
  <strong>Definition of Permutation</strong>
  <p>A <strong>permutation</strong> is an arrangement in a definite order of a number of objects taken some or all at a time.</p>
  <p>The number of permutations of $n$ distinct objects taken $r$ at a time ($0 \\le r \\le n$) without repetition is:</p>
  <p>$$^nP_r = \\frac{n!}{(n - r)!} = n(n - 1)(n - 2)\\dots(n - r + 1)$$</p>
  <p>Special values: $^nP_n = n!$, $^nP_0 = 1$, $^nP_1 = n$.</p>
</div>

<!-- SECTION 4 -->
<h2 class="section-title" id="s4">[[ZAP]] 4. Permutations of Objects Not All Distinct</h2>

<div class="concept-box">
  <h4>The Multiset Permutation Formula</h4>
  <p>The number of permutations of $n$ objects, where $p_1$ objects are of one kind, $p_2$ are of second kind, ..., and $p_k$ are of $k$-th kind is:</p>
  <p>$$\\mathbf{\\frac{n!}{p_1! \\cdot p_2! \\dots p_k!}}$$</p>
  <p><strong>Classic Example (ROOT):</strong> The word ROOT has 4 letters where O repeats 2 times. Total arrangements $= \\frac{4!}{2!} = \\frac{24}{2} = 12$.</p>
  <p><strong>Classic Example (MISSISSIPPI):</strong> 11 letters total (1 M, 4 I, 4 S, 2 P). Total ways $= \\frac{11!}{4! \\cdot 4! \\cdot 2!} = 34,650$.</p>
</div>

<!-- SECTION 5 -->
<h2 class="section-title" id="s5">[[ZAP]] 5. Master Arrangement Strategies</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>Strategy A: The "Tie-Together" (String) Method</h5>
    <p>Use when certain objects <strong>must always be together</strong>.</p>
    <ol>
      <li>Tie the required items into a single bundle/block.</li>
      <li>Treat that block as 1 giant item. Count permutations of the items including the block.</li>
      <li>Multiply by the internal permutations within the block!</li>
    </ol>
  </div>
  <div class="type-card">
    <h5>Strategy B: The "Gap" Method</h5>
    <p>Use when certain objects <strong>must NEVER be together</strong>.</p>
    <ol>
      <li>Arrange the unrestricted items first (say $k$ items in $k!$ ways).</li>
      <li>These $k$ items create $k + 1$ available "gaps" (spaces before, between, and after them).</li>
      <li>Place the restricted items into these gaps using combinations/permutations. No two will ever sit together!</li>
    </ol>
  </div>
</div>

<!-- SECTION 6 -->
<h2 class="section-title" id="s6">[[ZAP]] 6. Combinations ($^nC_r$) — Order Does NOT Matter</h2>

<div class="concept-box">
  <h4>Permutation vs Combination</h4>
  <p>Think about a cricket team: Choosing 11 players out of 15 is a <strong>Combination</strong> (it doesn't matter who was picked first). But assigning batting positions 1 to 11 is a <strong>Permutation</strong> (order changes the lineup completely!).</p>
</div>

<div class="definition">
  <strong>Definition of Combination</strong>
  <p>The number of combinations (selections) of $n$ different objects taken $r$ at a time is:</p>
  <p>$$^nC_r = \\frac{n!}{r!(n - r)!} = \\frac{^nP_r}{r!}$$</p>
</div>

<!-- SECTION 7 -->
<h2 class="section-title" id="s7">[[ZAP]] 7. Core Properties of $^nC_r$ & Geometric Formulas</h2>

<div class="concept-box">
  <h4>Properties of Combinations</h4>
  <ul>
    <li><strong>Symmetry:</strong> $^nC_r = ^nC_{n - r}$. (Choosing who stays is the same as choosing who leaves! E.g. $^{10}C_8 = ^{10}C_2 = 45$).</li>
    <li><strong>Equality Condition:</strong> If $^nC_a = ^nC_b$, then either $a = b$ or $\\mathbf{a + b = n}$.</li>
    <li><strong>Pascal's Identity:</strong> $^nC_r + ^nC_{r - 1} = ^{n+1}C_r$.</li>
    <li><strong>Sum of All Combinations:</strong> $^nC_0 + ^nC_1 + ^nC_2 + \\dots + ^nC_n = 2^n$.</li>
  </ul>
</div>

<div class="types-grid">
  <div class="type-card">
    <h5>Number of Diagonals in an $n$-gon</h5>
    <p>Selecting any 2 vertices gives a line segment ($^nC_2$). Subtracting the $n$ perimeter sides gives the diagonals:</p>
    <p>$$\\text{Diagonals} = ^nC_2 - n = \\frac{n(n - 3)}{2}$$</p>
  </div>
  <div class="type-card">
    <h5>Collinear Points & Lines / Triangles</h5>
    <p>From $n$ points where $m$ are collinear:</p>
    <p>$$\\text{Lines} = ^nC_2 - ^mC_2 + 1$$</p>
    <p>$$\\text{Triangles} = ^nC_3 - ^mC_3$$</p>
  </div>
</div>

<!-- SECTION 8 -->
<h2 class="section-title" id="s8">[[TARGET]] 8. Worked Examples — Easy to Hard</h2>

<!-- Ex 1 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 1: Factorial Equation</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    If $\\frac{1}{6!} + \\frac{1}{7!} = \\frac{x}{8!}$, find $x$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Express factorials in terms of the smallest factorial ($6!$):</strong>
      $$\\frac{1}{6!} + \\frac{1}{7 \\times 6!} = \\frac{x}{8 \\times 7 \\times 6!}$$
    </div>
    <div class="step">
      <strong>Step 2: Multiply both sides by $6!$:</strong>
      $$1 + \\frac{1}{7} = \\frac{x}{56} \\implies \\frac{8}{7} = \\frac{x}{56}$$
    </div>
    <div class="step">
      <strong>Step 3: Solve for $x$:</strong>
      $$x = \\frac{8 \\times 56}{7} = 8 \\times 8 = 64$$
    </div>
  </div>
</div>

<!-- Ex 2 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 2: Words Formed with Repeating Letters</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    How many different words (with or without meaning) can be formed using all letters of the word <strong>MATHEMATICS</strong>?
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Count letter frequencies:</strong>
      Total letters $n = 11$.
      Frequencies: M appears 2 times, A appears 2 times, T appears 2 times, H: 1, E: 1, I: 1, C: 1, S: 1.
    </div>
    <div class="step">
      <strong>Step 2: Apply multiset formula:</strong>
      $$\\text{Total words} = \\frac{11!}{2! \\cdot 2! \\cdot 2!} = \\frac{39,916,800}{8} = 4,989,600$$
    </div>
  </div>
</div>

<!-- Ex 3 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 3: Vowels Always Together (Tie-Together Method)</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Find the number of arrangements of the letters of the word <strong>DAUGHTER</strong> such that all vowels are always together.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Identify vowels and consonants:</strong>
      Word has 8 letters: Vowels are $\\{A, U, E\\}$ (3 vowels). Consonants are $\\{D, G, H, T, R\\}$ (5 consonants).
    </div>
    <div class="step">
      <strong>Step 2: Tie vowels into a single block $[AUE]$:</strong>
      Now we have 5 consonants + 1 block $= 6$ objects.
      Number of ways to arrange these 6 objects $= 6! = 720$.
    </div>
    <div class="step">
      <strong>Step 3: Arrange vowels inside the block:</strong>
      The 3 vowels can be arranged among themselves in $3! = 6$ ways.
    </div>
    <div class="step">
      <strong>Total ways:</strong>
      $$6! \\times 3! = 720 \\times 6 = 4320$$
    </div>
  </div>
</div>

<!-- Ex 4 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 4: Vowels Never Together (Gap Method)</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    In how many ways can the letters of the word <strong>DAUGHTER</strong> be arranged so that no two vowels are ever together?
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Arrange the 5 consonants first:</strong>
      $$\\_ D \\_ G \\_ H \\_ T \\_ R \\_$$
      Number of ways to arrange 5 consonants $= 5! = 120$.
    </div>
    <div class="step">
      <strong>Step 2: Count available gaps for vowels:</strong>
      5 consonants create $5 + 1 = 6$ gaps (marked with $\\_$).
    </div>
    <div class="step">
      <strong>Step 3: Place 3 vowels into the 6 gaps:</strong>
      Number of ways $= ^6P_3 = 6 \\times 5 \\times 4 = 120$.
    </div>
    <div class="step">
      <strong>Total ways:</strong>
      $$5! \\times ^6P_3 = 120 \\times 120 = 14,400$$
    </div>
  </div>
</div>

<!-- Ex 5 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 5: Committee Selection with "At Least" Condition</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    A committee of 7 has to be formed from 9 boys and 4 girls. In how many ways can this be done when the committee consists of at least 3 girls?
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Break into mutually exclusive cases:</strong>
      Since there are 4 girls available, "at least 3 girls" means either 3 girls or 4 girls:
      <ul>
        <li><strong>Case 1 (3 girls and 4 boys):</strong> $^4C_3 \\times ^9C_4 = 4 \\times 126 = 504$.</li>
        <li><strong>Case 2 (4 girls and 3 boys):</strong> $^4C_4 \\times ^9C_3 = 1 \\times 84 = 84$.</li>
      </ul>
    </div>
    <div class="step">
      <strong>Total combinations (Addition Principle):</strong>
      $$504 + 84 = 588$$
    </div>
  </div>
</div>

<!-- SECTION 9 -->
<h2 class="section-title" id="s9">[[BOOK]] 9. NCERT Key Exercise Questions Solved</h2>

<div class="ncert-box">
  <h4>NCERT Exercise 6.3 — Question 8</h4>
  <div class="ncert-q">
    <strong>Q:</strong> How many 4-digit numbers can be formed by using the digits 1 to 9 if repetition of digits is not allowed?
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>There are 9 available digits $\\{1, 2, ..., 9\\}$ and we must choose and arrange 4 distinct digits.</p>
        <p>$$^9P_4 = 9 \\times 8 \\times 7 \\times 6 = 3024$$</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 6.4 — Question 2</h4>
  <div class="ncert-q">
    <strong>Q:</strong> If $^{2n}C_3 : ^nC_3 = 12 : 1$, find $n$.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>$$\\frac{^{2n}C_3}{^nC_3} = \\frac{\\frac{2n(2n-1)(2n-2)}{3!}}{\\frac{n(n-1)(n-2)}{3!}} = \\frac{2n(2n-1) \\cdot 2(n-1)}{n(n-1)(n-2)} = \\frac{4(2n-1)}{n - 2} = 12$$</p>
        <p>$$4(2n - 1) = 12(n - 2) \\implies 8n - 4 = 12n - 24 \\implies 4n = 20 \\implies n = 5$$</p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Miscellaneous Exercise — Question 7</h4>
  <div class="ncert-q">
    <strong>Q:</strong> In an examination, a question paper consists of 12 questions divided into two parts, Part I and Part II, containing 5 and 7 questions respectively. A student is required to attempt 8 questions in all, selecting at least 3 from each part. In how many ways can a student select the questions?
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Possible distributions of 8 questions between Part I (5 questions) and Part II (7 questions) with $\\ge 3$ from each:</p>
        <ul>
          <li><strong>Case 1: 3 from Part I, 5 from Part II:</strong> $^5C_3 \\times ^7C_5 = 10 \\times 21 = 210$.</li>
          <li><strong>Case 2: 4 from Part I, 4 from Part II:</strong> $^5C_4 \\times ^7C_4 = 5 \\times 35 = 175$.</li>
          <li><strong>Case 3: 5 from Part I, 3 from Part II:</strong> $^5C_5 \\times ^7C_3 = 1 \\times 35 = 35$.</li>
        </ul>
        <p>Total ways $= 210 + 175 + 35 = 420$.</p>
      </div>
    </details>
  </div>
</div>

<!-- SECTION 10 -->
<h2 class="section-title" id="s10">[[ALERT]] 10. Common Exam Traps & Quick Self-Check Quiz</h2>

<div class="trap-card">
  <h4>[[ALERT]] Trap 1: Confusing Permutation with Combination</h4>
  <p>Ask yourself: <em>Does changing the order create a brand new outcome?</em> If yes $\\to$ Permutation ($^nP_r$). If no $\\to$ Combination ($^nC_r$). Picking a delegation is $^nC_r$; appointing President, Secretary is $^nP_r$.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 2: Forgetting Internal Arrangements in Tie-Together</h4>
  <p>Students tie vowels $[A, E, I]$ together and count $6!$, but completely forget to multiply by $3!$ for their internal arrangements! Always multiply by the permutations within each tied block.</p>
</div>

<div class="quiz-card">
  <p><strong>Q1:</strong> If $^nC_{10} = ^nC_{12}$, what is the value of $n$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Using $^nC_a = ^nC_b \\implies a + b = n$, we get $n = 10 + 12 = 22$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q2:</strong> How many diagonals does a regular decagon (10-sided polygon) have?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$\\text{Diagonals} = ^{10}C_2 - 10 = \\frac{10 \\times 9}{2} - 10 = 45 - 10 = 35$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q3:</strong> What is $^nC_r + ^nC_{r-1}$ equal to?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$^{n+1}C_r$ (Pascal's rule).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q4:</strong> In how many ways can 5 people sit on 5 chairs?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$5! = 120$ ways.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q5:</strong> How many 3-letter words can be formed from letters of the word <strong>BIRD</strong> without repetition?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Word has 4 distinct letters. $^4P_3 = 4 \\times 3 \\times 2 = 24$.</div></details>
</div>
"""

out = wrap("Permutations and Combinations", 6, "Chapter_5_Linear_Inequalities.html", "Chapter_7_Binomial_Theorem.html", ch6)
with open(os.path.join(BASE_DIR, "Chapter_6_Permutations_and_Combinations.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Chapter 6 written successfully!")
print("File size:", os.path.getsize(os.path.join(BASE_DIR, "Chapter_6_Permutations_and_Combinations.html")), "bytes")
