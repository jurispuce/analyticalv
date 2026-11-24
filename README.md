# analytica.lv

Static website for SIA Analytica. Latvian is served at `/`, English at `/en/`. Each language has the home page and four service pages.

## Layout

- `src/body.lv.html`, `src/body.html`: home page content (Latvian, English)
- `src/pages.py`: content of the four service pages in both languages
- `src/style.css`: all styling
- `assets/`: logo files
- `build.py`: builds every page, `sitemap.xml` and `robots.txt`
- `design-system/`: colour, type and spacing tokens and brand usage notes

The built pages are committed, so the repository can be served as it is.

## Editing

Change files under `src/`, then rebuild:

```bash
python3 build.py
```

The build also writes `preview/analytica-site.html`, a single-file preview that is not committed.

## Deploying

Netlify reads `netlify.toml` and publishes the repository root as it is, with no build step, so run `python3 build.py` and commit the built pages before pushing. The site address used for canonical links and the sitemap is set as `SITE` at the top of `build.py`.
