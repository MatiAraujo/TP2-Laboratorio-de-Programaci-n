from ParserHtml import ParserHtml


# Datos de prueba
articulos = [
    ("Pronóstico del tiempo", "Pablo Pérez", "Hoy estará parcialmente soleado, y pueden haber chubascos por la tarde."),
    ("Nueva apertura cultural en la ciudad", "Carla Suárez", "El teatro municipal reabre sus puertas con una muestra gratuita para todo público."),
    ("Tecnología al alcance de todos", "Martín Díaz", "Una startup local desarrolló una app que traduce lenguaje de señas en tiempo real."),
    ("Suben los precios de los alimentos", "Carla Suárez", "El índice de inflación marcó un aumento del 5% en productos de la canasta básica."),
    ("Deportes, el equipo local sigue invicto", "Ian Colombo", "Con un gol en el último minuto, el equipo se mantiene primero en la tabla."),
]

def main():
    parser = ParserHtml(articulos)
    parser.generar_html()

if __name__ == "__main__":
    main()