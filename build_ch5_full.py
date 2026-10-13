import os
from builder_common import BASE_DIR, wrap, si

ch5 = """
<div class="header-card">
  <span class="badge">NCERT Chapter 5</span>
  <h1>Linear Inequalities</h1>
  <p>Learn how to solve inequalities algebraically, represent intervals on the number line, graph half-planes, and solve classic word problems.</p>
  <div class="stats-row">
    <span>[[CLOCK]] ~35 min read</span>
    <span>[[TARGET]] 4–6 marks in exam</span>
    <span>[[BOOK]] <a href="../kemh105.pdf">kemh105.pdf</a></span>
  </div>
</div>

<div class="toc">
  <h3>[[INFO]] What you will learn in this chapter</h3>
  <ol>
    <li><a href="#s1">What is an Inequality? Strict vs Slack</a></li>
    <li><a href="#s2">The 3 Golden Rules of Inequality Transformations</a></li>
    <li><a href="#s3">Interval Notation & Number Line Representations</a></li>
    <li><a href="#s4">Solving Systems of Linear Inequalities in One Variable</a></li>
    <li><a href="#s5">Graphical Solution in Two Variables (Half-Planes)</a></li>
    <li><a href="#s6">Word Problems: Mixture & Average Problems</a></li>
    <li><a href="#s7">Worked Examples — Easy to Hard</a></li>
    <li><a href="#s8">NCERT Key Exercise Questions Solved</a></li>
    <li><a href="#s9">Common Exam Traps & Pitfalls</a></li>
    <li><a href="#s10">Quick Self-Check Quiz</a></li>
  </ol>
</div>

<!-- SECTION 1 -->
<h2 class="section-title" id="s1">[[ZAP]] 1. What is an Inequality? Strict vs Slack</h2>

<div class="concept-box">
  <h4>Equations vs Inequalities</h4>
  <p>An equation says two quantities are <strong>identical</strong> ($x = 5$). An inequality says one quantity is <strong>greater than, less than, or bounded by</strong> another ($x < 5$ or $x \\ge 5$).</p>
</div>

<div class="types-grid">
  <div class="type-card">
    <h5>Strict Inequalities ($<, >$)</h5>
    <p>The boundary value itself is <strong>strictly excluded</strong>.</p>
    <p>Examples: $ax + b < 0$, $ax + b > 0$.</p>
    <p>Number line representation uses a <strong>hollow circle ($\circ$)</strong>. 2D graphs use a <strong>dashed boundary line</strong>.</p>
  </div>
  <div class="type-card">
    <h5>Slack / Non-Strict Inequalities ($\\le, \\ge$)</h5>
    <p>The boundary value is <strong>included</strong> ("less than or equal to").</p>
    <p>Examples: $ax + b \\le 0$, $ax + b \\ge 0$.</p>
    <p>Number line representation uses a <strong>solid dot ($\bullet$)</strong>. 2D graphs use a <strong>solid boundary line</strong>.</p>
  </div>
</div>

<!-- SECTION 2 -->
<h2 class="section-title" id="s2">[[ZAP]] 2. The 3 Golden Rules of Inequality Transformations</h2>

<div class="concept-box">
  <h4>Rule 1: Addition & Subtraction</h4>
  <p>Equal numbers may be added to (or subtracted from) both sides of an inequality <strong>without changing the direction</strong> of the inequality sign:</p>
  <p>$$a < b \\implies a + c < b + c \\quad \\text{and} \\quad a - c < b - c$$</p>
</div>

<div class="concept-box">
  <h4>Rule 2: Multiplication/Division by a Positive Number</h4>
  <p>Both sides of an inequality can be multiplied (or divided) by the same <strong>positive</strong> number ($c > 0$) <strong>without changing the direction</strong> of the inequality sign:</p>
  <p>$$a < b \\implies ac < bc \\quad \\text{and} \\quad \\frac{a}{c} < \\frac{b}{c} \\quad (\\text{when } c > 0)$$</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Rule 3 (THE MOST IMPORTANT RULE): Multiplying/Dividing by a Negative Number</h4>
  <p>When both sides of an inequality are multiplied (or divided) by the same <strong>negative</strong> number ($c < 0$), the inequality sign <strong>MUST BE REVERSED</strong>!</p>
  <p>$$a < b \\implies ac > bc \\quad \\text{and} \\quad \\frac{a}{c} > \\frac{b}{c} \\quad (\\text{when } c < 0)$$</p>
  <p><em>Intuition:</em> We know $2 < 5$. If we multiply both sides by $-1$, $-2$ is greater than $-5$ on the number line! Hence $-2 > -5$.</p>
</div>

<!-- SECTION 3 -->
<h2 class="section-title" id="s3">[[ZAP]] 3. Interval Notation & Number Line</h2>

<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Inequality</th>
        <th>Interval Notation</th>
        <th>Type</th>
        <th>Graphic Meaning</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>$a < x < b$</td>
        <td>$(a, b)$</td>
        <td>Open Interval</td>
        <td>All real numbers between $a$ and $b$; endpoints excluded.</td>
      </tr>
      <tr>
        <td>$a \\le x \\le b$</td>
        <td>$[a, b]$</td>
        <td>Closed Interval</td>
        <td>All real numbers between $a$ and $b$; both endpoints included.</td>
      </tr>
      <tr>
        <td>$a \\le x < b$</td>
        <td>$[a, b)$</td>
        <td>Semi-closed / Semi-open</td>
        <td>$a$ is included (square bracket), $b$ is excluded (round bracket).</td>
      </tr>
      <tr>
        <td>$x > a$</td>
        <td>$(a, \\infty)$</td>
        <td>Unbounded Above</td>
        <td>Ray extending infinitely to the right from $a$. $\\infty$ always has round bracket!</td>
      </tr>
      <tr>
        <td>$x \\le b$</td>
        <td>$(-\\infty, b]$</td>
        <td>Unbounded Below</td>
        <td>Ray extending infinitely to the left up to $b$ inclusive.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="concept-box">
  <h4>Dependence on Domain: $\\mathbb{N}$ vs $\\mathbb{Z}$ vs $\\mathbb{R}$</h4>
  <p>Consider the inequality: $24x < 100 \\implies x < \\frac{100}{24} = \\frac{25}{6} = 4.166...$</p>
  <ul>
    <li><strong>If $x \\in \\mathbb{N}$ (Natural numbers):</strong> Solution set is $\\{1, 2, 3, 4\\}$ (discrete elements in curly braces).</li>
    <li><strong>If $x \\in \\mathbb{Z}$ (Integers):</strong> Solution set is $\\{..., -2, -1, 0, 1, 2, 3, 4\\}$.</li>
    <li><strong>If $x \\in \\mathbb{R}$ (Real numbers):</strong> Solution set is an infinite continuum: $(-\\infty, 25/6)$ in interval notation!</li>
  </ul>
</div>

<!-- SECTION 4 -->
<h2 class="section-title" id="s4">[[ZAP]] 4. Solving Systems of Linear Inequalities in One Variable</h2>

<div class="concept-box">
  <h4>Step-by-Step Method</h4>
  <ol>
    <li>Solve each inequality independently for $x$.</li>
    <li>Plot the solution of each inequality on the same real number line.</li>
    <li>The overall solution is the <strong>intersection (overlapping region)</strong> of all individual solutions.</li>
    <li>Write the common overlapping region in interval notation.</li>
  </ol>
</div>

<!-- SECTION 5 -->
<h2 class="section-title" id="s5">[[ZAP]] 5. Graphical Solution in Two Variables (Half-Planes)</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>Step 1: Draw Boundary Line</h5>
    <p>Replace inequality sign with equality: $ax + by = c$. Plot by finding $x$-intercept (set $y=0$) and $y$-intercept (set $x=0$).</p>
    <p>Draw <strong>solid line</strong> for $\\le, \\ge$; draw <strong>dashed line</strong> for $<, >$.</p>
  </div>
  <div class="type-card">
    <h5>Step 2: Test Point Method</h5>
    <p>Pick an easy point not on the line, usually the origin $(0, 0)$. Substitute $(0, 0)$ into the inequality.</p>
    <p>If true: shade the half-plane <strong>containing $(0,0)$</strong>.<br>If false: shade the opposite half-plane.</p>
  </div>
</div>

<!-- SECTION 6 -->
<h2 class="section-title" id="s6">[[ZAP]] 6. Solving Classic Word Problems</h2>

<div class="concept-box">
  <h4>1. Examination Average Problem</h4>
  <p>If a student's marks in two tests are $m_1, m_2$, and they need an average of at least $A$ across 3 tests:</p>
  <p>$$\\frac{m_1 + m_2 + x}{3} \\ge A \\implies x \\ge 3A - (m_1 + m_2)$$</p>
  <h4>2. Mixture Problems</h4>
  <p>When mixing $x$ liters of $c_1\\%$ solution with $y$ liters of $c_2\\%$ solution, the total amount of solute is:</p>
  <p>$$\\frac{c_1}{100}x + \\frac{c_2}{100}y$$</p>
  <p>Divide by total volume $(x + y)$ to find the resulting concentration.</p>
</div>

<!-- SECTION 7 -->
<h2 class="section-title" id="s7">[[TARGET]] 7. Worked Examples — Easy to Hard</h2>

<!-- Ex 1 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 1: Single Inequality with Negative Coefficient</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">
    Solve $-12x > 30$, when: (i) $x$ is a natural number, (ii) $x$ is an integer, (iii) $x$ is a real number.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Divide by $-12$ and REVERSE sign:</strong>
      $$x < \\frac{30}{-12} = -\\frac{5}{2} = -2.5$$
    </div>
    <div class="step">
      <strong>(i) $x \\in \\mathbb{N}$:</strong> Natural numbers are $\\{1, 2, 3, ...\\}$. None are $< -2.5$. Solution set is $\\phi$ (empty set).
    </div>
    <div class="step">
      <strong>(ii) $x \\in \\mathbb{Z}$:</strong> Integers $< -2.5$ are $\\{..., -5, -4, -3\\}$.
    </div>
    <div class="step">
      <strong>(iii) $x \\in \\mathbb{R}$:</strong> Interval is $(-\\infty, -5/2)$.
    </div>
  </div>
</div>

<!-- Ex 2 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 2: Fractions on Both Sides</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Solve the inequality for real $x$:
    $$\\frac{3(x - 2)}{5} \\le \\frac{5(2 - x)}{3}$$
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Multiply both sides by LCM $= 15$ (positive, so sign does not change):</strong>
      $$3 \\times 3(x - 2) \\le 5 \\times 5(2 - x)$$
      $$9(x - 2) \\le 25(2 - x)$$
    </div>
    <div class="step">
      <strong>Step 2: Expand and collect terms:</strong>
      $$9x - 18 \\le 50 - 25x$$
      $$9x + 25x \\le 50 + 18$$
      $$34x \\le 68 \\implies x \\le 2$$
    </div>
    <p><strong>Solution:</strong> $x \\in (-\\infty, 2]$.</p>
  </div>
</div>

<!-- Ex 3 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 3: System of Inequalities in One Variable</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Solve the system of inequalities and represent the solution on a number line:
    $$5x + 1 > -24 \\quad \\text{and} \\quad 5x - 1 < 24$$
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Solve first inequality:</strong>
      $$5x > -24 - 1 = -25 \\implies x > -5$$
    </div>
    <div class="step">
      <strong>Step 2: Solve second inequality:</strong>
      $$5x < 24 + 1 = 25 \\implies x < 5$$
    </div>
    <div class="step">
      <strong>Step 3: Intersection:</strong>
      $$x > -5 \\quad \\text{and} \\quad x < 5 \\implies -5 < x < 5$$
      $$\\mathbf{\\text{Solution Interval: } (-5, 5)}$$
    </div>
  </div>
</div>

<!-- Ex 4 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 4: Double / Compound Inequality</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">
    Solve: $-5 \\le \\frac{5 - 3x}{2} \\le 8$ for real $x$.
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Multiply all sides by $2$:</strong>
      $$-10 \\le 5 - 3x \\le 16$$
    </div>
    <div class="step">
      <strong>Step 2: Subtract $5$ from all parts:</strong>
      $$-15 \\le -3x \\le 11$$
    </div>
    <div class="step">
      <strong>Step 3: Divide by $-3$ and REVERSE all inequality signs:</strong>
      $$\\frac{-15}{-3} \\ge x \\ge \\frac{11}{-3} \\implies 5 \\ge x \\ge -\\frac{11}{3}$$
      Rewriting in standard increasing order:
      $$-\\frac{11}{3} \\le x \\le 5$$
      $$\\mathbf{\\text{Solution: } \\left[-\\frac{11}{3}, 5\\right]}$$
    </div>
  </div>
</div>

<!-- Ex 5 -->
<div class="example-box">
  <div class="example-header">
    <strong>Example 5: Word Problem — Acid Mixture</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">
    A manufacturer has 600 liters of a $12\\%$ solution of acid. How many liters of a $30\\%$ acid solution must be added to it so that acid content in the resulting mixture will be more than $15\\%$ but less than $18\\%$?
  </div>
  <div class="example-sol">
    <div class="step">
      <strong>Step 1: Define variables:</strong>
      Let $x$ liters of $30\\%$ acid solution be added.
      Total volume of mixture $= 600 + x$ liters.
      Total acid content $= 12\\% \\text{ of } 600 + 30\\% \\text{ of } x = \\frac{12}{100}(600) + \\frac{30}{100}(x) = 72 + 0.3x$.
    </div>
    <div class="step">
      <strong>Step 2: Set up inequalities:</strong>
      $$15\\% \\text{ of } (600 + x) < 72 + 0.3x < 18\\% \\text{ of } (600 + x)$$
      $$0.15(600 + x) < 72 + 0.3x < 0.18(600 + x)$$
    </div>
    <div class="step">
      <strong>Step 3: Solve first inequality:</strong>
      $$90 + 0.15x < 72 + 0.3x \\implies 90 - 72 < 0.3x - 0.15x \\implies 18 < 0.15x \\implies x > 120$$
    </div>
    <div class="step">
      <strong>Step 4: Solve second inequality:</strong>
      $$72 + 0.3x < 108 + 0.18x \\implies 0.12x < 36 \\implies x < 300$$
    </div>
    <p><strong>Conclusion:</strong> Between $120$ liters and $300$ liters of $30\\%$ acid solution must be added.</p>
  </div>
</div>

<!-- SECTION 8 -->
<h2 class="section-title" id="s8">[[BOOK]] 8. NCERT Key Exercise Questions Solved</h2>

<div class="ncert-box">
  <h4>NCERT Exercise 5.1 — Question 21</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Ravi obtained 70 and 75 marks in first two unit tests. Find the minimum marks he should get in the third test to have an average of at least 60 marks.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Let $x$ be the marks in the third test.</p>
        <p>$$\\frac{70 + 75 + x}{3} \\ge 60$$</p>
        <p>$$145 + x \\ge 180 \\implies x \\ge 180 - 145 = 35$$</p>
        <p><strong>Minimum marks required = 35.</strong></p>
      </div>
    </details>
  </div>
</div>

<div class="ncert-box">
  <h4>NCERT Exercise 5.1 — Question 23</h4>
  <div class="ncert-q">
    <strong>Q:</strong> Find all pairs of consecutive odd positive integers, both of which are smaller than 10, such that their sum is more than 11.
    <details>
      <summary>View Full Solution</summary>
      <div class="ncert-ans">
        <p>Let the smaller odd positive integer be $x$. The next consecutive odd integer is $x + 2$.</p>
        <p>Condition 1: Both smaller than 10: $x + 2 < 10 \\implies x < 8$.</p>
        <p>Condition 2: Sum more than 11: $x + (x + 2) > 11 \\implies 2x + 2 > 11 \\implies 2x > 9 \\implies x > 4.5$.</p>
        <p>Since $x$ is an odd positive integer and $4.5 < x < 8$, the possible values for $x$ are $5$ and $7$.</p>
        <p>Pairs $(x, x+2)$ are: <strong>$(5, 7)$ and $(7, 9)$</strong>.</p>
      </div>
    </details>
  </div>
</div>

<!-- SECTION 9 -->
<h2 class="section-title" id="s9">[[ALERT]] 9. Common Exam Traps & Pitfalls</h2>

<div class="trap-card">
  <h4>[[ALERT]] Trap 1: Cross-Multiplying Variables</h4>
  <p>In an inequality like $\\frac{1}{x} < 1$, NEVER cross-multiply $x$ to get $1 < x$! Because if $x$ is negative, multiplying by $x$ would flip the sign. Always bring everything to one side: $\\frac{1}{x} - 1 < 0 \\implies \\frac{1 - x}{x} < 0$, and use sign charts.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 2: Forgetting to Reverse Sign on Negative Division</h4>
  <p>The single most common mistake in board exams: Writing $-2x \\le 8 \\implies x \\le -4$. IT IS WRONG! Dividing by $-2$ reverses the sign to $x \\ge -4$.</p>
</div>

<div class="trap-card">
  <h4>[[ALERT]] Trap 3: Confusing Natural Numbers with Real Numbers</h4>
  <p>If the question says "where $x$ is an integer", do NOT write $(-\\infty, 3)$ as your final answer. Write $\\{..., -1, 0, 1, 2\\}$. Bracket notation like $(a, b)$ is strictly reserved for real numbers.</p>
</div>

<!-- SECTION 10 -->
<h2 class="section-title" id="s10">[[QUIZ]] 10. Quick Self-Check Quiz</h2>

<div class="quiz-card">
  <p><strong>Q1:</strong> If $-3x + 17 < -13$, what is the range of real $x$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$-3x < -30 \\implies x > 10$. In interval notation: $(10, \\infty)$.</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q2:</strong> How many positive integers satisfy $4x + 3 < 6x + 7$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$4x - 6x < 7 - 3 \\implies -2x < 4 \\implies x > -2$. Since all positive integers are $> -2$, there are infinitely many solutions ($x \\in \\{1, 2, 3, ...\\}$).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q3:</strong> What is the intersection of $[-3, 7)$ and $(2, 10]$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$(2, 7)$. (2 is excluded because it's excluded in $(2, 10]$, 7 is excluded because it's excluded in $[-3, 7)$).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q4:</strong> In a graph of $2x - 3y > 6$, is the boundary line solid or dashed?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Dashed, because the inequality is strict ($>$).</div></details>
</div>

<div class="quiz-card">
  <p><strong>Q5:</strong> Does the point $(0, 0)$ satisfy $3x - 5y \\le 15$?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">Yes, $3(0) - 5(0) = 0 \\le 15$ is true, so $(0, 0)$ lies in the solution half-plane.</div></details>
</div>
"""

out = wrap("Linear Inequalities", 5, "Chapter_4_Complex_Numbers.html", "Chapter_6_Permutations_and_Combinations.html", ch5)
with open(os.path.join(BASE_DIR, "Chapter_5_Linear_Inequalities.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Chapter 5 written successfully!")
print("File size:", os.path.getsize(os.path.join(BASE_DIR, "Chapter_5_Linear_Inequalities.html")), "bytes")
