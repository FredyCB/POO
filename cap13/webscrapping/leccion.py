from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejemplo de Beautiful Soup</title>
</head>
<body>
    <div id="contenedor-principal">
        <div class="seccion">
            <h2 class="titulo">Título de Sección 1</h2>
            <p class="descripcion">Este es el primer párrafo de la sección 1.</p>
            <a href="https://www.unah.edu.hn">Enlace de ejemplo</a>
            <div class="sub-seccion">
                <h3>Subsección 1.1</h3>
                <p>Este es un párrafo dentro de la subsección 1.1.</p>
                <div class="sub-sub-seccion">
                    <h4>Subsubsección 1.1.1</h4>
                    <p>Este es un párrafo dentro de la subsubsección 1.1.1.</p>
                    <a href="https://www.google.com">Otro enlace de ejemplo</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

# Acceder a la subsubsección (tercer nivel de anidación)
subsub_section = soup.find("div", class_="sub-sub-seccion")
print(subsub_section.h4.text)
print(
    subsub_section.p.text
)

print("Enlaces...")
a_list = soup.find_all("a")
for a in a_list:
    # Encontrar todos los enlaces en el documento
    print(a.get("href"))

contenedor = soup.find(id="contenedor-principal")
print("Contenedor principal:")
print(contenedor.text)
