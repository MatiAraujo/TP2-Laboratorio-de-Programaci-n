from componentes import navbar_html, generar_footer
from excepciones import CaracteresInvalidosException

class Articulo:
    def __init__(self, titulo, autor, texto):
        if len(titulo) < 10:
            raise CaracteresInvalidosException("El título debe tener al menos 10 caracteres.")
        if len(texto) < 10:
            raise CaracteresInvalidosException("El texto debe tener al menos 10 caracteres.")
        self.titulo = titulo.strip()
        self.autor = autor.strip().title()
        self.texto = texto.strip()

    #mostrar texto recortado
    def to_html(self):
        if len(self.texto) > 300:
            texto_recortado = self.texto[:300] + '...'
        else:
            texto_recortado = self.texto
        return f"""
        <div class="articulo_recortado">
            
            <p>{texto_recortado}</p>
        </div>
        """
    
    def contiene_palabra(self, palabra):
        return palabra.lower() in self.texto.lower()
    
    def obtener_nombre_archivo(self):
        safe = (self.titulo
                  .lower()
                  .replace(" ", "_")
                  .replace("á","a").replace("é","e")
                  .replace("í","i").replace("ó","o")
                  .replace("ú","u"))
        return f"{safe}.html"
    
    #html para cada artículo
    def generar_html_individual(self,articulo_anterior=None, articulo_siguiente=None):
        nombre_archivo = self.titulo.lower().replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u") + ".html"
        self.nombre_archivo = nombre_archivo

        # Generar botones anterior y siguiente en los articulos si los hay
        navegacion = '<div class="navegacion-articulos">'
        navegacion += '<div class="navegacion-anterior"> '
        if articulo_anterior:
            navegacion += f'<a href="{articulo_anterior}.html" class="btn btn-primary m-2 anterior">&larr; Artículo anterior</a>'
        navegacion += '</div> '
        navegacion += '<div class="navegacion-siguiente"> '
        if articulo_siguiente:
            navegacion += f'<a href="{articulo_siguiente}.html" class="btn btn-primary m-2 siguiente">Artículo siguiente &rarr;</a>'
        navegacion += """
                </div>
            </div>"""
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

                {navegacion}

                {generar_footer()}
            </body>
            
            </html>"""

        with open(f"Articulos/{nombre_archivo}", "w", encoding="utf-8") as f:
            f.write(contenido)

        return nombre_archivo  