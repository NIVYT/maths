def update_index():
    with open(r'Revision_Notes\index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    replacements = [
        ('<span class="ch-num">Chapter 1</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 20m</span>',
         '<span class="ch-num">Chapter 1 • 4–6 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 45m</span>'),

        ('<span class="ch-num">Chapter 2</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 25m</span>',
         '<span class="ch-num">Chapter 2 • 6–8 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 45m</span>'),

        ('<span class="ch-num">Chapter 3</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 35m</span>',
         '<span class="ch-num">Chapter 3 • 8–10 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 55m</span>'),

        ('<span class="ch-num">Chapter 4</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 25m</span>',
         '<span class="ch-num">Chapter 4 • 5–6 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 40m</span>'),

        ('<span class="ch-num">Chapter 5</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 20m</span>',
         '<span class="ch-num">Chapter 5 • 4–6 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 35m</span>'),

        ('<span class="ch-num">Chapter 6</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 30m</span>',
         '<span class="ch-num">Chapter 6 • 6–8 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 50m</span>'),

        ('<span class="ch-num">Chapter 7</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 25m</span>',
         '<span class="ch-num">Chapter 7 • 4–6 Marks</span>\n            <span class="ch-time"><svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> 40m</span>'),
    ]

    count = 0
    for old, new in replacements:
        if old in html:
            html = html.replace(old, new)
            count += 1
        else:
            # Normalize whitespace and try regex
            pattern = re.escape(old).replace(r'\ ', r'\s+').replace(r'\n', r'\s+')
            if re.search(pattern, html):
                html = re.sub(pattern, new, html, count=1)
                count += 1

    with open(r'Revision_Notes\index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Updated {count}/7 chapter card badges in index.html!")

if __name__ == "__main__":
    update_index()
