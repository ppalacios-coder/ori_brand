#!/usr/bin/env python3
"""Genera las piezas de redes de ORI (SVG con texto en curvas + PNG).

Uso: python3 social/src/build.py   (desde la raiz del repositorio)
Requiere: cairosvg, fonttools, brotli, uharfbuzz.
Todo color sale del manual de marca: ver social/README.md.
"""
import os, re, io, tempfile
import cairosvg
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)            # social/
A = os.path.join(HERE, 'assets')

# Colores del manual
PINK = '#EB4A5F'      # pink-ori
GRIS = '#EFEFE9'      # gris
DARK = '#262323'      # dark-ori (texto, iconos)
LOGO_DARK = '#1E1E1E' # tinta oscura del logo en las laminas del manual
WHITE = '#FFFFFF'

def paths(fn):
    return re.findall(r'<path d="([^"]+)"', open(os.path.join(A, 'logos', fn)).read())

WM = paths('Logo08-wordmark.svg')     # wordmark "Ori" (4 trazados)
MO = paths('Logo03-monograma.svg')    # monograma "O"
WM_BB = (75.0, 119.5, 363.0, 260.5)   # bbox del wordmark en su viewBox
MO_BB = (148.75, 122.0, 289.25, 258.0)

# Poppins Regular (woff2 -> ttf temporal) para convertir texto en curvas
_tmp = tempfile.mkdtemp()
_ttf = os.path.join(_tmp, 'Poppins-Regular.ttf')
_f = TTFont(os.path.join(A, 'fonts', 'Poppins-Regular.woff2')); _f.flavor = None; _f.save(_ttf)

def text_path(text, size):
    """Devuelve (d, ancho) del texto en Poppins Regular, con kerning, baseline en y=0."""
    face = hb.Face(hb.Blob.from_file_path(_ttf)); font = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {'kern': True, 'liga': True})
    tt = TTFont(_ttf); gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    s = size / tt['head'].unitsPerEm
    x = 0; ds = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = SVGPathPen(gs, ntos=lambda v: '%.2f' % v)
        gs[order[info.codepoint]].draw(TransformPen(pen, (s, 0, 0, -s, (x + pos.x_offset) * s, 0)))
        ds.append(pen.getCommands()); x += pos.x_advance
    return ' '.join(d for d in ds if d), x * s

def svg(w, h, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">%s</svg>\n'
            % (w, h, w, h, body))

def mark(ds, bb, width, cx, cy, fill):
    """Coloca un logo (lista de trazados) con ancho dado, centrado en (cx, cy)."""
    s = width / (bb[2] - bb[0])
    tx = cx - s * (bb[0] + bb[2]) / 2
    ty = cy - s * (bb[1] + bb[3]) / 2
    return ('<g fill="%s" transform="translate(%.3f %.3f) scale(%.5f)">%s</g>'
            % (fill, tx, ty, s, ''.join('<path d="%s"/>' % d for d in ds)))

def write(relpath, content, png_width=None):
    p = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p + '.svg', 'w').write(content)
    cairosvg.svg2png(bytestring=content.encode(), write_to=p + '.png',
                     output_width=png_width) if png_width else cairosvg.svg2png(
                     bytestring=content.encode(), write_to=p + '.png')
    print(relpath)

# 1) Foto de perfil 1080x1080 (Facebook, Instagram, WhatsApp Business).
#    Proporcion del manual (pag. 8): monograma = 37.2 % del diametro del circulo.
N = 1080
for name, bg, fg in [('rosa', PINK, WHITE), ('oscuro', LOGO_DARK, WHITE), ('gris', GRIS, PINK)]:
    body = '<rect width="%d" height="%d" fill="%s"/>' % (N, N, bg) + mark(MO, MO_BB, 0.372 * N, N / 2, N / 2, fg)
    write('perfil/ori-perfil-%s-1080' % name, svg(N, N, body))

# 2) Portada de Facebook. Subida recomendada 851x315; se entrega al doble (1702x630) y a 1x.
#    Composicion centrada: en movil se ve solo el tercio central ampliado (zona segura ~66 % del ancho).
W, H = 1702, 630
def cover(name, bg, wm_fill, tag_fill):
    wm_w = 440; sw = wm_w / (WM_BB[2] - WM_BB[0]); wm_h = sw * (WM_BB[3] - WM_BB[1])
    tag_size = 34; cap = 0.70 * tag_size; gap = 44
    top = (H - (wm_h + gap + cap)) / 2
    d, tw = text_path('Excelencia en cada servicio', tag_size)
    body = ('<rect width="%d" height="%d" fill="%s"/>' % (W, H, bg)
            + mark(WM, WM_BB, wm_w, W / 2, top + wm_h / 2, wm_fill)
            + '<path fill="%s" transform="translate(%.2f %.2f)" d="%s"/>' % (tag_fill, (W - tw) / 2, top + wm_h + gap + cap, d))
    s = svg(W, H, body)
    write('facebook/ori-fb-portada-%s-1702x630' % name, s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=os.path.join(ROOT, 'facebook/ori-fb-portada-%s-851x315.png' % name), output_width=851)
cover('gris', GRIS, PINK, DARK)
cover('oscuro', LOGO_DARK, WHITE, WHITE)

# 3) Portadas de destacadas de Instagram, 1080x1920. Icono de la biblioteca en dark-ori,
#    ~30 % del ancho, dentro del 40 % central.
ICON_DIR = os.path.join(A, 'iconos')
DEST = [  # (archivo-slug, nombre propuesto de la destacada, icono)
    ('hogar', 'Hogar', 'icono-01-casa-sonrisa'),
    ('renovacion', 'Renovación', 'icono-11-rodillo'),
    ('jardin', 'Jardín', 'icono-05-arbol'),
    ('cocina', 'Cocina', 'icono-04-gorro-chef'),
    ('cuidado', 'Cuidado', 'icono-03-mano-corazon'),
    ('salud', 'Salud', 'icono-09-enfermera'),
    ('belleza', 'Belleza', 'icono-12-labial'),
    ('auto', 'Auto', 'icono-10-auto'),
    ('soporte', 'Soporte', 'icono-07-auricular'),
    ('agenda', 'Agenda', 'icono-08-calendario-estrella'),
    ('equipo', 'Equipo', 'icono-13-operario'),
    ('confianza', 'Confianza', 'icono-15-apreton-manos'),
]
HW, HH = 1080, 1920
SC = 24  # 24 unidades -> 576 px (trazo visible ~384 px, dentro del 40 % central)
for i, (slug, label, icon) in enumerate(DEST, 1):
    d = re.search(r' d="([^"]+)"', open(os.path.join(ICON_DIR, icon + '.svg')).read()).group(1)
    body = ('<rect width="%d" height="%d" fill="%s"/>' % (HW, HH, GRIS)
            + '<path fill="%s" fill-rule="evenodd" transform="translate(%d %d) scale(%d)" d="%s"/>'
            % (DARK, HW / 2 - 12 * SC, HH / 2 - 12 * SC, SC, d))
    write('instagram/destacadas/ori-ig-destacada-%02d-%s-1080x1920' % (i, slug), svg(HW, HH, body))
