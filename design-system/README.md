Analytica LV's identity is two things: a graphite wordmark in wide-set geometric capitals, and a shield cut by the letter Λ with a red gem at its point. Everything here extends those two things and nothing else.

## Logo

- Use the files in `assets/Logos/` as they are. Never redraw, recolour, outline, stretch or rotate the mark, and never retype the wordmark in a font.
- `analytica-logo.svg` is the primary lockup (shield + wordmark + the raised LV). Use it wherever the name must be read: site header, document covers, email signatures.
- `analytica-icon.svg` is the shield alone. Use it where the name is already present or space is square: favicon, app icon, social avatar, slide corners.
- On `surface` and `surface-raised` in the light theme use the graphite files. On dark grounds (`surface` in the dark theme, `graphite`, photography) use the `-reversed` files, which keep the gem red and turn the rest white.
- Never place the logo on `red`, `red-deep` or `surface-tint`: the gem disappears.
- Clear space on every side is the width of the gem. Minimum height: 20px for the lockup, 16px for the icon.
- The crossbar-less Λ is the mark's signature. Do not use Λ for A in headings or body copy; it belongs to the logo.

## Colour

- The palette is graphite, white and one red. Pages are mostly `surface` and `ink`; `graphite` builds large blocks; red appears once per view as the point of emphasis, the way the gem sits in the shield.
- Body copy is `ink`. Secondary copy is `ink-muted`.
- `red` is for shapes, not words. For red text, links and the focus ring use `red-text`. For a filled button or badge use `red-deep` with `on-red`.
- Use the two reds together only as light and shade of one object (as in the gem). Do not use them as two separate categories.
- No gradients. No shadows. Separate surfaces with `border` or a step to `surface-raised`.
- There are no status colours yet. Do not use `red` to mean error until a status set is added, or every accent will read as a warning.

## Type

- Headings are Outfit at weight 500 (`display`, `h1`–`h3`): a geometric sans in the spirit of the wordmark. Sentence case.
- Running text is Source Sans 3 (`lead`, `body`, `small`).
- `eyebrow` is the one place for capitals: 12px, tracked 0.18em, in `ink-muted`. It echoes the wordmark's spacing. Do not track or capitalise anything else.
- Both families render Latvian diacritics (ā č ē ģ ī ķ ļ ņ š ū ž) correctly. Do not swap in Jost or Urbanist: their web fonts misplace the macron on ā ē ī ū.
- Both load from Google Fonts: `https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600&family=Source+Sans+3:wght@400;600&display=swap`.

## Shape and layout

- Corners are square (`radius-none`). Only controls take `radius-sm`.
- The brand angle is the slope of the Λ: about 26° off vertical (a run of 27 for a rise of 55). Use it for diagonal cuts on bands, image crops and dividers. Do not introduce other angles or curves.
- Space with the scale: `space-6` inside cards, `space-10` between blocks, `space-16` between sections. Keep a `space-4` gutter at phone width.
- Focus ring: 2px solid `red-text`, offset 2px.

## Not defined yet

Voice and tone, photography, iconography, status colours and components are not part of this system yet. Do not invent them; ask.
