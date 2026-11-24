#!/usr/bin/env python3
"""Builds the Netlify site (Latvian at /, English at /en/, four service pages per language)
and preview/analytica-site.html, one file holding every page as a switchable view."""
import re, json, pathlib, sys
root = pathlib.Path(__file__).parent
sys.path.insert(0, str(root/'src'))
from pages import PAGES, ORDER, UI, PRIVACY

SITE = 'https://analytica.lv'  # the domain the site will be served from; used for canonical links, sitemap and structured data
LANGS = ['lv', 'en']
css = (root/'src/style.css').read_text()
fonts = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600&family=Source+Sans+3:wght@400;600&display=swap">'

def inner(name, ink_class=True):
    s = (root/'assets'/name).read_text()
    m = re.search(r'<svg[^>]*viewBox="([^"]+)"[^>]*>(.*)</svg>', s, re.S)
    content = re.sub(r'<title>.*?</title>', '', m.group(2))
    if ink_class: content = content.replace('fill="#58595b"', 'class="logo-ink"')
    return m.group(1), content
vb, logo = inner('analytica-logo.svg')
_, icon_rev = inner('analytica-icon-reversed.svg', False)

HOME = {
 'lv': dict(title='ISO 27001 ieviešana, drošības auditi, MK 397 atbilstība | Analytica', locale='lv_LV',
   desc='Analytica kopš 2006. gada: drošības auditi, ISO 27001 ieviešana, MK 397 atbilstība un kiberdrošības pārvaldnieks kā pakalpojums. Iekļauta Aizsardzības ministrijas kiberdrošības auditoru sarakstā.'),
 'en': dict(title='Analytica | Security audits, ISO 27001 and cybersecurity compliance in Latvia', locale='en_GB',
   desc='Analytica is a Latvian cybersecurity firm, working since 2006: security audits, ISO 27001 implementation, compliance with Cabinet Regulation 397 and cybersecurity manager as a service.'),
}
SWITCH = {'lv': ('en', 'EN', 'In English'), 'en': ('lv', 'LV', 'Latviešu valodā')}

THANKS = {'lv': dict(path='/paldies/', title='Paldies | Analytica', h1='Paldies, ziņa ir saņemta.', p='Atbildēsim, cik drīz vien iespējams.', back='Uz sākumlapu'),
          'en': dict(path='/en/thank-you/', title='Thank you | Analytica', h1='Thank you, we have your message.', p='We will reply as soon as we can.', back='Back to the home page')}

def path(page, lang):
    if page == 'thanks': return THANKS[lang]['path']
    if page == 'privacy': return PRIVACY['path'][lang]
    return ('/' if lang == 'lv' else '/en/') if page == 'home' else PAGES[page]['path'][lang]

def home_body(lang):
    f = 'src/body.lv.html' if lang == 'lv' else 'src/body.html'
    return (root/f).read_text().replace('@@LOGO@@', f'<svg viewBox="{vb}" role="img" aria-label="Analytica LV">{logo}</svg>').replace('@@ICON_REVERSED@@', icon_rev)

def service_body(page, lang):
    """Header, contact block and footer are taken from the home page so they stay identical."""
    h = home_body(lang); c = PAGES[page][lang]; ui = UI[lang]
    header = h[:h.index('<main')]
    header = re.sub(r'href="#top"', 'href="@@P:home@@"', header)
    header = re.sub(r'href="#(services|expertise|experience|partners)"', r'href="@@P:home@@#\1"', header)
    tail = h[h.index('  <section class="contact"'):]
    li = lambda xs: '\n'.join(f'          <li>{x}</li>' for x in xs)
    st_title, numbered, st = c['steps']
    others = '\n'.join(f'        <li><a href="@@P:{k}@@">{PAGES[k][lang]["name"]}</a></li>' for k in ORDER if k != page)
    return header + f'''<main id="top">
  <section class="page-hero">
    <div class="wrap">
      <a class="back" href="@@P:home@@#services">← {ui['back']}</a>
      <p class="eyebrow">{ui['eyebrow']}</p>
      <h1>{c['h1']}</h1>
      <p class="lead">{c['lead']}</p>
      <div class="cta"><a class="btn btn-primary" href="#contact">{ui['cta']}</a></div>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="two">
        <div class="block"><h2>{c['who'][0]}</h2><ul class="plain">
{li(c['who'][1])}
        </ul></div>
        <div class="block"><h2>{c['get'][0]}</h2><ul class="plain">
{li(c['get'][1])}
        </ul></div>
      </div>
    </div>
  </section>
  <section class="section raised">
    <div class="wrap">
      <div class="section-head"><h2>{st_title}</h2></div>
      <ol class="steps{' numbered' if numbered else ''}">
''' + '\n'.join(f'        <li><h3>{t}</h3><p>{d}</p></li>' for t, d in st) + f'''
      </ol>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <p class="proof">{c['proof']}</p>
      <div class="section-head"><h2>{ui['faq']}</h2></div>
      <div class="faq">
''' + '\n'.join(f'        <div><h3>{q}</h3><p>{a}</p></div>' for q, a in c['faq']) + f'''
      </div>
      <div class="block"><h2>{ui['other']}</h2><ul class="others">
{others}
      </ul></div>
    </div>
  </section>
''' + tail

def thanks_body(lang):
    h = home_body(lang); t = THANKS[lang]
    header = h[:h.index('<main')]
    header = re.sub(r'href="#top"', 'href="@@P:home@@"', header)
    header = re.sub(r'href="#(services|expertise|experience|partners|contact)"', r'href="@@P:home@@#\1"', header)
    footer = h[h.index('<footer'):]
    return header + f'''<main id="top">
  <section class="thanks">
    <div class="wrap">
      <h1>{t['h1']}</h1>
      <p class="lead">{t['p']}</p>
      <a class="btn btn-quiet" href="@@P:home@@">{t['back']}</a>
    </div>
  </section>
</main>

''' + footer

def privacy_body(lang):
    h = home_body(lang); c = PRIVACY[lang]
    header = h[:h.index('<main')]
    header = re.sub(r'href="#top"', 'href="@@P:home@@"', header)
    header = re.sub(r'href="#(services|expertise|experience|partners|contact)"', r'href="@@P:home@@#\1"', header)
    footer = h[h.index('<footer'):]
    def block(b): return '<ul>' + ''.join(f'<li>{x}</li>' for x in b) + '</ul>' if isinstance(b, list) else f'<p>{b}</p>'
    secs = '\n'.join(f'        <section><h2>{t}</h2>' + ''.join(block(b) for b in bs) + '</section>' for t, bs in c['sections'])
    return header + f'''<main id="top">
  <section class="page-hero">
    <div class="wrap">
      <h1>{c['h1']}</h1>
      <p class="lead">{c['lead']}</p>
      <p class="updated">{c['updated']}</p>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="doc">
{secs}
      </div>
    </div>
  </section>
</main>

''' + footer

def body(page, lang): return home_body(lang) if page == 'home' else thanks_body(lang) if page == 'thanks' else privacy_body(lang) if page == 'privacy' else service_body(page, lang)
def meta(page, lang): return HOME[lang] if page == 'home' else dict(THANKS[lang], desc='') if page == 'thanks' else PRIVACY[lang] if page == 'privacy' else PAGES[page][lang]
strip = lambda s: re.sub(r'<[^>]+>', '', s)

def jsonld(page, lang):
    m = meta(page, lang)
    org = {"@type": "ProfessionalService", "@id": SITE + "/#organization", "name": "Analytica", "legalName": "SIA Analytica",
        "url": SITE + path('home', lang), "logo": SITE + "/assets/analytica-logo.svg", "foundingDate": "2006", "telephone": "+37167471283",
        "address": {"@type": "PostalAddress", "streetAddress": "Dzeņu iela 3", "addressLocality": "Sigulda", "postalCode": "LV-2150", "addressCountry": "LV"},
        "areaServed": [{"@type": "Country", "name": "Latvia"}, "Europe"],
        "knowsAbout": ["ISO/IEC 27001", "MK noteikumi Nr. 397", "Nacionālās kiberdrošības likums", "NIS 2", "DORA", "penetration testing"]}
    if page == 'home':
        org.update({"description": m['desc'], "inLanguage": lang, "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": PAGES[k][lang]['name'], "url": SITE + path(k, lang)}} for k in ORDER]}})
        graph = [org]
    elif page == 'privacy':
        graph = [org]
    else:
        graph = [org,
          {"@type": "Service", "name": m['name'], "description": m['desc'], "url": SITE + path(page, lang), "inLanguage": lang, "provider": {"@id": SITE + "/#organization"}, "areaServed": {"@type": "Country", "name": "Latvia"}},
          {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in m['faq']]}]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

MENU_JS = """<script>
/* Phone menu: close it after a link is chosen, on a tap outside, or on Escape. */
(function () {
  function closeAll(except) { document.querySelectorAll('details.menu[open]').forEach(function (d) { if (d !== except) d.open = false; }); }
  document.addEventListener('click', function (e) {
    var inside = e.target.closest('details.menu');
    if (inside && e.target.closest('.menu-panel a')) inside.open = false;
    closeAll(inside);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
})();
</script>
"""
ALL = ['home'] + ORDER + ['privacy']
LINK = re.compile(r'(href|action)="@@P:(\w+)@@(?:#(\w+))?"')

# --- Netlify pages ---
for page in ALL + ['thanks']:
    for lang in LANGS:
        m = meta(page, lang); other, label, aria = SWITCH[lang]
        b = body(page, lang).replace('@@LANG@@', f'<a class="lang" href="{path(page, other)}" lang="{other}" hreflang="{other}" aria-label="{aria}">{label}</a>')
        b = LINK.sub(lambda x: f'{x.group(1)}="{path(x.group(2), lang)}{"#" + x.group(3) if x.group(3) else ""}"', b)
        if page == 'thanks': head_extra = '<meta name="robots" content="noindex">'
        else: head_extra = f'<script type="application/ld+json">{jsonld(page, lang)}</script>'
        out = root/path(page, lang).strip('/')/'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{m['title']}</title>
<meta name="description" content="{m['desc']}">
<link rel="canonical" href="{SITE}{path(page, lang)}">
<link rel="alternate" hreflang="lv" href="{SITE}{path(page, 'lv')}">
<link rel="alternate" hreflang="en" href="{SITE}{path(page, 'en')}">
<link rel="alternate" hreflang="x-default" href="{SITE}{path(page, 'lv')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Analytica">
<meta property="og:title" content="{m['title']}">
<meta property="og:description" content="{m['desc']}">
<meta property="og:url" content="{SITE}{path(page, lang)}">
<meta property="og:locale" content="{HOME[lang]['locale']}">
{head_extra}
<link rel="icon" type="image/svg+xml" href="/assets/analytica-icon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<style>
{css}</style>
</head>
<body>
{b}{MENU_JS}</body>
</html>
''')

(root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /preview/\nDisallow: /src/\n\nSitemap: {SITE}/sitemap.xml\n')
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + ''.join(f'<url><loc>{SITE}{path(p, l)}</loc>' + ''.join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{SITE}{path(p, a)}"/>' for a in LANGS) + '</url>\n' for p in ALL for l in LANGS) + '</urlset>\n')

# --- Preview: every page as a view in one file, switched in place ---
def aid(view, name): return name if view == 'lv-home' else f'{view}-{name}'
views = []
for lang in LANGS:
    for page in ALL:
        view = f'{lang}-{page}'; other, label, aria = SWITCH[lang]
        b = body(page, lang).replace('@@LANG@@', f'<a class="lang" href="#" data-go="{other}-{page}" aria-label="{aria}">{label}</a>')
        if view != 'lv-home':
            b = re.sub(r'id="([a-z]+)"', lambda x: f'id="{view}-{x.group(1)}"', b)
            b = re.sub(r'href="#([a-z]+)"', lambda x: f'href="#{view}-{x.group(1)}"', b)
        def go(x):
            if x.group(1) == 'action': return 'action="#"'
            t = f'{lang}-{x.group(2)}'
            return f'href="#" data-go="{t}"' + (f' data-anchor="{aid(t, x.group(3))}"' if x.group(3) else '')
        b = LINK.sub(go, b)
        views.append(f'<div data-view="{view}" lang="{lang}"{"" if view == "lv-home" else " hidden"}>\n{b}</div>\n')
(root/'preview').mkdir(exist_ok=True)
(root/'preview/analytica-site.html').write_text(f'''<title>Analytica Website Draft</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fonts}
<style>
{css}</style>
{''.join(views)}{MENU_JS}<script>
(function () {{
  function show(view, anchor) {{
    var found = false;
    document.querySelectorAll('[data-view]').forEach(function (el) {{ var on = el.dataset.view === view; el.hidden = !on; found = found || on; }});
    if (!found) return show('lv-home');
    try {{ localStorage.setItem('view', view); }} catch (e) {{}}
    var t = anchor && document.getElementById(anchor);
    if (t) t.scrollIntoView(); else window.scrollTo(0, 0);
  }}
  document.addEventListener('click', function (e) {{
    var a = e.target.closest('a[data-go]'); if (!a) return;
    e.preventDefault(); show(a.dataset.go, a.dataset.anchor);
  }});
  document.addEventListener('submit', function (e) {{
    var f = e.target.closest('form.contact-form'); if (!f) return;
    e.preventDefault(); var s = f.querySelector('.form-status'); s.textContent = f.dataset.previewNote; s.hidden = false;
  }});
  var saved = null; try {{ saved = localStorage.getItem('view'); }} catch (e) {{}}
  if (saved && saved !== 'lv-home') show(saved);
}})();
</script>
''')
print('built', len(ALL) * len(LANGS), 'pages')
