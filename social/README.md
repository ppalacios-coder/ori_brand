# Redes sociales: perfiles, portadas y destacadas

Material para vestir las páginas de ORI en Facebook, Instagram y WhatsApp Business. No incluye publicaciones. Generado el 2026-10-05T22:27Z desde el sistema de diseño Ori, cuya fuente de verdad es el manual de marca.

## Contenido

| Carpeta | Pieza | Archivos |
| --- | --- | --- |
| `perfil/` | Foto de perfil 1080 × 1080 para Facebook, Instagram y WhatsApp Business | `ori-perfil-rosa-1080` (principal), `ori-perfil-oscuro-1080`, `ori-perfil-gris-1080` |
| `facebook/` | Portada de Facebook | `ori-fb-portada-gris-1702x630` (principal), `ori-fb-portada-oscuro-1702x630`; cada una también a 851 × 315 |
| `instagram/destacadas/` | 12 portadas de historias destacadas, 1080 × 1920 | `ori-ig-destacada-01-hogar-1080x1920` a `12-confianza` |
| `src/` | Script y fuentes para regenerar todo | `build.py`, `assets/` |

Cada pieza existe en `.png` (para subir) y `.svg` (editable; el texto va en curvas, no necesita la tipografía).

## Reglas de diseño aplicadas

- Minimalista: un logo o un icono por pieza, sin fotografía, sin patrones.
- Perfil: monograma "O" a la proporción del manual para el logo circular (37.2 % del diámetro). La plataforma recorta en círculo; el monograma queda dentro del círculo con margen.
- Portada: wordmark y eslogan "Excelencia en cada servicio" centrados. En móvil Facebook recorta los costados, así que todo está dentro del 66 % central. La esquina inferior izquierda queda libre para el perfil.
- Destacadas: icono de la biblioteca del sistema en `dark-ori` sobre `gris`, dentro del 40 % central del lienzo.
- Colores: `pink-ori` #EB4A5F, `gris` #EFEFE9, `dark-ori` #262323, blanco; el fondo oscuro es #1E1E1E, la tinta con que el manual dibuja el logo oscuro.
- Contraste: la portada gris usa wordmark `pink-ori` (marca, texto grande) y eslogan `dark-ori` (13.51:1). La portada oscura usa blanco sobre #1E1E1E (16.67:1). No hay texto blanco ni `pink-ori` pequeño sobre `pink-ori`.

## Medidas

Las medidas salen de guías de terceros, no de documentación oficial de Meta. Confírmalas en la plataforma al subir.

| Pieza | Medida usada | Nota |
| --- | --- | --- |
| Perfil Facebook, Instagram, WhatsApp Business | 1080 × 1080 | Se muestra en círculo. Instagram sube a 720 × 720; la plataforma reduce. No hay medida oficial verificada para Facebook ni WhatsApp |
| Portada Facebook | 1702 × 630 (doble densidad) y 851 × 315 | Se ve 820 × 312 en escritorio y 640 × 360 en móvil |
| Destacada Instagram | 1080 × 1920 | Zona segura: 40 % central |

## Destacadas: nombres propuestos

El listado de servicios de ORI es abierto (todo lo que un hogar pueda necesitar), así que el manual no asigna iconos a servicios. Los nombres de abajo son una propuesta inicial; el nombre de la destacada se escribe en Instagram, no en la imagen. Para cambiar un icono, edita `DEST` en `src/build.py` y vuelve a generar.

| # | Nombre propuesto | Icono |
| --- | --- | --- |
| 01 | Hogar | casa con sonrisa |
| 02 | Renovación | rodillo de pintura |
| 03 | Jardín | árbol |
| 04 | Cocina | gorro de chef |
| 05 | Cuidado | mano con corazón |
| 06 | Salud | persona con gorro de enfermería |
| 07 | Belleza | labial |
| 08 | Auto | auto de frente |
| 09 | Soporte | auricular con micrófono |
| 10 | Agenda | calendario con estrella |
| 11 | Equipo | persona con gorra y overol |
| 12 | Confianza | apretón de manos |

Los iconos sin destacada asignada (libro con gorro de chef, secador, tijeras, corazón) siguen disponibles en la biblioteca del sistema.

## Regenerar

```
pip install cairosvg fonttools brotli uharfbuzz
python3 social/src/build.py
```
