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
    "CHECK": '<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
}

def si(text):
    for k, v in SVGS.items():
        text = text.replace(f"[[{k}]]", v)
    return text

def wrap(title, num, prev, nxt, body, custom_css=""):
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
    .concept-box p, .concept-box ul, .concept-box ol {{ color:#bfdbfe; font-size:0.95rem; margin-bottom:0.4rem; }}
    .concept-box ul, .concept-box ol {{ padding-left:1.25rem; }}
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
    .table-container {{ overflow-x:auto; margin-bottom:1.25rem; }}
    table.data-table {{ width:100%; border-collapse:collapse; background:#ffffff; border-radius:8px; overflow:hidden; }}
    table.data-table th {{ background:#1e293b; color:#ffffff; padding:0.75rem 1rem; text-align:left; font-size:0.9rem; }}
    table.data-table td {{ padding:0.75rem 1rem; border-bottom:1px solid #e2e8f0; font-size:0.9rem; color:#1e293b; }}
    table.data-table tr:nth-child(even) td {{ background:#f8fafc; }}
    {custom_css}
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
