import os, random, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

# ---- edit these ------------------------------------------------------------
NAME = "Bagavati Narayanan"
HANDLE = "baggle11"
ROLE = "Final IT student at SSN College of Engineering, Chennai"
LOCATION = "Chennai"
STARS = 2
CONTRIBUTIONS = 277
REPOS = 10
FOLLOWERS = 0
CHIPS = ["Python", "TypeScript", "Jupyter Notebook", "JavaScript"]
PROJECTS = [
    ("AI-Content-Platform", "AI Content Platform is a FastAPI and Streamlit based multi-agent system for generating content.", ["Python"], 0, "updated 1 day ago", 85),
    ("virtual-photobooth", "Virtual Photobooth is a web app that lets you snap or upload photos and turn them into strips.", ["TypeScript", "Jupyter Notebook", "JavaScript"], 0, "updated 2 days ago", 65),
    ("Ask_your_Bookmarks", "Bookmark AI lets you semantically search your Chrome bookmarks using natural language.", ["TypeScript", "JavaScript", "HTML"], 1, "updated 10mo ago", 62),
    ("Finetuning_Deepseek_OCR", "Fine-tuning DeepSeek OCR 3B on Vietnamese handwritten text recognition.", ["Python"], 0, "updated 1 day ago", 100),
]
LANGS = [("Python", 81, "#4b8bbe"), ("TypeScript", 6, "#3178c6"), ("Jupyter Notebook", 5, "#f37726"),
         ("JavaScript", 4, "#f1e05a"), ("HTML", 4, "#e34c26")]
# ---------------------------------------------------------------------------

BG, BORDER, G, DIM, TXT = "#030b05", "#0f5a2a", "#39ff6a", "#2f8a4d", "#b6f5c8"
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Courier New',monospace"
esc = html.escape


def wrap(w, h, body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
<defs>
<radialGradient id="glow" cx="0.5" cy="0" r="0.9"><stop offset="0" stop-color="#0c7a30" stop-opacity="0.55"/><stop offset="1" stop-color="#030b05" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="#1fd45a"/><stop offset="1" stop-color="#39ff6a"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="2.2"/></filter>
{extra_defs}
</defs>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="{BG}" stroke="{BORDER}" stroke-width="1.5"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="url(#glow)"/>
{body}
</svg>'''


def save(name, svg):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


# ---------------- header ----------------
def header():
    w, h = 800, 130
    chips, x = "", 120
    for c in CHIPS:
        cw = 14 + len(c) * 7.2
        chips += f'<rect x="{x}" y="92" width="{cw}" height="22" rx="11" fill="#06200e" stroke="{BORDER}"/><text x="{x+cw/2}" y="107" fill="{G}" font-size="11" text-anchor="middle">{esc(c)}</text>'
        x += cw + 10
    body = f'''
<circle cx="64" cy="62" r="34" fill="#06200e" stroke="{G}" stroke-width="2"/>
<text x="64" y="71" fill="{G}" font-size="24" font-weight="700" text-anchor="middle">BN</text>
<text x="120" y="38" fill="{DIM}" font-size="12">@{esc(HANDLE)}</text>
<text x="120" y="72" fill="{G}" font-size="30" font-weight="700" filter="url(#blur)" opacity="0.6">{esc(NAME)}</text>
<text x="120" y="72" fill="{G}" font-size="30" font-weight="700">{esc(NAME)}</text>
<text x="120" y="88" fill="{DIM}" font-size="0"> </text>
{chips}
<text x="735" y="62" fill="{G}" font-size="34" font-weight="700" text-anchor="middle">{STARS}</text>
<text x="735" y="82" fill="{DIM}" font-size="9" letter-spacing="2" text-anchor="middle">TOTAL STARS</text>
<text x="{w-14}" y="{h-8}" fill="#145c2d" font-size="9" text-anchor="end">github.com</text>'''
    save("header.svg", wrap(w, h, body))


# ---------------- terminal ----------------
def terminal():
    w, h = 800, 270
    random.seed(7)
    art = ""
    rows, cols = 26, 40
    for r in range(rows):
        half = int((r / rows) * (cols / 2 - 2)) + 1
        line = " " * (cols // 2 - half) + "".join(random.choice("01{}<>/;=") for _ in range(half * 2))
        art += f'<text x="30" y="{58 + r*8}" fill="{G}" font-size="7" opacity="{0.35 + 0.65*r/rows:.2f}" xml:space="preserve">{esc(line)}</text>'
    info = [("subject", NAME), ("handle", "@" + HANDLE), ("role", ROLE), ("status", "building | learning | shipping"),
            ("languages", ", ".join(c.lower() for c in CHIPS)), ("repositories", str(REPOS)),
            ("contributions", str(CONTRIBUTIONS)), ("stars", str(STARS)), ("followers", str(FOLLOWERS)),
            ("location", LOCATION), ("contact", f"github.com/{HANDLE}")]
    rows_svg = ""
    for i, (k, v) in enumerate(info):
        y = 70 + i * 17
        rows_svg += f'<text x="355" y="{y}" fill="{DIM}" font-size="11">{k}</text><text x="440" y="{y}" fill="{TXT}" font-size="11">{esc(v)}</text>'
    body = f'''
<circle cx="20" cy="18" r="4" fill="#ff5f56"/><circle cx="34" cy="18" r="4" fill="#ffbd2e"/><circle cx="48" cy="18" r="4" fill="#27c93f"/>
<text x="400" y="22" fill="{DIM}" font-size="10" text-anchor="middle">{esc(HANDLE)}@github ~ github.com ~ zsh</text>
<line x1="1" y1="34" x2="{w-1}" y2="34" stroke="{BORDER}"/>
{art}
<line x1="335" y1="46" x2="335" y2="{h-16}" stroke="{BORDER}"/>
<text x="355" y="52" fill="{G}" font-size="11">$ whoami</text>
{rows_svg}'''
    save("terminal.svg", wrap(w, h, body))


# ---------------- projects ----------------
def projects():
    w, h = 800, 330
    cards = ""
    cw, ch = 372, 118
    for i, (name, desc, tags, stars, upd, pct) in enumerate(PROJECTS):
        x, y = 20 + (i % 2) * (cw + 16), 52 + (i // 2) * (ch + 14)
        # wrap description to 2 lines
        words, lines, cur = desc.split(), [], ""
        for wd in words:
            if len(cur) + len(wd) > 46:
                lines.append(cur); cur = wd
            else:
                cur = (cur + " " + wd).strip()
        lines.append(cur)
        lines = lines[:2]
        if len(" ".join(words)) > 92:
            lines[1] = lines[1][:43] + "..."
        d = "".join(f'<text x="{x+14}" y="{y+52+j*14}" fill="{TXT}" font-size="10.5">{esc(l)}</text>' for j, l in enumerate(lines))
        tx, t = x + 14, ""
        for tg in tags[:3]:
            tw = 12 + len(tg) * 6
            t += f'<rect x="{tx}" y="{y+76}" width="{tw}" height="16" rx="3" fill="#06200e" stroke="{BORDER}"/><text x="{tx+tw/2}" y="{y+88}" fill="{G}" font-size="9" text-anchor="middle">{esc(tg)}</text>'
            tx += tw + 6
        r = 20
        circ = 2 * 3.14159 * r
        ring = f'''<g transform="translate({x+cw-42},{y+60})"><circle r="{r}" fill="none" stroke="#0a2d15" stroke-width="4"/>
<circle r="{r}" fill="none" stroke="{G}" stroke-width="4" stroke-linecap="round" stroke-dasharray="{circ*pct/100:.1f} {circ:.1f}" transform="rotate(-90)"/>
<text y="4" fill="{G}" font-size="10" text-anchor="middle">{pct}%</text></g>'''
        cards += f'''<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8" fill="#041208" stroke="{BORDER}"/>
<text x="{x+14}" y="{y+26}" fill="{G}" font-size="13" font-weight="700">&gt; {esc(name)}</text>
{d}{t}{ring}
<text x="{x+14}" y="{y+108}" fill="{DIM}" font-size="9">&#9733; {stars}   {esc(upd)}</text>'''
    body = f'''<text x="20" y="30" fill="{G}" font-size="13" font-weight="700">PROJECTS.LIST</text>
<text x="150" y="30" fill="{DIM}" font-size="10">./pinned.sh --all</text>
<text x="{w-20}" y="30" fill="{DIM}" font-size="10" text-anchor="end">{len(PROJECTS)} pinned</text>
{cards}'''
    save("projects.svg", wrap(w, h, body))


# ---------------- languages ----------------
def languages():
    w, h = 800, 220
    rows = ""
    for i, (n, p, c) in enumerate(LANGS):
        y = 70 + i * 28
        bw = 440 * p / 100
        rows += f'''<circle cx="34" cy="{y-4}" r="4" fill="{c}"/><text x="46" y="{y}" fill="{TXT}" font-size="12">{esc(n)}</text>
<rect x="220" y="{y-10}" width="440" height="8" rx="4" fill="#0a2d15"/><rect x="220" y="{y-10}" width="{max(bw,6):.1f}" height="8" rx="4" fill="{c}"/>
<text x="780" y="{y}" fill="{G}" font-size="12" text-anchor="end">{p}%</text>'''
    body = f'''<text x="20" y="32" fill="{G}" font-size="16" font-weight="700">Language Stack</text>
<text x="20" y="48" fill="{DIM}" font-size="10">Repository-weighted technologies</text>
<text x="{w-20}" y="32" fill="{G}" font-size="11" text-anchor="end">&gt; stack.scan _</text>
{rows}'''
    save("languages.svg", wrap(w, h, body))


# ---------------- contributions ----------------
def contributions():
    w, h = 800, 190
    random.seed(11)
    cols, rows, size, gap = 52, 7, 11, 3
    ox, oy = 20, 62
    cells = ""
    shades = ["#0a2d15", "#0e5a26", "#17913b", "#27c93f", "#39ff6a"]
    total = 0
    for c in range(cols):
        for r in range(rows):
            v = random.choices([0, 1, 2, 3, 4], [55, 20, 13, 8, 4])[0]
            cells += f'<rect x="{ox + c*(size+gap)}" y="{oy + r*(size+gap)}" width="{size}" height="{size}" rx="2" fill="{shades[v]}"/>'
    lg = "".join(f'<rect x="{w-120+i*14}" y="26" width="10" height="10" rx="2" fill="{s}"/>' for i, s in enumerate(shades))
    body = f'''<text x="20" y="32" fill="{G}" font-size="16" font-weight="700">Contribution Activity</text>
<text x="20" y="48" fill="{DIM}" font-size="10">{CONTRIBUTIONS} contributions in the last year</text>
<text x="{w-132}" y="35" fill="{DIM}" font-size="9" text-anchor="end">Less</text>{lg}<text x="{w-46}" y="35" fill="{DIM}" font-size="9">More</text>
{cells}'''
    save("contributions.svg", wrap(w, h, body))


for fn in (header, terminal, projects, languages, contributions):
    fn()

readme = f'''<div align="center">

<img src="assets/header.svg" alt="{NAME}" width="100%"/>
<img src="assets/terminal.svg" alt="terminal" width="100%"/>
<img src="assets/projects.svg" alt="projects" width="100%"/>
<img src="assets/languages.svg" alt="language stack" width="100%"/>
<img src="assets/contributions.svg" alt="contribution activity" width="100%"/>

</div>
'''
with open(os.path.join(os.path.dirname(OUT), "README.md"), "w") as f:
    f.write(readme)
print("done")
