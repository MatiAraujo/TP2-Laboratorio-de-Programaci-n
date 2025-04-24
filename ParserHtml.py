from datetime import datetime
from collections import defaultdict

class ParserHtml:
    def __init__(self, articulos):
        self.articulos = self.filtrar_articulos(articulos)

    def filtrar_articulos(self, articulos):
        filtrados = []
        for titulo, autor, texto in articulos:
            if titulo.strip() and autor.strip() and texto.strip():
                normalizar = autor.strip().title()
                filtrados.append((titulo.strip(), normalizar, texto.strip()))
        return filtrados


    def generar_html(self, archivo_html='index.html'):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        articulos_por_autor = defaultdict(list)

        for titulo, autor, texto in self.articulos:
            articulos_por_autor[autor].append((titulo, texto))

        indice_autores = "<div class='indice'><h2>Autores</h2><ul>\n"
        for autor in articulos_por_autor:
            id_autor = autor.lower().replace(" ", "-")
            indice_autores += f'<li><a href="#{id_autor}">{autor}</a></li>\n'
        indice_autores += "</ul></div>\n"

        contenido_articulos = ""

        for autor, articulos in articulos_por_autor.items():
            id_autor = autor.lower().replace(" ", "-")
            contenido_articulos += f"""
            <div class="autor" id="{id_autor}">
                <h3>{autor}</h3>
            """

            for titulo, texto in articulos:
                contenido_articulos += f"""
                <div class="articulo">
                    <h2>{titulo}</h2>
                    <p>{texto}</p>
                </div>
                """
            contenido_articulos += "</div>\n"

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
        color: #007BFF; /* o el color que prefieras */
        text-decoration: none;
        }}

        a:visited {{
        color: #007BFF; /* mismo color que el estado normal */
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
    {contenido_articulos}
</body>
<footer><p>Fecha de creación: {fecha} </p></footer>
</html>
"""

        with open(archivo_html, 'w', encoding='utf-8') as f:
            f.write(html_completo)

articulos = [
    ("Pronóstico del tiempo", "pablo pérez", "Hoy estará parcialmente soleado, y pueden haber chubascos por la tarde."),
    ("Nueva apertura cultural en la ciudad", "Laura Fernández", "El teatro municipal reabre sus puertas con una muestra gratuita para todo público."),
    ("Tecnología al alcance de todos", "Martín Díaz", "Una startup local desarrolló una app que traduce lenguaje de señas en tiempo real."),
    ("Suben los precios de los alimentos", "Carla Suárez", "El índice de inflación marcó un aumento del 5% en productos de la canasta básica."),
    ("Deportes: el equipo local sigue invicto", "Ian Colombo", "Con un gol en el último minuto, el equipo se mantiene primero en la tabla."),
    ("Educación en tiempos digitales", "Mariana López", "El 70% de las escuelas ya incorporaron plataformas virtuales como complemento."),
    ("Recomendaciones para el cuidado del medio ambiente", "Camila Torres", "Separar los residuos y reducir el uso de plásticos puede marcar la diferencia."),
    ("Festival gastronómico en el parque", "Valentina Godoy", "Más de 30 puestos ofrecerán comidas típicas durante todo el fin de semana."),
    ("La música vuelve a los escenarios", "Javier Gómez", "Este viernes se realizará un recital gratuito en la plaza central con bandas locales."),
    ("Consejos para una vida saludable", "Camila Torres", "Dormir bien, hidratarse y caminar 30 minutos al día mejoran la salud general.")
]

nuevo = ParserHtml(articulos)
nuevo.generar_html()

