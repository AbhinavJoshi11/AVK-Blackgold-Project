#!/usr/bin/env python3
"""
build.py — generates every page for the AVK Blackgold Infra site.
Shared shell + quote modal live here once; page bodies are defined below.
Run:  python3 build.py   ->  writes .html files next to this script.
Content is ORIGINAL placeholder copy for AVK Blackgold (edit freely).
"""
import os, textwrap

OUT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(OUT, "assets", "img")
os.makedirs(IMGDIR, exist_ok=True)

# ---------- dummy image generator (on-theme SVG, works offline) ----------
import re as _re
_imgcache = {}
def _slug(s):
    return _re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40] or "img"

def genimg(label, w=800, h=600, slug=None):
    slug = slug or _slug(label)
    rel = "assets/img/%s.svg" % slug
    if slug not in _imgcache:
        lane_y = int(h * 0.66)
        svg = (
'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" preserveAspectRatio="xMidYMid slice" role="img" aria-label="%s">'
'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
'<stop offset="0" stop-color="#2a231c"/><stop offset="1" stop-color="#15120f"/></linearGradient></defs>'
'<rect width="%d" height="%d" fill="url(#g)"/>'
'<line x1="0" y1="%d" x2="%d" y2="%d" stroke="#f4c430" stroke-width="6" stroke-dasharray="40 32" opacity="0.16"/>'
'<rect x="0" y="0" width="74" height="26" fill="#df6315"/>'
'<text x="12" y="18" font-family="monospace" font-size="13" font-weight="700" fill="#fff" letter-spacing="2">AVK</text>'
'<text x="50%%" y="49%%" font-family="monospace" font-size="20" fill="#7d7466" text-anchor="middle" letter-spacing="3">%s</text>'
'<text x="50%%" y="49%%" dy="26" font-family="monospace" font-size="12" fill="#52493f" text-anchor="middle" letter-spacing="2">%d x %d</text>'
'</svg>'
        ) % (w, h, w, h, label, w, h, lane_y, w, lane_y, label.upper()[:34], w, h)
        with open(os.path.join(IMGDIR, slug + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(svg)
        _imgcache[slug] = True
    return rel

def portrait(name):
    slug = "team-" + _slug(name)
    rel = "assets/img/%s.svg" % slug
    if slug not in _imgcache:
        svg = (
'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-label="%s">'
'<rect width="400" height="400" fill="#241d17"/>'
'<circle cx="200" cy="160" r="70" fill="#3a3129"/>'
'<path d="M70 380c0-80 60-120 130-120s130 40 130 120z" fill="#3a3129"/>'
'<rect x="0" y="0" width="74" height="26" fill="#df6315"/>'
'<text x="12" y="18" font-family="monospace" font-size="13" font-weight="700" fill="#fff" letter-spacing="2">AVK</text>'
'</svg>') % name
        with open(os.path.join(IMGDIR, slug + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(svg)
        _imgcache[slug] = True
    return rel

def figimg(label, classes="", w=800, h=600):
    cls = ("figbox " + classes).strip()
    return '<div class="%s"><img src="%s" alt="%s"></div>' % (cls, genimg(label, w, h), label)

# ---------- lorem ----------
_L = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor "
"incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
"exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ")
_L2 = ("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
"fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa "
"qui officia deserunt mollit anim id est laborum. ")
_L3 = ("Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis "
"et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. ")
def lorem(n=1):
    src = [_L, _L2, _L3]
    return "".join("<p>%s</p>" % src[i % 3] for i in range(n))

# ---------- shared shell ----------
QUOTE_MODAL = """
<div class="modal" id="quote-modal" role="dialog" aria-modal="true" aria-label="Request a quotation">
  <div class="modal__scrim" data-close-modal></div>
  <div class="modal__panel">
    <button class="modal__close" data-close-modal aria-label="Close">&times;</button>
    <span class="eyebrow">Request a Quotation</span>
    <h2 class="h-sec" style="margin-bottom:1.2rem">Tell us what you need</h2>
    <form data-form data-subject="Quotation Request">
      <div class="form-grid">
        <div class="field"><label>Name <span class="req">*</span></label><input name="name" required><span class="err">Enter your name</span></div>
        <div class="field"><label>Designation <span class="req">*</span></label><input name="designation" required><span class="err">Required</span></div>
        <div class="field"><label>Email <span class="req">*</span></label><input type="email" name="email" required><span class="err">Enter a valid email</span></div>
        <div class="field"><label>Phone Number <span class="req">*</span></label><input name="phone" required><span class="err">Required</span></div>
        <div class="field"><label>Company Name <span class="req">*</span></label><input name="company" required><span class="err">Required</span></div>
        <div class="field"><label>Emulsion Grade <span class="req">*</span></label><select name="grade" required><option value="">Choose from dropdown</option>__GRADES__</select><span class="err">Select a grade</span></div>
        <div class="field"><label>Location <span class="req">*</span></label><input name="location" required><span class="err">Required</span></div>
        <div class="field"><label>Project Name</label><input name="project"></div>
        <div class="field full"><label>Specific Requirement</label><textarea name="requirement"></textarea></div>
      </div>
      <label class="consent"><input type="checkbox" name="consent" required>
        <span>I authorise the AVK Blackgold sales team to contact me via phone, text and email, and acknowledge my information may be stored per the privacy policy. <span class="req">*</span></span></label>
      <button class="btn btn--primary btn--lg" type="submit">Submit Request <span class="arr">&rarr;</span></button>
      <div class="form-status" role="status"></div>
    </form>
  </div>
</div>
<a class="qbtn-fab" href="#" data-open-quote>Request a Quotation</a>
"""

def shell(filename, title, desc, body):
    grades = "".join("<option>%s</option>" % g for g in EMULSION_GRADES)
    modal = QUOTE_MODAL.replace("__GRADES__", grades)
    return textwrap.dedent("""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <script>(function(){try{var t=localStorage.getItem('avk-theme')||'light';document.documentElement.setAttribute('data-theme',t);}catch(e){document.documentElement.setAttribute('data-theme','light');}document.documentElement.classList.add('js');})();</script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>%s</title>
    <meta name="description" content="%s">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/styles.css">
    </head>
    <body>
    <a class="skip" href="#main">Skip to content</a>
    <div id="site-header"></div>
    <main id="main">
    %s
    </main>
    <div id="site-footer"></div>
    %s
    <script src="assets/js/site.config.js"></script>
    <script src="assets/js/components.js"></script>
    <script src="assets/js/main.js"></script>
    </body>
    </html>
    """) % (title, desc, body, modal)

EMULSION_GRADES = [
    "Rapid Setting 1","Rapid Setting 2","Medium Setting","Slow Setting SS1",
    "Slow Setting 2","Slow Setting 1 ASTM","Slow Setting 1h","RAP Emulsion",
    "SS2 Stab","Prime SS1 (ASTM)",
]

# ---------- small builders ----------
def phero(title, desc, crumb):
    return """
    <section class="phero"><div class="phero__glow"></div><div class="wrap">
      <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; %s</p>
      <h1>%s</h1><p>%s</p>
    </div></section>
    <div class="lane"></div>""" % (crumb, title, desc)

def card(tag, title, body, href, link="Explore More"):
    return """
    <article class="card reveal">
      <div class="card__img" data-tag="%s"><img src="%s" alt="%s"></div>
      <div class="card__body"><h3>%s</h3><p>%s</p>
        <a class="card__link" href="%s">%s <span class="arr">&rarr;</span></a></div>
    </article>""" % (tag, genimg(title, 800, 450), title, title, body, href, link)

def stat(num, accent, lab, desc):
    return """<div class="stat reveal"><div class="num">%s<span>%s</span></div>
      <div class="lab">%s</div><div class="desc">%s</div></div>""" % (num, accent, lab, desc)

def spec_rows(rows):
    return "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)

# ============================================================
#  PAGE BODIES  (original copy — edit anytime)
# ============================================================
PAGES = {}

# ---------------- HOME ----------------
PAGES["index.html"] = dict(
    title="AVK Blackgold Infra | Bituminous Products & Road Solutions",
    desc="AVK Blackgold Infra manufactures bitumen emulsions, modified bitumen (CRMB/PMB), special products and road maintenance services for highways and infrastructure.",
    body="""
<section class="hero">
  <div class="hero__media">
    <video autoplay muted loop playsinline poster="assets/img/hero.svg">
      <source src="assets/videos/245030_medium.mp4" type="video/mp4">
    </video></div>
  <div class="hero__glow"></div>
  <div class="wrap hero__inner">
    <span class="eyebrow">AVK Blackgold Infra Pvt. Ltd.</span>
    <h1 class="display">Engineered<br>Bituminous<br>Solutions</h1>
    <p class="hero__sub">High-performance bitumen products and road maintenance services, built for India's highways, runways and expressways.</p>
    <div class="hero__cta">
      <a class="btn btn--primary btn--lg" href="#products">Explore Products <span class="arr">&rarr;</span></a>
      <a class="btn btn--ghost btn--lg" href="#" data-open-quote>Request a Quote</a>
    </div>
  </div>
  <div class="lane"></div><div class="heatline"></div>
</section>

<!-- ABOUT TEASER -->
<section class="section"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">About AVK Blackgold</span>
    <h2 class="h-sec">Your trusted partner in delivering commitments</h2>
    <p class="lead">AVK Blackgold Infra is a construction and distribution company bringing globally established road and building technologies to India. Established in 2021, our purpose is simple &mdash; make roads more durable, longer lasting and greener, using the best cost-effective solutions available.</p>
    <a class="btn btn--ghost mt2" href="about-us.html">More about us <span class="arr">&rarr;</span></a>
  </div>
  <div class="figbox reveal">company image</div>
</div></section>

<!-- STATS -->
<section class="section--dark section--tight"><div class="wrap">
  <div class="stats">
    %s%s%s%s
  </div>
</div></section>

<!-- PRODUCTS -->
<section class="section anchor" id="products"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Our Products</span>
    <h2 class="h-sec">Value-added bituminous products</h2>
    <p class="lead">A range engineered for performance and durability across road and infrastructure applications, manufactured to relevant BIS / ASTM standards.</p></div>
  <div class="grid cols-4">
    %s%s%s%s
  </div>
</div></section>

<!-- SERVICES -->
<section class="section--dark"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Our Services</span>
    <h2 class="h-sec">Road repair &amp; maintenance</h2>
    <p class="lead">Comprehensive services backed by experienced teams and modern equipment, for reliable results on every project.</p></div>
  <div class="grid cols-4">
    %s%s%s%s
  </div>
</div></section>

<!-- CLIENTS -->
<section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Our Clients</span>
    <h2 class="h-sec">Where our products perform</h2></div>
  <div class="grid cols-3">
    %s%s%s
  </div>
</div></section>

<!-- KNOWLEDGE -->
<section class="section--dark"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Knowledge @ AVK</span>
    <h2 class="h-sec">From the field &amp; the lab</h2></div>
  <div class="grid cols-3">
    %s%s%s
  </div>
  <a class="btn btn--ghost mt2" href="blogs.html">All articles <span class="arr">&rarr;</span></a>
</div></section>

<!-- FEEDBACK -->
<section class="section"><div class="wrap" style="max-width:820px">
  <div class="sec-head center" style="margin-inline:auto"><span class="eyebrow" style="justify-content:center">Customer Feedback</span>
    <h2 class="h-sec">Tell us how we're doing</h2>
    <p class="lead" style="margin-inline:auto">Your feedback helps us improve our products and service. It takes a minute.</p></div>
  %s
</div></section>
""" % (
    stat("2021","","Established","Founded to bring globally proven road and building technologies to Indian infrastructure."),
    stat("7L","+","Sq.M Microsurfaced","NH &amp; SH microsurfacing completed with premier customers in 2023&ndash;24."),
    stat("25-45","%","Life-cycle Cost Saved","Microsurfacing versus traditional resurfacing methods."),
    stat("44","%","Lower Emissions","Reduction in greenhouse gases versus traditional resurfacing."),
    card("Emulsion","Bitumen Emulsion","Prasol-based emulsifiers and emulsions for tack, prime and microsurfacing &mdash; superior performance with lower energy use.","bitumen-emulsions.html"),
    card("Modified","Modified Bitumen","Kraton SBS polymer-modified bitumen (PMB &amp; CRMB) for HiMA and conventional mixes on high-traffic roads.","pmb.html"),
    card("Repair","Re-Active Pothole Repair","BG Re-Active ready-to-use asphalt for quick, durable, all-weather pothole and patch repair.","roadbond.html"),
    card("Special","Special Products","Rejuvenators, anti-stripping agents, warmix additives, SBR latex and cellulose fibre for SMA.","special-products.html"),
    card("Service","Microsurfacing","Polymer-modified surface treatment &mdash; over 7 lakh sq.m of NH &amp; SH delivered in 2023&ndash;24, adding 6&ndash;8 years of life.","services.html#Microsurfacing"),
    card("Service","Coldmix Design","Custom cold-mix formulations applied at ambient temperature, with no heating required.","services.html#Coldmix"),
    card("Service","Pavement Preservation","Rhinophalt and rejuvenator-based preservation that extends pavement and runway service life.","services.html#Technical-Consultancy"),
    card("Service","Technical Consultancy","Product research, technical support and proven global technologies for road construction.","services.html#Technical-Consultancy"),
    card("Sector","Highways & Expressways","Binders and treatments for national highways and high-traffic expressways.","our-clients.html#Highways"),
    card("Sector","Runways","Specialised products engineered for airport runways and aprons.","our-clients.html#MES"),
    card("Sector","Race & Test Tracks","High-specification surfacing for race circuits and vehicle test tracks.","our-clients.html#Racetracks"),
    card("Article","Understanding RS1 grade emulsion","What RS1 bitumen emulsion is and where it fits in road construction.","blog-rs1-grade.html","Read more"),
    card("Article","Where does bitumen come from?","The story behind this ancient material and how it reaches the road.","blog-where-bitumen.html","Read more"),
    card("Article","How bitumen is made","The refinery process that produces bitumen, explained simply.","blog-how-bitumen-made.html","Read more"),
    # feedback form
    """<form data-form data-subject="Customer Feedback" class="reveal">
      <div class="form-grid">
        <div class="field"><label>Name <span class="req">*</span></label><input name="name" required><span class="err">Required</span></div>
        <div class="field"><label>Company Name <span class="req">*</span></label><input name="company" required><span class="err">Required</span></div>
        <div class="field"><label>Email <span class="req">*</span></label><input type="email" name="email" required><span class="err">Valid email required</span></div>
        <div class="field"><label>Mobile Number <span class="req">*</span></label><input name="mobile" required><span class="err">Required</span></div>
        <div class="field full"><label>Which road segment do you mainly execute? <span class="req">*</span></label>
          <select name="segment" required><option value="">Choose from dropdown</option>
            <option>PMGSY / Rural Projects</option><option>NHAI / State Highway Projects</option>
            <option>Repair & Maintenance Projects</option><option>Other</option></select><span class="err">Required</span></div>
      </div>
      <div class="rating-grid">
        <div class="field"><label>Rate product quality (1-10) <span class="req">*</span></label><input name="rate_quality" type="number" min="1" max="10" required><span class="err">1-10</span></div>
        <div class="field"><label>Rate delivery time (1-10) <span class="req">*</span></label><input name="rate_delivery" type="number" min="1" max="10" required><span class="err">1-10</span></div>
        <div class="field"><label>Rate documentation (1-10) <span class="req">*</span></label><input name="rate_docs" type="number" min="1" max="10" required><span class="err">1-10</span></div>
        <div class="field"><label>Rate sales availability (1-10) <span class="req">*</span></label><input name="rate_sales" type="number" min="1" max="10" required><span class="err">1-10</span></div>
      </div>
      <div class="field full"><label>How can we serve you better? <span class="req">*</span></label><textarea name="suggestions" required></textarea><span class="err">Required</span></div>
      <label class="consent"><input type="checkbox" name="consent" required>
        <span>I consent to the collection, storage and processing of my data per the applicable privacy policy. <span class="req">*</span></span></label>
      <button class="btn btn--primary btn--lg" type="submit">Submit Feedback <span class="arr">&rarr;</span></button>
      <div class="form-status" role="status"></div>
    </form>""",
))

build_list = []  # populated below by helper

def add_inner(fname, title, desc, crumb, body):
    PAGES[fname] = dict(title=title + " | AVK Blackgold Infra", desc=desc,
        body=phero(title, desc, crumb) + body)

# ---------------- ABOUT ----------------
add_inner("about-us.html","About AVK Blackgold",
    "Who we are: our vision, values, quality systems, research and leadership.","About Us",
    """
<section class="section"><div class="wrap prose reveal">
  <span class="eyebrow">Our Story</span>
  <h2 class="mt0">Shaping the future with innovative solutions</h2>
  <p>AVK Blackgold Infra Private Limited is a construction and distribution company bringing globally established road and building construction technologies to India. Established in 2021, we supply value-added bituminous products and road-preservation solutions that make roads more durable, longer lasting and more sustainable.</p>
  <p>We work with world-class technology partners &mdash; including Kraton, Prasol, Rhinophalt, BG Re-Active and K31 Road Engineering &mdash; to bring proven materials to Indian highways, expressways, runways and city roads. Road preservation, done right, is one step forward to a more sustainable future.</p>

  <h2 class="anchor" id="Vision">Vision</h2>
  <p>To make roads more durable and long lasting using the best available greener and cost-effective solutions &mdash; because road preservation is one step forward to a sustainable future.</p>

  <h2 class="anchor" id="Core-Values">Core values</h2>
  <ul><li>Durable, longer-lasting roads</li><li>Greener, cost-effective solutions</li><li>Globally proven technologies</li><li>Reliability our customers can plan around</li><li>Responsibility to communities and the environment</li></ul>

  <h2 class="anchor" id="Quality">Quality</h2>
  <p>Our products meet relevant BIS and ASTM standards, and our raw materials come from established global suppliers, so that what reaches the road performs as specified.</p>

  <h2 class="anchor" id="RD">Technology partners</h2>
  <p>Kraton SBS polymers for PMB and HiMA, Prasol bitumen emulsifiers, SBR latex for microsurfacing, rejuvenators and anti-strip for recycling (RAP), cellulose fibre for SMA, K31 soil stabilisation, BG Re-Active for pothole repair, and Rhinophalt for pavement and runway preservation.</p>

  <h2 class="anchor" id="Certificates">Certificates</h2>
  <p><em>EDIT: list your certifications and accreditations here.</em></p>
  <div class="tagrow"><span class="tag">ISO &mdash;</span><span class="tag">BIS &mdash;</span><span class="tag">Lab accreditation &mdash;</span></div>

  <h2 class="anchor" id="Leadership">Leadership team</h2>
  <p>%s</p>
  </div>
  <div class="wrap" style="margin-top:32px"><div class="grid cols-4">__TEAM__</div></div>
</section>""" % _L)

# ---------------- RESPONSIBLE COMMITMENT ----------------
add_inner("responsible-commitment.html","Responsible Commitment",
    "Our commitments to community, environment, health and safety, risk and ethics.","Responsible Commitment",
    """
<section class="section"><div class="wrap prose reveal">
  <h2 class="anchor mt0" id="CSR">Corporate social responsibility</h2>
  <p>We invest in the communities around our operations through programmes in education, skilling and local development. <em>(EDIT with your CSR initiatives.)</em></p>
  <h2 class="anchor" id="Sustainability">Sustainability</h2>
  <p>We work to reduce the environmental footprint of our products and processes, including cold-application technologies that lower energy use.</p>
  <h2 class="anchor" id="HSE">Health, safety &amp; environment</h2>
  <p>Safety is built into how we operate &mdash; from plant procedures to site support &mdash; with the goal of zero harm to people and the environment.</p>
  <h2 class="anchor" id="Risk">Risk management</h2>
  <p>We identify, assess and manage operational and supply risks so that our customers experience reliable, uninterrupted service.</p>
  <h2 class="anchor" id="Whistleblower">Whistleblower</h2>
  <p>We maintain a confidential channel for raising concerns about unethical conduct. <em>(EDIT: add your reporting contact / policy link.)</em></p>
</div></section>""")

# ---------------- CLIENTS ----------------
add_inner("our-clients.html","Our Clients",
    "The sectors and projects our bituminous products serve.","Our Clients",
    """
<section class="section"><div class="wrap">
  <div class="grid cols-2">
    <div class="figbox reveal anchor" id="Highways">highways image</div>
    <div class="reveal prose"><span class="eyebrow">Sector</span><h2 class="mt0">Highways &amp; Expressways</h2>
      <p>Binders and surface treatments engineered for the loads and traffic of national highways and expressways, delivering durability and ride quality.</p></div>
  </div>
  <div class="grid cols-2" style="margin-top:48px">
    <div class="reveal prose anchor" id="MES"><span class="eyebrow">Sector</span><h2 class="mt0">Runways &amp; Airports</h2>
      <p>High-specification products for runways, taxiways and aprons, where surface performance and safety margins are critical.</p></div>
    <div class="figbox reveal">runway image</div>
  </div>
  <div class="grid cols-2" style="margin-top:48px">
    <div class="figbox reveal anchor" id="Racetracks">race track image</div>
    <div class="reveal prose"><span class="eyebrow">Sector</span><h2 class="mt0">Race &amp; Test Tracks</h2>
      <p>Precision surfacing for race circuits and vehicle test tracks, where grip and consistency directly affect performance.</p></div>
  </div>
</div></section>""")

# ---------------- PRODUCT PAGES ----------------
def product_page(fname, name, desc, intro, rows, apps):
    body = """
<section class="section"><div class="wrap">
  <div class="split">
    <div class="reveal prose"><span class="eyebrow">Product</span><h2 class="mt0">%s</h2>
      <p class="lead">%s</p>
      <a class="btn btn--primary mt2" href="#" data-open-quote>Request a quote <span class="arr">&rarr;</span></a></div>
    <div class="figbox reveal">product image</div>
  </div>
</div></section>
<section class="section--dark"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Typical Grades</span><h2 class="h-sec">Grades &amp; specifications</h2>
    <p class="lead">Indicative grades below &mdash; <em>EDIT to match your catalogue and test certificates.</em></p></div>
  <table class="spectable"><caption>Representative grades</caption>
    <thead><tr><th>Grade</th><th>Description</th><th>Typical use</th></tr></thead>
    <tbody>%s</tbody></table>
</div></section>
<section class="section"><div class="wrap prose reveal">
  <h2 class="mt0">Applications</h2><ul>%s</ul>
</div></section>""" % (name, intro, spec_rows(rows), "".join("<li>%s</li>" % a for a in apps))
    PAGES[fname] = dict(title=name + " | AVK Blackgold Infra",
        desc=desc, body=phero(name, desc, "What We Do / " + name) + body)

product_page("bitumen-emulsions.html","Bitumen Emulsions",
    "High-quality bitumen emulsions for road construction and maintenance, made to BIS/ASTM standards.",
    "Water-based bitumen emulsions for surface treatments, tack and prime coats, and cold-mix work &mdash; offering superior performance and sustainability for roads and pavements.",
    [["RS-1","Rapid setting","Surface dressing, tack coat"],
     ["RS-2","Rapid setting (higher viscosity)","Surface dressing"],
     ["MS","Medium setting","Premix with coarse aggregate"],
     ["SS-1","Slow setting","Prime coat, fine premix"],
     ["SS-2","Slow setting","Slurry seal, microsurfacing"]],
    ["Tack and prime coats","Surface dressing and chip seals","Slurry seal and microsurfacing","Cold-mix patching and recycling"])

product_page("crmb.html","Crumb Rubber Modified Bitumen (CRMB)",
    "CRMB for durable, high-performance road surfaces using recycled crumb rubber.",
    "Bitumen modified with recycled crumb rubber to improve elasticity, temperature resistance and fatigue life &mdash; well suited to heavy-traffic roads.",
    [["CRMB 50","Softer grade","Cooler regions"],
     ["CRMB 55","Standard grade","General highway use"],
     ["CRMB 60","Stiffer grade","Hot climates, heavy traffic"]],
    ["Heavy-traffic highways","High-temperature regions","Overlays on distressed pavement"])

product_page("pmb.html","Polymer Modified Bitumen (PMB)",
    "Kraton SBS polymer-modified bitumen for HiMA and conventional mixes on highways, runways and expressways.",
    "Bitumen modified with Kraton SBS polymers for superior resistance to rutting, cracking and ageing &mdash; supporting both HiMA (Highly Modified Asphalt) and conventional PMB for demanding infrastructure.",
    [["D1101 E","Kraton SBS for PMB","Highways, expressways"],
     ["D1192 E","Kraton SBS for PMB","High-traffic / HiMA mixes"],
     ["D1184 A","Kraton SBS","Conventional modification"],
     ["D0243 E","Kraton SBS","PMB blends"]],
    ["Expressways and national highways","Airport runways","Bridge decks and intersections","HiMA high-performance overlays"])

product_page("special-products.html","Special Products",
    "Rejuvenators, anti-stripping agents, warmix additives, SBR latex and cellulose fibre.",
    "A suite of specialised additives that improve durability, recyclability and workability of bituminous mixes &mdash; covering situations standard binders don't.",
    [["Bitufix RAS / Re-Pave","Rejuvenator","Asphalt recycling (RAP)"],
     ["Bitufix LAS 90","Anti-stripping agent","All aggregate types"],
     ["Bitufix WMA","Warmix additive","Lower-energy paving"],
     ["SBR Latex","Microsurfacing latex","Slurry / microsurfacing"],
     ["Cellulose Fibre","SMA additive","Stone Matrix Asphalt"]],
    ["Asphalt recycling and rejuvenation (RAP)","Anti-stripping for moisture resistance","Warm-mix asphalt for lower emissions","Stone Matrix Asphalt (SMA)"])

product_page("roadbond.html","Re-Active Pothole Repair",
    "BG Re-Active ready-to-use asphalt for quick, durable, all-weather pothole repair.",
    "A premixed, ready-to-use Re-Active asphalt for fast pothole repair on flexible and rigid pavements &mdash; usable in all weather, with no heating required.",
    [["BG Re-Active","Ready-to-use asphalt","General pothole repair"],
     ["All-weather","Cold-applied patch","Wet / monsoon conditions"]],
    ["Pothole and edge repair","Utility-cut reinstatement","Emergency and monsoon maintenance"])

# ---------------- SERVICES ----------------
add_inner("services.html","Services",
    "Microsurfacing, cold-mix design, material testing and technical consultancy.","Services",
    """
<section class="section"><div class="wrap">
  <div class="split anchor" id="Microsurfacing">
    <div class="reveal prose"><span class="eyebrow">Service</span><h2 class="mt0">Microsurfacing</h2>
      <p>A polymer-modified emulsion treatment that restores road surfaces by sealing cracks, improving skid resistance and ride quality. We have completed over 7 lakh sq.m of NH &amp; SH microsurfacing with premier customers in 2023&ndash;24.</p>
      <p>Versus traditional resurfacing it cuts life-cycle cost 25&ndash;45%, lowers greenhouse gases by 44% and energy use by 54%, reduces raw material use by 35%, returns traffic within an hour, and adds 6&ndash;8 years of service life.</p></div>
    <div class="figbox reveal">microsurfacing image</div>
  </div>
  <div class="split anchor" id="Coldmix" style="margin-top:64px">
    <div class="figbox reveal">cold-mix image</div>
    <div class="reveal prose"><span class="eyebrow">Service</span><h2 class="mt0">Cold-mix design</h2>
      <p>Custom cold-mix asphalt &mdash; aggregate, binder and additives produced and applied at ambient temperature, with no heating or drying. Ideal for remote sites and maintenance.</p></div>
  </div>
  <div class="split anchor" id="Material-Testing" style="margin-top:64px">
    <div class="reveal prose"><span class="eyebrow">Service</span><h2 class="mt0">Material testing</h2>
      <p>Independent testing of construction materials for quality and compliance &mdash; critical for the safety, durability and sustainability of roads and infrastructure.</p></div>
    <div class="figbox reveal">lab image</div>
  </div>
  <div class="split anchor" id="Technical-Consultancy" style="margin-top:64px">
    <div class="figbox reveal">consultancy image</div>
    <div class="reveal prose"><span class="eyebrow">Service</span><h2 class="mt0">Technical consultancy</h2>
      <p>Technical support, product research and advanced solutions for road construction &mdash; helping customers improve operations with practical, proven approaches.</p></div>
  </div>
</div></section>""")

# ---------------- PARTNERING CUSTOMER ----------------
add_inner("partnering-customer.html","Partnering Customer",
    "Partner with AVK Blackgold for reliable supply, technical support and joint growth.","Partnering Customer",
    """
<section class="section"><div class="wrap split">
  <div class="reveal prose"><span class="eyebrow">Work With Us</span><h2 class="mt0">Become a partner</h2>
    <p class="lead">We work with contractors, distributors and agencies to deliver dependable bituminous products and on-ground technical support. Tell us about your requirement and our team will get in touch.</p>
    <ul><li>Reliable, on-time supply</li><li>Technical and application support</li><li>Products to BIS / ASTM standards</li></ul></div>
  <div class="reveal">
    <form data-form data-subject="Partnership Enquiry">
      <div class="field"><label>Name <span class="req">*</span></label><input name="name" required><span class="err">Required</span></div>
      <div class="field"><label>Company <span class="req">*</span></label><input name="company" required><span class="err">Required</span></div>
      <div class="field"><label>Email <span class="req">*</span></label><input type="email" name="email" required><span class="err">Valid email required</span></div>
      <div class="field"><label>Phone <span class="req">*</span></label><input name="phone" required><span class="err">Required</span></div>
      <div class="field"><label>How would you like to partner?</label><textarea name="message"></textarea></div>
      <label class="consent"><input type="checkbox" name="consent" required><span>I consent to being contacted about my enquiry. <span class="req">*</span></span></label>
      <button class="btn btn--primary btn--lg" type="submit">Send enquiry <span class="arr">&rarr;</span></button>
      <div class="form-status" role="status"></div>
    </form>
  </div>
</div></section>""")

# ---------------- JOIN US ----------------
add_inner("join-us.html","Join Us",
    "Build your career with AVK Blackgold Infra. See open roles and apply.","Join Us",
    """
<section class="section"><div class="wrap split">
  <div class="reveal prose"><span class="eyebrow">Careers</span><h2 class="mt0">Grow with us</h2>
    <p class="lead">We're a team of engineers, chemists and operators building better roads. If that sounds like you, we'd like to hear from you.</p>
    <p>See current openings on our <a href="jobs.html">Jobs</a> page, or send your details below and we'll keep you in mind.</p></div>
  <div class="reveal">
    <form data-form data-subject="Job Application">
      <div class="field"><label>Full name <span class="req">*</span></label><input name="name" required><span class="err">Required</span></div>
      <div class="field"><label>Email <span class="req">*</span></label><input type="email" name="email" required><span class="err">Valid email required</span></div>
      <div class="field"><label>Phone <span class="req">*</span></label><input name="phone" required><span class="err">Required</span></div>
      <div class="field"><label>Role of interest</label><input name="role"></div>
      <div class="field"><label>Message</label><textarea name="message"></textarea></div>
      <p class="form-note">Resume upload needs a backend or a Web3Forms paid plan &mdash; for now, email your CV to the address in the footer.</p>
      <label class="consent"><input type="checkbox" name="consent" required><span>I consent to my details being stored for recruitment. <span class="req">*</span></span></label>
      <button class="btn btn--primary btn--lg" type="submit">Apply <span class="arr">&rarr;</span></button>
      <div class="form-status" role="status"></div>
    </form>
  </div>
</div></section>""")

# ---------------- CONTACT ----------------
add_inner("contact-us.html","Contact Us",
    "Get in touch with AVK Blackgold Infra for products, services and support.","Contact Us",
    """
<section class="section"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Get In Touch</span><h2 class="h-sec mt0" style="margin-bottom:1.2rem">Send us a message</h2>
    <form data-form data-subject="Contact Form">
      <div class="form-grid">
        <div class="field"><label>Name <span class="req">*</span></label><input name="name" required><span class="err">Required</span></div>
        <div class="field"><label>Company</label><input name="company"></div>
        <div class="field"><label>Email <span class="req">*</span></label><input type="email" name="email" required><span class="err">Valid email required</span></div>
        <div class="field"><label>Phone <span class="req">*</span></label><input name="phone" required><span class="err">Required</span></div>
      </div>
      <div class="field"><label>Subject</label><input name="topic"></div>
      <div class="field"><label>Message <span class="req">*</span></label><textarea name="message" required></textarea><span class="err">Required</span></div>
      <label class="consent"><input type="checkbox" name="consent" required><span>I consent to being contacted about my enquiry. <span class="req">*</span></span></label>
      <button class="btn btn--primary btn--lg" type="submit">Send message <span class="arr">&rarr;</span></button>
      <div class="form-status" role="status"></div>
    </form>
  </div>
  <div class="reveal prose">
    <h3>Registered Office</h3>
    <p>AVK Blackgold Infra Private Limited<br>714, Rajhans Montessa, Beside Le Meridien Hotel,<br>Magdalla, Surat &ndash; 395 007, Gujarat, India</p>
    <h3>Reach us</h3>
    <p>Email: <a href="mailto:info@blackgoldinfra.com">info@blackgoldinfra.com</a><br>Phone: <a href="tel:+919033090399">+91 90330 90399</a> / <a href="tel:+918828599845">+91 88285 99845</a></p>
    <h3>Hours</h3><p>Mon&ndash;Sat, 9:30 am &ndash; 6:00 pm</p>
    <div class="mapbox" style="aspect-ratio:16/9;margin-top:16px"><iframe title="AVK Blackgold Infra, Magdalla, Surat" src="https://www.google.com/maps?q=Rajhans%20Montessa%2C%20Magdalla%2C%20Surat%20395007&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</div></section>""")

# ---------------- JOBS ----------------
add_inner("jobs.html","Jobs",
    "Current openings at AVK Blackgold Infra.","Jobs",
    """
<section class="section"><div class="wrap reveal">
  <div class="sec-head"><span class="eyebrow">Open Positions</span><h2 class="h-sec">Current openings</h2>
    <p class="lead">EDIT this table as roles open and close.</p></div>
  <table class="spectable"><caption>Open roles</caption>
    <thead><tr><th>Role</th><th>Location</th><th>Type</th><th>Apply</th></tr></thead>
    <tbody>
      <tr><td>Production Engineer</td><td>Plant — City</td><td>Full-time</td><td><a class="card__link" href="join-us.html">Apply &rarr;</a></td></tr>
      <tr><td>Lab Chemist</td><td>R&amp;D Centre</td><td>Full-time</td><td><a class="card__link" href="join-us.html">Apply &rarr;</a></td></tr>
      <tr><td>Sales Manager</td><td>Regional</td><td>Full-time</td><td><a class="card__link" href="join-us.html">Apply &rarr;</a></td></tr>
    </tbody></table>
</div></section>""")

# ---------------- TENDERS ----------------
add_inner("tenders.html","Tenders",
    "Active tenders and procurement notices from AVK Blackgold Infra.","Tenders",
    """
<section class="section"><div class="wrap reveal">
  <div class="sec-head"><span class="eyebrow">Procurement</span><h2 class="h-sec">Active tenders</h2>
    <p class="lead">EDIT this table to publish tender notices and link documents.</p></div>
  <table class="spectable"><caption>Tender notices</caption>
    <thead><tr><th>Ref</th><th>Title</th><th>Published</th><th>Closes</th><th>Document</th></tr></thead>
    <tbody>
      <tr><td>T-001</td><td>Supply of raw materials</td><td>&mdash;</td><td>&mdash;</td><td><a class="card__link" href="#">PDF &rarr;</a></td></tr>
      <tr><td>T-002</td><td>Logistics &amp; transport</td><td>&mdash;</td><td>&mdash;</td><td><a class="card__link" href="#">PDF &rarr;</a></td></tr>
    </tbody></table>
  <p class="form-note">No active tenders? Replace rows with an empty-state message.</p>
</div></section>""")

# ---------------- BLOGS ----------------
add_inner("blogs.html","Blogs",
    "Knowledge @ AVK — articles on bitumen, road construction and maintenance.","Blogs",
    """
<section class="section"><div class="wrap">
  <div class="grid cols-3">
    %s%s%s
  </div>
</div></section>""" % (
    card("Article","Understanding RS1 grade emulsion","What RS1 bitumen emulsion is and where it fits in road construction.","blog-rs1-grade.html","Read more"),
    card("Article","Where does bitumen come from?","The story behind this ancient material and how it reaches the road.","blog-where-bitumen.html","Read more"),
    card("Article","How bitumen is made","The refinery process that produces bitumen, explained simply.","blog-how-bitumen-made.html","Read more"),
))

# ---------------- BLOG POSTS ----------------
def blog_post(fname, title, desc, paras):
    body = phero(title, desc, "Blogs / Article") + """
<section class="section"><div class="wrap" style="max-width:74ch;margin-inline:auto">
  <p class="muted reveal" style="font-family:var(--ff-mono);font-size:.8rem">By AVK Blackgold &middot; 12 June 2026</p>
  <div class="figbox reveal" style="aspect-ratio:16/9;margin:18px 0"><img src="%s" alt="%s"></div>
  <div class="prose reveal">
  %s
  <p class="mt2"><a class="btn btn--ghost" href="blogs.html">&larr; All articles</a></p>
  </div>
</div></section>""" % (genimg(title, 1024, 576), title, "".join("<p>%s</p>" % p for p in paras))
    PAGES[fname] = dict(title=title + " | AVK Blackgold Infra", desc=desc, body=body)

blog_post("blog-rs1-grade.html","Understanding RS1 grade emulsion for road construction",
    "An introduction to RS1 bitumen emulsion and its role in road work.",
    [
     "RS1 is a rapid-setting bitumen emulsion widely used in surface dressing and as a tack coat between pavement layers. The paragraphs below are placeholder lorem ipsum text — replace with your own article.",
     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
     "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.",
     "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris."])
blog_post("blog-where-bitumen.html","Where does bitumen come from?",
    "The origins of bitumen and how it reaches the modern road.",
    [
     "Bitumen is a thick, dark, sticky material that binds roads together and keeps them waterproof. The paragraphs below are placeholder lorem ipsum text — replace with your own article.",
     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
     "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.",
     "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit."])
blog_post("blog-how-bitumen-made.html","How bitumen is made: the refinery process",
    "A simple explanation of how bitumen is produced at the refinery.",
    [
     "Bitumen is the heavy residue left after lighter fractions are distilled from crude oil. The paragraphs below are placeholder lorem ipsum text — replace with your own article.",
     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
     "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit.",
     "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis."])

# ---------------- PRIVACY ----------------
add_inner("privacy-policy.html","Privacy Policy",
    "How AVK Blackgold Infra collects, uses and protects your information.","Privacy Policy",
    """
<section class="section"><div class="wrap prose reveal" style="max-width:74ch">
  <p class="muted">Last updated: EDIT date. This is placeholder text &mdash; replace with a policy reviewed by your legal team.</p>
  <h2>Information we collect</h2><p>We collect information you provide through our forms, such as name, company, email and phone, to respond to your enquiries.</p>
  <h2>How we use it</h2><p>We use your information solely to process your request and to contact you about our products and services.</p>
  <h2>Storage &amp; security</h2><p>We take reasonable measures to protect your data and retain it only as long as needed.</p>
  <h2>Cookies</h2><p>EDIT: describe any cookies or analytics your site uses.</p>
  <h2>Your rights</h2><p>You may request access to, correction of, or deletion of your personal data by contacting us.</p>
  <h2>Contact</h2><p>Questions about this policy: <a href="mailto:corporate@avkblackgold.in">corporate@avkblackgold.in</a></p>
</div></section>""")

# ============================================================
#  WRITE FILES
# ============================================================
# ============================================================
#  WRITE FILES
# ============================================================
genimg("hero visual", 1600, 900, slug="hero")  # hero background
genimg("location map", 800, 800, slug="map")   # footer map placeholder

# dummy leadership team
_team = [("Rajesh Kumar","Managing Director"),("Anita Desai","Director, Operations"),
         ("Vikram Shah","Head of R&D"),("Priya Menon","Head of Quality")]
TEAM_HTML = "".join(
    '<article class="card"><div class="card__img" data-tag="Team"><img src="%s" alt="%s"></div>'
    '<div class="card__body"><h3 style="font-size:1.1rem">%s</h3>'
    '<p style="font-family:var(--ff-mono);font-size:.75rem;color:var(--amber);margin:0">%s</p>'
    '<p>%s</p></div></article>' % (portrait(n), n, n, r, _L3[:90] + "…")
    for n, r in _team)

# turn any text-only .figbox into an on-theme dummy image
_figbox_re = _re.compile(r'<div class="figbox([^"]*)"([^>]*)>([^<]+)</div>')
def _figbox_sub(m):
    classes, attrs, label = m.group(1), m.group(2), m.group(3).strip()
    label = _re.sub(r"&mdash;.*$", "", label).strip() or "image"
    return '<div class="figbox%s"%s><img src="%s" alt="%s"></div>' % (
        classes, attrs, genimg(label), label)

count = 0
for fname, p in PAGES.items():
    html = shell(fname, p["title"], p["desc"], p["body"])
    html = html.replace("__TEAM__", TEAM_HTML)
    html = _figbox_re.sub(_figbox_sub, html)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
        fh.write(html)
    count += 1
print("Generated %d pages and %d images." % (count, len(_imgcache)))
for f in sorted(PAGES): print("  -", f)
