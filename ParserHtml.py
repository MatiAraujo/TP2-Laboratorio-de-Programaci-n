from datetime import datetime

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
        contenido_articulos = ""

        for titulo, autor, texto in self.articulos:
            contenido_articulos += f"""
            <div class="articulo">
                <h2>{titulo}</h2>
                <h4>{autor}</h4>
                <p>{texto}</p>
            </div>
            """

        html_completo = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Noticias</title>
</head>
<body>
    <h1>Noticias del día</h1>
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
    ("Deportes: el equipo local sigue invicto", "Andrés Molina", "Con un gol en el último minuto, el equipo se mantiene primero en la tabla."),
    ("Educación en tiempos digitales", "Mariana López", "El 70% de las escuelas ya incorporaron plataformas virtuales como complemento."),
    ("Recomendaciones para el cuidado del medio ambiente", "Diego Rivas", "Separar los residuos y reducir el uso de plásticos puede marcar la diferencia."),
    ("Festival gastronómico en el parque", "Valentina Godoy", "Más de 30 puestos ofrecerán comidas típicas durante todo el fin de semana."),
    ("La música vuelve a los escenarios", "Javier Gómez", "Este viernes se realizará un recital gratuito en la plaza central con bandas locales."),
    ("Consejos para una vida saludable", "Camila Torres", "Dormir bien, hidratarse y caminar 30 minutos al día mejoran la salud general.")
]

nuevo = ParserHtml(articulos)
nuevo.generar_html()

