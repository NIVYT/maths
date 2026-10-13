import os

BASE_DIR = r"c:\Users\Nived.LAPTOP-AOD9V08S\Downloads\kemh1dd\Revision_Notes"

SVGS = {
    "COMPASS": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>',
    "EYE": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>',
    "PRINT": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>',
    "CLOCK": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "TARGET": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    "BOOK": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
    "ZAP": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "ALERT": '<svg class="icon-svg icon-alert" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "QUIZ": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>',
    "ARROW_LEFT": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>',
    "ARROW_RIGHT": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "HOME": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',
    "INFO": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
}

def si(text):
    for k, v in SVGS.items():
        text = text.replace(f"[[{k}]]", v)
    return text

def wrap(title, num, prev, nxt, body):
    pb = f'<a href="{prev}" class="btn">[[ARROW_LEFT]] Prev Chapter</a>' if prev else '<span></span>'
    nb = f'<a href="{nxt}" class="btn btn-primary">Next Chapter [[ARROW_RIGHT]]</a>' if nxt else '<span></span>'
    return si(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter {num}: {title} — Class 11 Maths</title>
  <link rel="stylesheet" href="common_style.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}]}});"></script>
  <style>
    .concept-box {{ background:#1e40af; border-radius:10px; padding:1.25rem 1.5rem; margin-bottom:1.25rem; color:#bfdbfe; }}
    .concept-box h4 {{ color:#ffffff; margin-bottom:0.5rem; font-size:1rem; }}
    .concept-box p, .concept-box ul {{ color:#bfdbfe; font-size:0.95rem; margin-bottom:0.4rem; }}
    .concept-box ul {{ padding-left:1.25rem; }}
    .concept-box strong {{ color:#ffffff; }}
    .example-box {{ background:#ffffff; border-radius:10px; margin-bottom:1.25rem; overflow:hidden; }}
    .example-header {{ background:#7c3aed; padding:0.75rem 1.25rem; display:flex; justify-content:space-between; align-items:center; }}
    .example-header strong {{ color:#ffffff; font-size:0.95rem; }}
    .example-level {{ font-size:0.75rem; font-weight:700; padding:0.15rem 0.5rem; border-radius:4px; color:#ffffff; }}
    .level-easy {{ background:#059669; }}
    .level-med {{ background:#d97706; }}
    .level-hard {{ background:#dc2626; }}
    .example-q {{ background:#f5f3ff; padding:1rem 1.25rem; color:#3b0764; font-size:0.95rem; }}
    .example-sol {{ background:#ede9fe; padding:1rem 1.25rem; }}
    .example-sol p {{ color:#4c1d95; font-size:0.92rem; margin-bottom:0.5rem; }}
    .step {{ padding:0.4rem 0 0.4rem 0.75rem; border-left:3px solid #7c3aed; margin-bottom:0.5rem; color:#3b0764; font-size:0.92rem; }}
    .ncert-box {{ background:#0f172a; border-radius:10px; padding:1.25rem 1.5rem; margin-bottom:1.25rem; }}
    .ncert-box h4 {{ color:#7dd3fc; margin-bottom:0.75rem; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.04em; }}
    .ncert-q {{ background:#1e293b; border-radius:6px; padding:0.85rem 1rem; margin-bottom:0.75rem; color:#e2e8f0; font-size:0.92rem; }}
    .ncert-ans {{ background:#0c4a6e; border-radius:6px; padding:0.6rem 1rem; margin-top:0.4rem; color:#bae6fd; font-size:0.9rem; }}
    .definition {{ background:#059669; border-radius:8px; padding:1rem 1.25rem; margin-bottom:1rem; }}
    .definition strong {{ color:#ffffff; display:block; margin-bottom:0.25rem; }}
    .definition p {{ color:#d1fae5; font-size:0.95rem; }}
    .types-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:1.25rem; }}
    .type-card {{ background:#0284c7; border-radius:8px; padding:0.85rem 1rem; }}
    .type-card h5 {{ color:#ffffff; font-size:0.9rem; margin-bottom:0.25rem; }}
    .type-card p {{ color:#bae6fd; font-size:0.83rem; }}
    .toc {{ background:#1e293b; border-radius:10px; padding:1.25rem; margin-bottom:2rem; }}
    .toc h3 {{ color:#7dd3fc; font-size:1rem; margin-bottom:0.75rem; }}
    .toc ol {{ padding-left:1.25rem; color:#94a3b8; font-size:0.9rem; line-height:2; }}
    .toc a {{ color:#7dd3fc; text-decoration:none; }}
    .toc a:hover {{ color:#ffffff; }}
  </style>
</head>
<body>
<nav class="top-navbar">
  <a href="index.html" class="nav-brand">[[COMPASS]] Class 11 Maths</a>
  <div class="nav-actions">
    <button class="btn" onclick="toggleAllSolutions()">[[EYE]] Toggle Solutions</button>
    <button class="btn btn-primary" onclick="window.print()">[[PRINT]] Print</button>
  </div>
</nav>
<div class="container">
{body}
<div class="bottom-nav">
  {pb}
  <a href="index.html" class="btn">[[HOME]] Hub</a>
  {nb}
</div>
</div>
<script>
  let open=false;
  function toggleAllSolutions(){{open=!open;document.querySelectorAll('details').forEach(d=>d.open=open);}}
</script>
</body></html>""")

# ═══════════════════════════════════════════════════════════════
# CHAPTER 1: SETS  — Full first-timer content
# ═══════════════════════════════════════════════════════════════
ch1 = """
<div class="header-card">
  <span class="badge">NCERT Chapter 1</span>
  <h1>Sets</h1>
  <p>A complete ground-up guide — from what a set even is, to solving 3-variable survey problems in exams.</p>
  <div class="stats-row">
    <span>[[CLOCK]] ~45 min read</span>
    <span>[[TARGET]] 4–6 marks in exam</span>
    <span>[[BOOK]] <a href="../kemh101.pdf">kemh101.pdf</a></span>
  </div>
</div>

<div class="toc">
  <h3>[[INFO]] What you will learn in this chapter</h3>
  <ol>
    <li><a href="#s1">What is a Set? (concept)</a></li>
    <li><a href="#s2">How to write sets — Roster & Set-Builder forms</a></li>
    <li><a href="#s3">8 Types of Sets you must know</a></li>
    <li><a href="#s4">Subsets, Proper Subsets & Power Set</a></li>
    <li><a href="#s5">Universal Set & Venn Diagrams</a></li>
    <li><a href="#s6">Set Operations — Union, Intersection, Difference, Complement</a></li>
    <li><a href="#s7">Laws of Sets (De Morgan's, etc.)</a></li>
    <li><a href="#s8">Cardinality Formulas (critical for word problems)</a></li>
    <li><a href="#s9">15 Worked Examples — Easy to Hard</a></li>
    <li><a href="#s10">NCERT Exercise Questions Solved</a></li>
  </ol>
</div>

<!-- SECTION 1 -->
<h2 class="section-title" id="s1">[[ZAP]] 1. What is a Set?</h2>

<div class="concept-box">
  <h4>The Core Idea</h4>
  <p>A <strong>set</strong> is simply a well-defined collection of distinct objects. "Well-defined" means there is no ambiguity — you can always tell whether something belongs to the collection or not.</p>
</div>

<div class="concept-box">
  <h4>Real-life examples that ARE sets</h4>
  <ul>
    <li>The collection of all vowels in the English alphabet: {a, e, i, o, u} — well-defined, no ambiguity.</li>
    <li>The collection of all prime numbers less than 10: {2, 3, 5, 7}.</li>
    <li>The collection of months of the year starting with 'J': {January, June, July}.</li>
    <li>The collection of students in your class whose roll numbers are below 5.</li>
  </ul>
</div>

<div class="concept-box">
  <h4>These are NOT sets — because they are NOT well-defined</h4>
  <ul>
    <li>"The collection of good students" — what does "good" mean? Different people decide differently.</li>
    <li>"The collection of tall people" — "tall" is subjective, not precise.</li>
    <li>"The collection of beautiful flowers" — beauty is subjective.</li>
  </ul>
  <p>The key test: Can any two people independently, without discussion, agree on whether an object belongs? If yes, it's a set.</p>
</div>

<div class="concept-box">
  <h4>Notation basics</h4>
  <ul>
    <li>Sets are denoted by <strong>capital letters</strong>: A, B, C, X, Y, Z...</li>
    <li>Elements (objects in the set) are denoted by <strong>small letters</strong>: a, b, x, y...</li>
    <li>$x \in A$ means "$x$ belongs to set $A$" (x is an element of A).</li>
    <li>$x \notin A$ means "$x$ does not belong to set $A$".</li>
  </ul>
  <p><strong>Example:</strong> If $A = \{1, 2, 3, 4, 5\}$, then $3 \in A$ but $7 \notin A$.</p>
</div>

<!-- SECTION 2 -->
<h2 class="section-title" id="s2">[[ZAP]] 2. How to Write Sets</h2>

<div class="concept-box">
  <h4>Method 1: Roster (Tabular) Form</h4>
  <p>List all elements inside curly braces {}, separated by commas. Each element appears only once — repetitions are ignored. Order doesn't matter.</p>
  <ul>
    <li>$A = \{1, 2, 3, 4, 5\}$ — set of natural numbers less than 6.</li>
    <li>$B = \{a, e, i, o, u\}$ — set of vowels.</li>
    <li>$C = \{2, 4, 6, 8, ...\}$ — even natural numbers (dots mean the pattern continues infinitely).</li>
    <li>The word SCHOOL in roster form: $\{S, C, H, O, L\}$ — repeated letters written only once.</li>
  </ul>
</div>

<div class="concept-box">
  <h4>Method 2: Set-Builder (Rule/Property) Form</h4>
  <p>Write the rule that an element must satisfy. Format: $\{x : x \text{ satisfies some property}\}$ — read as "the set of all x such that x satisfies..."</p>
  <ul>
    <li>$A = \{x : x \text{ is a natural number and } x < 6\} = \{1, 2, 3, 4, 5\}$</li>
    <li>$B = \{x : x = 2n, n \in \mathbb{N}\} = \{2, 4, 6, 8, ...\}$ — even natural numbers.</li>
    <li>$C = \{x : x \in \mathbb{R} \text{ and } x^2 = 4\} = \{-2, 2\}$</li>
    <li>$D = \{x : x \in \mathbb{N}, 1 \le x \le 5\} = \{1, 2, 3, 4, 5\}$</li>
  </ul>
  <p><strong>Tip:</strong> The colon ":" or "|" means "such that". Both are acceptable.</p>
</div>

<div class="concept-box">
  <h4>Important Number Sets (Memorise these symbols)</h4>
  <ul>
    <li>$\mathbb{N}$ = Natural numbers = $\{1, 2, 3, 4, ...\}$</li>
    <li>$\mathbb{Z}$ = Integers = $\{..., -3, -2, -1, 0, 1, 2, 3, ...\}$</li>
    <li>$\mathbb{Q}$ = Rational numbers = numbers of the form $p/q$ where $p, q \in \mathbb{Z}, q \ne 0$</li>
    <li>$\mathbb{R}$ = Real numbers = all numbers on the number line</li>
    <li>Relation: $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$</li>
  </ul>
</div>

<!-- SECTION 3 -->
<h2 class="section-title" id="s3">[[ZAP]] 3. Types of Sets</h2>

<div class="types-grid">
  <div class="type-card">
    <h5>Empty Set (Null Set)</h5>
    <p>A set with NO elements. Written as $\phi$ or $\{\}$. Example: Set of even prime numbers greater than 10.</p>
  </div>
  <div class="type-card">
    <h5>Singleton Set</h5>
    <p>A set with exactly ONE element. Example: $\{0\}$, $\{5\}$, $\{\phi\}$ (set containing the empty set).</p>
  </div>
  <div class="type-card">
    <h5>Finite Set</h5>
    <p>A set with a countable (limited) number of elements. Example: Set of days in a week = $\{Mon, Tue, ..., Sun\}$, $n = 7$.</p>
  </div>
  <div class="type-card">
    <h5>Infinite Set</h5>
    <p>A set with unlimited elements, cannot be fully listed. Example: $\mathbb{N}, \mathbb{Z}, \mathbb{R}$, set of all stars in the universe.</p>
  </div>
  <div class="type-card">
    <h5>Equal Sets</h5>
    <p>Two sets A and B are equal ($A = B$) if they have exactly the same elements. Order doesn't matter. $\{1,2,3\} = \{3,1,2\}$.</p>
  </div>
  <div class="type-card">
    <h5>Equivalent Sets</h5>
    <p>Sets with the same NUMBER of elements (same cardinality), but not necessarily the same elements. $\{1,2,3\}$ and $\{a,b,c\}$ are equivalent.</p>
  </div>
  <div class="type-card">
    <h5>Disjoint Sets</h5>
    <p>Two sets with NO common elements. $A \cap B = \phi$. Example: $\{1,3,5\}$ and $\{2,4,6\}$.</p>
  </div>
  <div class="type-card">
    <h5>Intervals (Subsets of $\mathbb{R}$)</h5>
    <p>$[a,b]$ = closed (both included). $(a,b)$ = open (both excluded). $[a,b)$ and $(a,b]$ = half-open.</p>
  </div>
</div>

<div class="concept-box">
  <h4>Critical Note: Empty Set Confusion</h4>
  <ul>
    <li>$\phi$ = the empty set (has 0 elements).</li>
    <li>$\{\phi\}$ = a set containing the empty set (has 1 element — NOT empty!).</li>
    <li>$\{0\}$ = a set containing zero (has 1 element — NOT empty!).</li>
    <li>The empty set $\phi$ is a subset of every set.</li>
  </ul>
</div>

<!-- SECTION 4 -->
<h2 class="section-title" id="s4">[[ZAP]] 4. Subsets, Proper Subsets & Power Set</h2>

<div class="definition">
  <strong>Subset ($A \subseteq B$)</strong>
  <p>$A$ is a subset of $B$ if every element of $A$ is also an element of $B$. In other words, $A$ is "contained inside" $B$.<br>
  Formally: $A \subseteq B \iff \forall x, (x \in A \implies x \in B)$</p>
</div>

<div class="concept-box">
  <h4>Understanding subsets with an example</h4>
  <p>Let $B = \{1, 2, 3\}$. All subsets of $B$:</p>
  <ul>
    <li>$\phi$ (empty set — always a subset of any set)</li>
    <li>$\{1\}, \{2\}, \{3\}$ (single-element subsets)</li>
    <li>$\{1,2\}, \{1,3\}, \{2,3\}$ (two-element subsets)</li>
    <li>$\{1,2,3\}$ (the set itself — every set is a subset of itself)</li>
  </ul>
  <p>Total: <strong>8 subsets</strong>. Since $|B| = 3$, total subsets $= 2^3 = 8$. ✓</p>
</div>

<div class="definition">
  <strong>Proper Subset ($A \subset B$ or $A \subsetneq B$)</strong>
  <p>$A$ is a proper subset of $B$ if $A \subseteq B$ AND $A \ne B$. In other words, $A$ is a subset but not equal to $B$ — at least one element of $B$ is not in $A$.</p>
</div>

<div class="formula-card">
  <h4>Power Set, Subset Count Formulas</h4>
  <div class="formula-highlight">
    $$\text{If } |A| = n \text{ (n elements in set A):}$$
    $$\text{Total subsets} = 2^n$$
    $$\text{Total proper subsets} = 2^n - 1$$
    $$\text{Total non-empty proper subsets} = 2^n - 2$$
    $$\text{Power Set } P(A) = \text{set of ALL subsets of } A, \quad |P(A)| = 2^n$$
  </div>
</div>

<div class="concept-box">
  <h4>Subset vs Element — the most common mistake in exams</h4>
  <ul>
    <li>Let $A = \{1, \{2, 3\}, 4\}$</li>
    <li>$1 \in A$ ✓ (1 is an element of A)</li>
    <li>$\{1\} \subset A$ ✓ ({1} is a subset of A)</li>
    <li>$\{2, 3\} \in A$ ✓ ({2,3} is an element of A — it's listed as a single element)</li>
    <li>$\{2, 3\} \subset A$ ✗ (2 is not directly in A; {2,3} as a whole is an element)</li>
    <li>$\{\{2, 3\}\} \subset A$ ✓ (the set containing {2,3} is a subset of A)</li>
  </ul>
</div>

<!-- SECTION 5 -->
<h2 class="section-title" id="s5">[[ZAP]] 5. Universal Set & Venn Diagrams</h2>

<div class="concept-box">
  <h4>Universal Set ($U$)</h4>
  <p>The universal set is the "master set" — it contains all elements relevant to the problem at hand. Every other set in the discussion is a subset of $U$.</p>
  <ul>
    <li>If we study natural numbers: $U = \mathbb{N}$</li>
    <li>If we study students in a school: $U$ = set of all students in the school</li>
    <li>If we study triangles: $U$ = set of all triangles</li>
  </ul>
</div>

<div class="concept-box">
  <h4>Venn Diagrams</h4>
  <p>Venn diagrams use overlapping circles inside a rectangle to visualize sets:</p>
  <ul>
    <li>The rectangle represents the Universal Set $U$.</li>
    <li>Each circle represents a set (A, B, C...).</li>
    <li>Overlapping regions represent elements in multiple sets.</li>
    <li>Elements outside all circles but inside the rectangle are in $U$ only.</li>
  </ul>
  <p>Venn diagrams are extremely useful for proving set identities and solving word problems — always draw one for survey-type questions!</p>
</div>

<!-- SECTION 6 -->
<h2 class="section-title" id="s6">[[ZAP]] 6. Set Operations</h2>

<div class="definition">
  <strong>Union: $A \cup B$</strong>
  <p>All elements that are in $A$, or $B$, or both. Think of it as combining both sets (removing duplicates).<br>
  $A \cup B = \{x : x \in A \text{ or } x \in B\}$<br>
  Example: $\{1,2,3\} \cup \{3,4,5\} = \{1,2,3,4,5\}$</p>
</div>

<div class="definition">
  <strong>Intersection: $A \cap B$</strong>
  <p>Only the elements that are in BOTH $A$ AND $B$. The "overlap".<br>
  $A \cap B = \{x : x \in A \text{ and } x \in B\}$<br>
  Example: $\{1,2,3\} \cap \{3,4,5\} = \{3\}$</p>
</div>

<div class="definition">
  <strong>Difference: $A - B$ (or $A \setminus B$)</strong>
  <p>Elements that are in $A$ but NOT in $B$. "Remove from A everything that's also in B."<br>
  $A - B = \{x : x \in A \text{ and } x \notin B\}$<br>
  Example: $\{1,2,3,4\} - \{3,4,5\} = \{1,2\}$<br>
  Note: $A - B \ne B - A$ in general!</p>
</div>

<div class="definition">
  <strong>Complement: $A'$ (or $A^c$)</strong>
  <p>All elements of the Universal Set that are NOT in $A$.<br>
  $A' = U - A = \{x : x \in U \text{ and } x \notin A\}$<br>
  Example: If $U = \{1,...,10\}$ and $A = \{1,3,5,7,9\}$, then $A' = \{2,4,6,8,10\}$</p>
</div>

<div class="formula-card">
  <h4>Properties of Set Operations</h4>
  <div class="formula-highlight">
    $$\text{Commutativity: } A \cup B = B \cup A \quad \text{and} \quad A \cap B = B \cap A$$
    $$\text{Associativity: } (A \cup B) \cup C = A \cup (B \cup C)$$
    $$\text{Distributivity: } A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
    $$\text{Identity: } A \cup \phi = A \quad \text{and} \quad A \cap U = A$$
    $$\text{Idempotent: } A \cup A = A \quad \text{and} \quad A \cap A = A$$
    $$A \cup A' = U \quad \text{and} \quad A \cap A' = \phi$$
    $$(A')' = A \quad \text{(Double complement)}$$
    $$\phi' = U \quad \text{and} \quad U' = \phi$$
  </div>
</div>

<!-- SECTION 7 -->
<h2 class="section-title" id="s7">[[ZAP]] 7. De Morgan's Laws</h2>

<div class="concept-box">
  <h4>De Morgan's Laws — Two Laws, Critical for Exams</h4>
  <div style="font-size:1.1rem; text-align:center; padding:0.75rem 0;">
    <p style="color:#ffffff; font-weight:700;">Law 1: $(A \cup B)' = A' \cap B'$</p>
    <p style="color:#bfdbfe; font-size:0.9rem;">The complement of a union = intersection of the complements.</p>
    <br>
    <p style="color:#ffffff; font-weight:700;">Law 2: $(A \cap B)' = A' \cup B'$</p>
    <p style="color:#bfdbfe; font-size:0.9rem;">The complement of an intersection = union of the complements.</p>
  </div>
  <p><strong>Memory trick:</strong> When you "distribute" the complement inside, the $\cup$ flips to $\cap$ and vice versa.</p>
</div>

<!-- SECTION 8 -->
<h2 class="section-title" id="s8">[[ZAP]] 8. Cardinality Formulas</h2>

<div class="formula-card">
  <h4>Number of elements formulas — used in every survey word problem</h4>
  <div class="formula-highlight">
    $$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$
    $$n(A - B) = n(A) - n(A \cap B) = n(A \cup B) - n(B)$$
    $$n(A \cap B) = n(A) + n(B) - n(A \cup B)$$
  </div>
  <div class="formula-highlight">
    $$\textbf{For three sets:}$$
    $$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(A \cap C) + n(A \cap B \cap C)$$
  </div>
  <div class="formula-highlight">
    $$\text{Only in A} = n(A) - n(A \cap B) - n(A \cap C) + n(A \cap B \cap C)$$
    $$\text{Exactly two sets} = n(A \cap B) + n(B \cap C) + n(A \cap C) - 3 \cdot n(A \cap B \cap C)$$
    $$\text{Exactly one set} = n(A \cup B \cup C) - [\text{exactly two}] - [\text{all three}]$$
  </div>
</div>

<!-- SECTION 9 -->
<h2 class="section-title" id="s9">[[TARGET]] 9. Worked Examples — Easy to Hard</h2>

<div class="example-box">
  <div class="example-header">
    <strong>Example 1: Write in Roster Form</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">Write the set $A = \{x : x$ is a natural number and $x^2 < 25\}$ in Roster form.</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">We need natural numbers where $x^2 < 25$, i.e., $x < 5$ (since $x$ is positive).</div>
      <div class="step">Natural numbers less than 5: $x = 1, 2, 3, 4$. Check: $1^2=1, 2^2=4, 3^2=9, 4^2=16$ — all $< 25$. And $5^2 = 25$, not $< 25$.</div>
      <div class="step">$\therefore A = \{1, 2, 3, 4\}$</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 2: Write in Set-Builder Form</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">Write $B = \{3, 6, 9, 12, 15\}$ in Set-Builder form.</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">Notice the pattern: $3 = 3(1),\ 6 = 3(2),\ 9 = 3(3),\ 12 = 3(4),\ 15 = 3(5)$</div>
      <div class="step">So every element is a multiple of 3, and there are 5 elements (multiples 1 through 5).</div>
      <div class="step">$B = \{x : x = 3n,\ n \in \mathbb{N},\ 1 \le n \le 5\}$</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 3: Which of these are sets?</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">State which of the following are sets. Justify.<br>
  (i) The collection of all months of a year beginning with the letter J<br>
  (ii) The collection of ten most talented writers of India<br>
  (iii) The collection of all even integers</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step"><strong>(i) YES — it is a set.</strong> Months starting with J are: January, June, July. These can be listed without ambiguity.</div>
      <div class="step"><strong>(ii) NO — not a set.</strong> "Most talented" is subjective. Different people would choose different writers. Not well-defined.</div>
      <div class="step"><strong>(iii) YES — it is a set.</strong> Even integers are perfectly well-defined: $\{..., -4, -2, 0, 2, 4, ...\}$. There is no ambiguity about whether a number is even.</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 4: Counting Subsets</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">Let $A = \{a, b, c, d\}$. Find: (i) Number of subsets (ii) Number of proper subsets (iii) Write the power set $P(A)$... just count it.</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">$|A| = 4$, so total subsets $= 2^4 = 16$</div>
      <div class="step">Proper subsets $= 2^4 - 1 = 15$ (excludes $A$ itself)</div>
      <div class="step">Non-empty proper subsets $= 2^4 - 2 = 14$ (excludes both $\phi$ and $A$)</div>
      <div class="step">$P(A)$ has $2^4 = 16$ elements (16 subsets listed).</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 5: Intervals</strong>
    <span class="example-level level-easy">Easy</span>
  </div>
  <div class="example-q">Write the following in interval notation:<br>
  (i) $\{x : x \in \mathbb{R},\ -4 < x \le 6\}$<br>
  (ii) $\{x : x \in \mathbb{R},\ 3 \le x \le 4\}$</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">(i) $-4$ is excluded (strict $<$) and $6$ is included ($\le$). So: $(-4,\ 6]$ (open at left, closed at right).</div>
      <div class="step">(ii) Both $3$ and $4$ are included ($\le$ on both sides). So: $[3,\ 4]$ (closed interval).</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 6: Set Operations</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">Let $A = \{1, 2, 3, 4, 5, 6\}$ and $B = \{2, 4, 6, 8\}$. Find:<br>
  (i) $A \cup B$ &nbsp; (ii) $A \cap B$ &nbsp; (iii) $A - B$ &nbsp; (iv) $B - A$</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">(i) $A \cup B$ = all elements in $A$ or $B$ = $\{1, 2, 3, 4, 5, 6, 8\}$</div>
      <div class="step">(ii) $A \cap B$ = elements in both $A$ and $B$ = $\{2, 4, 6\}$</div>
      <div class="step">(iii) $A - B$ = elements in $A$ but not $B$ = $\{1, 3, 5\}$ (remove 2, 4, 6 from A)</div>
      <div class="step">(iv) $B - A$ = elements in $B$ but not $A$ = $\{8\}$ (remove 2, 4, 6 from B — only 8 remains)</div>
      <div class="step">Notice: $A - B \ne B - A$. The difference operation is not commutative!</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 7: Complement & De Morgan's Verification</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">Let $U = \{1,2,3,4,5,6,7,8,9,10\}$, $A = \{1,3,5,7,9\}$, $B = \{2,4,6,8,10\}$.<br>
  Verify: $(A \cup B)' = A' \cap B'$</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step"><strong>LHS:</strong> $A \cup B = \{1,2,3,4,5,6,7,8,9,10\} = U$, so $(A \cup B)' = U' = \phi$</div>
      <div class="step"><strong>RHS:</strong> $A' = U - A = \{2,4,6,8,10\}$ and $B' = U - B = \{1,3,5,7,9\}$</div>
      <div class="step">$A' \cap B'$ = elements common to both $A'$ and $B'$ = $\phi$ (they share no elements)</div>
      <div class="step">LHS $= \phi =$ RHS $\checkmark$ — De Morgan's Law verified!</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 8: Nested Set Problem</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">Let $A = \{1, 2, \{3, 4\}, 5\}$. State True or False:<br>
  (i) $\{3,4\} \in A$ &nbsp; (ii) $\{3,4\} \subset A$ &nbsp; (iii) $\{\{3,4\}\} \subset A$ &nbsp; (iv) $1 \in A$ &nbsp; (v) $\{1, 2, 5\} \subset A$</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">Think of $A$ as having 4 elements: $1$, $2$, $\{3,4\}$ (the whole set is one element), and $5$.</div>
      <div class="step">(i) $\{3,4\} \in A$ — <strong>TRUE</strong>. The set $\{3,4\}$ is listed as one of the 4 elements of $A$.</div>
      <div class="step">(ii) $\{3,4\} \subset A$ — <strong>FALSE</strong>. For this to be true, $3 \in A$ and $4 \in A$ must both hold. But $3$ is not a direct element of $A$ (only $\{3,4\}$ is).</div>
      <div class="step">(iii) $\{\{3,4\}\} \subset A$ — <strong>TRUE</strong>. This set has one element: $\{3,4\}$. Since $\{3,4\} \in A$, the set $\{\{3,4\}\}$ is a subset of $A$.</div>
      <div class="step">(iv) $1 \in A$ — <strong>TRUE</strong>. $1$ is directly listed as an element.</div>
      <div class="step">(v) $\{1, 2, 5\} \subset A$ — <strong>TRUE</strong>. All three ($1, 2, 5$) are elements of $A$.</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 9: Using Cardinality Formula (2 sets)</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">In a class of 40 students, 25 play cricket, 20 play football, and 15 play both. How many students play neither sport?</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">Let $C$ = cricket players, $F$ = football players. Given: $n(C) = 25$, $n(F) = 20$, $n(C \cap F) = 15$, total $= 40$.</div>
      <div class="step">Students playing at least one sport: $n(C \cup F) = n(C) + n(F) - n(C \cap F) = 25 + 20 - 15 = 30$</div>
      <div class="step">Students playing neither: $40 - n(C \cup F) = 40 - 30 = \mathbf{10}$</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 10: Find $n(A \cap B)$ when union is given</strong>
    <span class="example-level level-med">Medium</span>
  </div>
  <div class="example-q">If $n(A) = 14$, $n(B) = 11$, $n(A \cup B) = 21$, find $n(A \cap B)$.</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">Using: $n(A \cup B) = n(A) + n(B) - n(A \cap B)$</div>
      <div class="step">$21 = 14 + 11 - n(A \cap B)$</div>
      <div class="step">$n(A \cap B) = 14 + 11 - 21 = \mathbf{4}$</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 11: Prove a Set Identity</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">Prove that $A - B = A \cap B'$</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step"><strong>To prove A - B = A ∩ B', we show each is a subset of the other.</strong></div>
      <div class="step"><strong>Step 1 (LHS ⊆ RHS):</strong> Let $x \in A - B$. By definition, $x \in A$ and $x \notin B$. Since $x \notin B$, we have $x \in B'$. So $x \in A$ and $x \in B'$, which means $x \in A \cap B'$.</div>
      <div class="step"><strong>Step 2 (RHS ⊆ LHS):</strong> Let $x \in A \cap B'$. Then $x \in A$ and $x \in B'$. Since $x \in B'$, $x \notin B$. So $x \in A$ and $x \notin B$, which means $x \in A - B$.</div>
      <div class="step">Since $A - B \subseteq A \cap B'$ and $A \cap B' \subseteq A - B$, we have $A - B = A \cap B'$. (Proved)</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 12: Classic 3-Set Survey (NCERT type)</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">In a survey of 60 people, 25 read newspaper H, 26 read T, 26 read I, 9 read H and I, 11 read H and T, 8 read T and I, and 3 read all three. Find:<br>
  (i) How many read at least one newspaper?<br>
  (ii) How many read exactly one newspaper?<br>
  (iii) How many read exactly two newspapers?</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step"><strong>Given:</strong> $n(H)=25, n(T)=26, n(I)=26, n(H \cap I)=9, n(H \cap T)=11, n(T \cap I)=8, n(H \cap T \cap I)=3$</div>
      <div class="step"><strong>(i) At least one newspaper:</strong><br>
      $n(H \cup T \cup I) = 25+26+26 - (11+8+9) + 3 = 77 - 28 + 3 = \mathbf{52}$</div>
      <div class="step"><strong>(ii) Exactly two (meaning two only, not three):</strong><br>
      - Only H and T (not I) $= n(H \cap T) - n(H \cap T \cap I) = 11 - 3 = 8$<br>
      - Only T and I (not H) $= 8 - 3 = 5$<br>
      - Only H and I (not T) $= 9 - 3 = 6$<br>
      Total exactly two $= 8 + 5 + 6 = \mathbf{19}$</div>
      <div class="step"><strong>(iii) Exactly one newspaper:</strong><br>
      $= n(H \cup T \cup I) - [\text{exactly two}] - [\text{all three}] = 52 - 19 - 3 = \mathbf{30}$</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 13: Work backwards from union</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">If $n(A) = 3$, $n(B) = 6$ and $A \subset B$, find $n(A \cup B)$ and $n(A \cap B)$.</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">Since $A \subset B$ (A is a proper subset of B), every element of A is already in B.</div>
      <div class="step">Therefore $A \cap B = A$, so $n(A \cap B) = n(A) = \mathbf{3}$</div>
      <div class="step">And $A \cup B = B$, so $n(A \cup B) = n(B) = \mathbf{6}$</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 14: Power Set of Power Set</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">If $A = \{a, b\}$, find $P(P(A))$.</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step"><strong>Step 1:</strong> Find $P(A)$. Since $|A| = 2$, $P(A)$ has $2^2 = 4$ elements.<br>
      $P(A) = \{\phi, \{a\}, \{b\}, \{a,b\}\}$</div>
      <div class="step"><strong>Step 2:</strong> Find $P(P(A))$. Now $|P(A)| = 4$, so $P(P(A))$ has $2^4 = 16$ elements. It is the set of all subsets of $P(A)$, which includes $\phi$, all singletons, all pairs, all triples, and $P(A)$ itself.</div>
    </div>
  </details>
</div>

<div class="example-box">
  <div class="example-header">
    <strong>Example 15: Real-life 3-Set Problem (NCERT Ex 1.6)</strong>
    <span class="example-level level-hard">Hard</span>
  </div>
  <div class="example-q">In a group of 65 people, 40 like cricket, 10 like both cricket and tennis. How many like tennis only and not cricket? (Total tennis lovers = 35)</div>
  <details>
    <summary style="background:#7c3aed;color:#fff;padding:0.6rem 1.25rem;cursor:pointer;font-weight:600;">Show Solution</summary>
    <div class="example-sol">
      <div class="step">$n(C) = 40$, $n(T) = 35$, $n(C \cap T) = 10$</div>
      <div class="step">$n(C \cup T) = 40 + 35 - 10 = 65$</div>
      <div class="step">Tennis only (not cricket) $= n(T) - n(C \cap T) = 35 - 10 = \mathbf{25}$</div>
    </div>
  </details>
</div>

<!-- SECTION 10 -->
<h2 class="section-title" id="s10">[[BOOK]] 10. NCERT Exercise Solutions</h2>

<div class="ncert-box">
  <h4>Exercise 1.1 — Key Questions</h4>

  <div class="ncert-q">Q3(iii): Write the set $C = \{17, 26, 35, 44, 53, 62, 71, 80\}$ in Set-Builder form.</div>
  <div class="ncert-ans">Pattern: $17 = 9(1)+8,\ 26=9(2)+8,\ ...$. But simpler: these are numbers of the form $9n+8$ for $n=1,...,8$, or equivalently numbers where digits add to 8 and they are two-digit numbers: $C = \{x : x = 9n+8,\ n \in \mathbb{N},\ 1 \le n \le 8\}$</div>

  <div class="ncert-q">Q4(i): Write the set in Set-Builder form: $\{3, 6, 9, 12\}$</div>
  <div class="ncert-ans">$\{x : x = 3n,\ n \in \mathbb{N},\ 1 \le n \le 4\}$</div>

  <div class="ncert-q">Q5: Write as intervals: (i) $\{x \in \mathbb{R} : -4 < x \le 6\}$ (ii) $\{x \in \mathbb{R} : -12 < x < -10\}$</div>
  <div class="ncert-ans">(i) $(-4, 6]$ &nbsp; (ii) $(-12, -10)$</div>
</div>

<div class="ncert-box">
  <h4>Exercise 1.3 — Key Questions</h4>

  <div class="ncert-q">Q2: Examine whether $\{a, b\} \in \{a, b, \{a, b\}\}$.</div>
  <div class="ncert-ans">The set $\{a, b, \{a,b\}\}$ has 3 elements: $a$, $b$, and the set $\{a,b\}$. Since $\{a,b\}$ is listed as an element: YES, $\{a,b\} \in \{a, b, \{a,b\}\}$. TRUE.</div>

  <div class="ncert-q">Q3: Write all subsets of $\{1, 2, 3\}$.</div>
  <div class="ncert-ans">$\phi,\ \{1\},\ \{2\},\ \{3\},\ \{1,2\},\ \{1,3\},\ \{2,3\},\ \{1,2,3\}$ — total $2^3 = 8$ subsets.</div>

  <div class="ncert-q">Q4: How many elements does $P(A)$ have if $A = \phi$?</div>
  <div class="ncert-ans">$|A| = 0$, so $|P(A)| = 2^0 = 1$. $P(\phi) = \{\phi\}$ — one element (the empty set itself).</div>
</div>

<div class="ncert-box">
  <h4>Exercise 1.6 — Key Questions (Cardinality)</h4>

  <div class="ncert-q">Q2: If $n(A) = 5$, $n(B) = 7$, $n(A \cup B) = 10$, find $n(A \cap B)$.</div>
  <div class="ncert-ans">$n(A \cap B) = n(A) + n(B) - n(A \cup B) = 5 + 7 - 10 = 2$</div>

  <div class="ncert-q">Q8: In a committee, 50 people speak French, 20 speak Spanish, 10 speak both. How many speak at least one of these?</div>
  <div class="ncert-ans">$n(F \cup S) = 50 + 20 - 10 = 60$ people speak at least one language.</div>
</div>

<h2 class="section-title">[[ALERT]] Common Mistakes to Avoid</h2>
<div class="trap-card">
  <h4>[[ALERT]] Trap 1: $\phi \ne \{\phi\}$</h4>
  <p>$\phi$ is the empty set with zero elements. $\{\phi\}$ is a set containing the empty set — it has ONE element. They are completely different.</p>
</div>
<div class="trap-card">
  <h4>[[ALERT]] Trap 2: $\in$ vs $\subset$ — never mix these up</h4>
  <p>$x \in A$ says $x$ is an ELEMENT. $\{x\} \subset A$ says the set $\{x\}$ is a SUBSET. You can never write $x \subset A$ for a non-set element — it's meaningless.</p>
</div>
<div class="trap-card">
  <h4>[[ALERT]] Trap 3: $A - B \ne B - A$</h4>
  <p>Set difference is not commutative. Always check the order — "A minus B" removes B's elements from A.</p>
</div>
<div class="trap-card">
  <h4>[[ALERT]] Trap 4: Equal sets vs Equivalent sets</h4>
  <p>Equal sets have the same elements. Equivalent sets just have the same number of elements. $\{1,2,3\} \ne \{4,5,6\}$ but they are equivalent (both have 3 elements).</p>
</div>

<h2 class="section-title">[[QUIZ]] Quick Self-Check</h2>
<div class="quiz-card">
  <p><strong>Q1:</strong> Is $0 \in \phi$? (Is zero in the empty set?)</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">No. The empty set has NO elements. Nothing belongs to $\phi$.</div></details>
</div>
<div class="quiz-card">
  <p><strong>Q2:</strong> If $n(A) = 5$, how many non-empty proper subsets does $A$ have?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$2^5 - 2 = 32 - 2 = 30$. (Subtract 1 for $\phi$ and 1 for $A$ itself.)</div></details>
</div>
<div class="quiz-card">
  <p><strong>Q3:</strong> Let $U = \{1,...,10\}$, $A = \{2,4,6\}$. Find $(A')' $.</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$(A')' = A = \{2,4,6\}$. Double complement always gives back the original set.</div></details>
</div>
<div class="quiz-card">
  <p><strong>Q4:</strong> State De Morgan's second law.</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$(A \cap B)' = A' \cup B'$. The complement of an intersection equals the union of the complements.</div></details>
</div>
<div class="quiz-card">
  <p><strong>Q5:</strong> In a class of 50, 30 play chess, 25 play scrabble, 15 play both. How many play neither?</p>
  <details><summary>Answer</summary>
  <div class="quiz-ans">$n(\text{at least one}) = 30 + 25 - 15 = 40$. Neither $= 50 - 40 = 10$.</div></details>
</div>
"""

out = wrap("Sets", 1, None, "Chapter_2_Relations_and_Functions.html", ch1)
with open(os.path.join(BASE_DIR, "Chapter_1_Sets.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Chapter 1 written successfully!")
print("File size:", os.path.getsize(os.path.join(BASE_DIR, "Chapter_1_Sets.html")), "bytes")
