from componentes import navbar_html, generar_footer

class Articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = autor.strip().title()
        self.texto = texto.strip()

    def to_html(self):
        if len(self.texto) > 300:
            texto_recortado = self.texto[:300] + '...'
        else:
            texto_recortado = self.texto
        return f"""
        <div class="articulo">
            
            <p>{texto_recortado}</p>
        </div>
        """
    
    def contiene_palabra(self, palabra):
        return palabra.lower() in self.texto.lower()
    
    def generar_html_individual(self):
        nombre_archivo = self.titulo.lower().replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u") + ".html"

        contenido = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{self.titulo}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../estilos.css">

    
</head>
<body class="body_articulo">
    {navbar_html}
    <div class="articulo_ind">
        <h1>{self.titulo}</h1>
        <h4>Por {self.autor}</h4>
        <p class="articulo_p">{self.texto}</p>
    </div>
    {generar_footer()}
</body>
</html>"""

        with open(f"Articulos/{nombre_archivo}", "w", encoding="utf-8") as f:
            f.write(contenido)

        return nombre_archivo  