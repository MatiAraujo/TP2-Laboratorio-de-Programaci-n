from datetime import datetime
from collections import defaultdict
from Articulo import *

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
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        articulos_por_autor = defaultdict(list)
        for articulo in self.articulos:
            articulos_por_autor[articulo.autor].append(articulo)

        #crear indices
        indice_autores = "<div class='indice'><h2>Autores</h2><ul>\n"
        for autor in articulos_por_autor:
            id_autor = autor.lower().replace(" ", "-")
            indice_autores += f'<li><a href="autor-{id_autor}.html">{autor}</a></li>\n'
        indice_autores += "</ul></div>\n"

       

        for autor, articulos in articulos_por_autor.items():
            id_autor = autor.lower().replace(" ", "-")
            
            # Generar el HTML para cada autor
            contenido_autor = f"""
            <div class="autor" id="{id_autor}">
            <h1>Artículos de {autor}</h1>    
            """
            for articulo in articulos:
                nombre_archivo = articulo.generar_html_individual()
                contenido_autor += f"""
                <div class="articulo">
                    <h2><a href="{nombre_archivo}">{articulo.titulo}</a></h2>
                </div>
                """
            contenido_autor += "</div>\n"
            
            with open(f"autor-{id_autor}.html", 'w', encoding='utf-8') as f:
                f.write(f"""<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Artículos de {autor}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                background-image: url(fondo.jpg);
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            a {{
                display: inline-block;
                color: white;
            }}

            .articulo {{
                background-color: #00a5e5;
                color: white;
                border-radius: 8px;
                padding: 5px;
                margin-top: 5px;
                font-size: 0.9em;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .articulo h2 {{
                color: #ffffff;
            }}
            .articulo h4 {{
                color: #d9f3ff;
                font-weight: normal;
                font-size: 0.95em;
            }}
            .articulo p {{
                color: #f0f8ff;
                margin: 0;
                line-height: 1.4;
            }}
            .autor h3 {{
                margin-top: 0px;
                margin-bottom: 5px;
            }}
            .autor {{
                margin-top: 30px;
                background-color: rgba(247,120,56,1);
                border-radius: 8px;
                padding: 16px 12px;
            }}

        </style>
    </head>
    <body>
        <a href="index.html">← Volver al inicio</a>
        
        {contenido_autor}
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
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                background-image: url(fondo.jpg);
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            header, footer {{
                background-color: rgba(247,120,56,1);
                color: white;
                padding: 15px;
                text-align: center;
            }}
            .articulo {{
                background-color: #00a5e5;
                color: white;
                border-radius: 8px;
                padding: 5px;
                margin-top: 5px;
                font-size: 0.9em;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            footer{{
                margin-top: 30px;
            }}
            
            .articulo h2 {{
                color: #ffffff;
            }}
            .articulo h4 {{
                color: #d9f3ff;
                font-weight: normal;
                font-size: 0.95em;
            }}
            .articulo p {{
                color: #f0f8ff;
                margin: 0;
                line-height: 1.4;
            }}
            .autor h3 {{
                margin-top: 0px;
                margin-bottom: 5px;
            }}
            .autor {{
                margin-top: 30px;
                background-color: rgba(247,120,56,1);
                border-radius: 8px;
                padding: 16px 12px;
            }}
            a {{
                color: #007BFF;
                text-decoration: none;
            }}
            a:visited {{
                color: #007BFF;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            a:active {{
                color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <header><h1>Noticias del día</h1></header>
        {indice_autores}
    </body>
    <footer><p>Fecha de creación: {fecha} </p></footer>
    </html>
    """

        
        with open(archivo_html, 'w', encoding='utf-8') as f:
            f.write(html_completo)

articulos = [
    ("Pronóstico del tiempo", "pablo pérez", "Hoy estará parcialmente soleado, y pueden haber chubascos por la tarde."),
    ("Nueva apertura cultural en la ciudad", "Carla Suárez", "El teatro municipal reabre sus puertas con una muestra gratuita para todo público."),
    ("Tecnología al alcance de todos", "Martín Díaz", "Una startup local desarrolló una app que traduce lenguaje de señas en tiempo real."),
    ("Suben los precios de los alimentos", "Carla Suárez", "El índice de inflación marcó un aumento del 5% en productos de la canasta básica."),
    ("Deportes, el equipo local sigue invicto", "Ian Colombo", "Con un gol en el último minuto, el equipo se mantiene primero en la tabla."),
    
]

nuevo = ParserHtml(articulos)
nuevo.generar_html()
