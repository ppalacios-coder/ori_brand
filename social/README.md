# Redes sociales: perfiles, portadas y destacadas

Material para vestir las páginas de ORI en Facebook, Instagram y WhatsApp Business. No incluye publicaciones. Generado el 2026-10-05T22:27Z desde el sistema de diseño Ori, cuya fuente de verdad es el manual de marca.

## Contenido

| Carpeta | Pieza | Archivos |
| --- | --- | --- |
| `perfil/` | Foto de perfil 1080 × 1080 para Facebook, Instagram y WhatsApp Business | `ori-perfil-rosa-1080` (principal), `ori-perfil-oscuro-1080`, `ori-perfil-gris-1080` |
| `facebook/` | Portada de Facebook | `ori-fb-portada-gris-1702x630` (principal), `ori-fb-portada-oscuro-1702x630`; cada una también a 851 × 315 |
| `instagram/destacadas/` | 8 portadas de historias destacadas, 1080 × 1920 | `ori-ig-destacada-01-hogar-1080x1920` a `08-clientes` |
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

## Destacadas

Aprobadas por Pepe el 2026-10-05T23:08Z. Siguen el eje del manual (cuidado, mantenimiento y renovación del hogar) más el recorrido del cliente. No afirman servicios que ORI no haya confirmado; el listado de servicios es abierto. El nombre de la destacada se escribe en Instagram, no en la imagen. Para cambiar un icono o agregar una destacada, edita `DEST` en `src/build.py` y vuelve a generar.

| # | Nombre | Icono | Contenido previsto |
| --- | --- | --- | --- |
| 01 | Hogar | casa con sonrisa | Quiénes somos |
| 02 | Cuidado | mano con corazón | Cuidado del hogar |
| 03 | Mantenimiento | persona con gorra y overol | Mantenimiento |
| 04 | Renovaciones | rodillo de pintura | Renovaciones |
| 05 | Agenda | calendario con estrella | Cómo solicitar un servicio |
| 06 | Contacto | auricular con micrófono | Atención al cliente |
| 07 | Confianza | apretón de manos | Garantías y proceso |
| 08 | Clientes | corazón | Testimonios |

Los demás iconos (enfermera, labial, auto, secador, gorro de chef, libro con gorro, tijeras, árbol) siguen en la biblioteca y se asignan solo con confirmación de ORI.

## Regenerar

```
pip install cairosvg fonttools brotli uharfbuzz
python3 social/src/build.py
```
