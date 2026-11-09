"""Builds the "Cited G" icons from the 1a handoff spec (docs/brand/cvcite-1a-ink/README.md).

Glyphs are outlined from IBM Plex Sans, so no icon depends on a font being installed.
Run from the repo root:
  uv run --with fonttools --with resvg-py --with pillow python -I docs/brand/icons/build.py <dir with plex-500.ttf, plex-600.ttf, plex-700.ttf>
"""
import io, pathlib, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import resvg_py
from PIL import Image

INK, WHITE = "#17202E", "#FFFFFF"
fonts = pathlib.Path(sys.argv[1])
out = pathlib.Path(".")
here = pathlib.Path(__file__).parent

def fmt(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")

def glyph(weight, char, size):
    f = TTFont(fonts / f"plex-{weight}.ttf")
    gs = f.getGlyphSet(); g = gs[f.getBestCmap()[ord(char)]]
    return f, gs, g, size / f["head"].unitsPerEm

def css_box_glyph(weight, char, size, left, bottom_gap, canvas):
    """A glyph placed as CSS would: line-height 1 box, `left` and `bottom` offsets."""
    f, gs, g, s = glyph(weight, char, size)
    asc, desc = f["hhea"].ascent, f["hhea"].descent
    top = canvas - bottom_gap - size
    baseline = top + (size - (asc - desc) * s) / 2 + asc * s
    pen = SVGPathPen(gs, ntos=fmt); g.draw(TransformPen(pen, (s, 0, 0, -s, left, baseline)))
    return pen.getCommands()

def centred_glyph(weight, char, size, cx, cy):
    f, gs, g, s = glyph(weight, char, size)
    b = BoundsPen(gs); g.draw(b); x0, y0, x1, y1 = b.bounds
    dx = cx - (x0 + x1) / 2 * s; dy = cy + (y0 + y1) / 2 * s
    pen = SVGPathPen(gs, ntos=fmt); g.draw(TransformPen(pen, (s, 0, 0, -s, dx, dy)))
    return pen.getCommands()

def box(x, y, w, border, radius):
    i = border / 2  # border-box: stroke centred inside the outer edge
    return (f'<rect x="{fmt(x + i)}" y="{fmt(y + i)}" width="{fmt(w - border)}" height="{fmt(w - border)}" '
            f'rx="{fmt(radius)}" fill="none" stroke="{WHITE}" stroke-width="{fmt(border)}"/>')

def svg(n, *parts):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" width="{n}" height="{n}"><title>GovernedAI</title>'
            f'<rect width="{n}" height="{n}" fill="{INK}"/>' + "".join(parts) + "</svg>\n")

def path(d):
    return f'<path fill="{WHITE}" d="{d}"/>'

icons = {
    # 96 px master: G 500 58px, left 10 / bottom 6; box 24, 3px border, radius 3, top 10 / right 10, "1" 700 14px.
    96: svg(96, path(css_box_glyph(500, "G", 58, 10, 6, 96)), box(96 - 10 - 24, 10, 24, 3, 3),
            path(centred_glyph(700, "1", 14, 96 - 10 - 12, 10 + 12))),
    # 36 px: G 22px, left 4 / bottom 2; box 9, 1.5px border, radius 1, top 4 / right 4; no number.
    36: svg(36, path(css_box_glyph(500, "G", 22, 4, 2, 36)), box(36 - 4 - 9, 4, 9, 1.5, 1)),
    # 16 px, hand-tuned: G 600 10px, left 1 / bottom 0; box 5, 1px border, top 2 / right 2.
    16: svg(16, path(css_box_glyph(600, "G", 10, 1, 0, 16)), box(16 - 2 - 5, 2, 5, 1, 0)),
}
for n, s in icons.items():
    (here / f"icon-{n}.svg").write_text(s)
(out / "favicon.svg").write_text(icons[36])

def png(src, n):
    return bytes(resvg_py.svg_to_bytes(svg_string=src, width=n, height=n))

# Published at the site root: favicon.svg, favicon.ico, apple-touch-icon.png. The rest stay in docs.
renders = {out / "apple-touch-icon.png": (96, 180), here / "favicon-16.png": (16, 16),
           here / "favicon-32.png": (36, 32), here / "icon-512.png": (96, 512)}
for dest, (src, n) in renders.items():
    dest.write_bytes(png(icons[src], n))
ico16 = Image.open(io.BytesIO(png(icons[16], 16))); ico32 = Image.open(io.BytesIO(png(icons[36], 32)))
ico32.save(out / "favicon.ico", sizes=[(32, 32), (16, 16)], append_images=[ico16])
print("built", ", ".join(["favicon.svg", "favicon.ico", *(str(p) for p in renders)]))
