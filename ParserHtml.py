from datetime import datetime
from collections import defaultdict
from Articulo import *
from componentes import *

class ParserHtml:
    def __init__(self, articulos):
        self.articulos = self.filtrar_articulos(articulos)

    def filtrar_articulos(self, articulos):
        return [
        Articulo(titulo, autor, texto)
        for titulo, autor, texto in articulos
        if titulo.strip() and autor.strip() and texto.strip()
    ]

    def filtrar_por_palabra(self, palabra_clave):
        filtrados = []
        for art in self.articulos:
            if art.contiene_palabra(palabra_clave):
                filtrados.append(art)
        return filtrados


    def generar_html(self, archivo_html='index.html'):
        

        articulos_por_autor = defaultdict(list)
        for articulo in self.articulos:
            articulos_por_autor[articulo.autor].append(articulo)

        #crear indices
        indice_autores = """<div class='indice'>
        <ul>
            <table class="tabla_autores" >
        <tr>
            <th>Autor</th>
            <th>Cantidad de artículos</th>
        </tr>
        """

        for autor in articulos_por_autor:
            id_autor = autor.lower().replace(" ", "-")
            cantidad = len(articulos_por_autor[autor])
            indice_autores += f"""
                <tr>
                    <td><a class= "enlace_autor" href="Articulos/autor-{id_autor}.html">{autor}</a></td>
                    <td>{cantidad}</td>
                </tr>
            """
        indice_autores += """
                </table>
            </div>"""

       

        for autor, articulos in articulos_por_autor.items():
            id_autor = autor.lower().replace(" ", "-")
            
            # Generar el HTML para cada autor
            contenido_autor = f"""
            <div class="autor" id="{id_autor}">
            <h1>Artículos de {autor}</h1>   
            <div class="row"> 
            """
            for articulo in articulos:
                nombre_archivo = articulo.generar_html_individual()
                contenido_autor += f"""
                <div class="col-md-4 mb-4">
                    <a href="{nombre_archivo}" class="text-decoration-none">
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">
                                    {articulo.titulo}
                                </h5>
                                {articulo.to_html()}
                            </div>
                        </div>
                    </a>
                </div>
                """
            contenido_autor += """
                </div>
            </div>\n"""
            
            with open(f"Articulos/autor-{id_autor}.html", 'w', encoding='utf-8') as f:
                f.write(f"""<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Artículos de {autor}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="../estilos.css">
        
    </head>
    <body>
        {navbar_html}
        
        {contenido_autor}
        {generar_footer()}
    </body>
    </html>
    """)

        #página principal
        # no importa style articulo y autor
        html_completo = f"""<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Noticias</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="estilos.css">
        
    </head>
    <body>
        {navbar_inicio(navbar_html)}

        <header><h1>Noticias del día</h1></header>
        {indice_autores}
    </body>
        {generar_footer()}
        
    </html>
    """

        
        with open(archivo_html, 'w', encoding='utf-8') as f:
            f.write(html_completo)


