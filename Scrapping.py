import re
import csv
import html

def resolver_tarea_max(archivo_entrada, archivo_salida):
    with open(archivo_entrada, "r", encoding="utf-8") as f:
        buffer = f.read()

    regex_nombre = re.compile(
        r'id="product-info-section-title-([^\"]+)"[^>]*>(.*?)</a>',
        re.DOTALL,
    )

    productos_finales = []

    print("Procesando productos de Tiendas MAX...")

    for match in regex_nombre.finditer(buffer):
        producto_id = match.group(1).strip()
        nombre_producto = html.unescape(match.group(2).strip())

        regex_imagen = re.compile(
            rf'id="product-thumbnail-image-{re.escape(producto_id)}"[^>]*?src="(.*?)"',
            re.DOTALL,
        )
        match_imagen = regex_imagen.search(buffer)
        if match_imagen:
            url_imagen = match_imagen.group(1).strip()
            productos_finales.append([nombre_producto, url_imagen])

    # generacion del csv
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos_finales)

    print(f"Se exportaron {len(productos_finales)} productos a {archivo_salida}.")

nombre_archivo_subido = "Switch2_TiendaMax.html"
resolver_tarea_max(nombre_archivo_subido, "switch2_max.csv")