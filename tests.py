import unittest
from Articulo import Articulo
from ParserHtml import ParserHtml

class TestArticuloParser(unittest.TestCase):
    
    def test_articulo(self):
        articulo1 = Articulo("Título primer articulo", "Autor A", "Texto del artículo 1")
        articulo2 = Articulo("Título 2", "Autor B", "Texto del artículo 2")
        
        self.assertEqual(articulo1.titulo, "Título primer articulo", "Error en el título del artículo 1")
        self.assertEqual(articulo2.titulo, "Título 2", "Error en el título del artículo 2")
        
        self.assertEqual(articulo1.autor, "Autor A", "Error en el autor del artículo 1")
        self.assertEqual(articulo2.autor, "Autor B", "Error en el autor del artículo 2")
        
        self.assertEqual(articulo1.texto, "Texto del artículo 1", "Error en el texto del artículo 1")
        self.assertEqual(articulo2.texto, "Texto del artículo 2", "Error en el texto del artículo 2")
    
    def test_parser_html(self):
        articulos = [
            ("Título primero", "Autor A", "Texto del artículo 1"),
            ("Título segundo", "Autor B", "Texto del artículo 2"),
            ("Título tercero", "Autor A", "Texto del artículo 3")
        ]
        
        parser = ParserHtml(articulos)
        
        self.assertEqual(len(parser.articulos), 3, "Error en la cantidad de artículos filtrados")
        
        articulos_filtrados = parser.filtrar_por_palabra("artículo 1")
        self.assertEqual(len(articulos_filtrados), 1, "Error en el filtrado por palabra clave")
        self.assertEqual(articulos_filtrados[0].titulo, "Título primero", "Error en el filtrado por palabra clave")
        
        articulos_filtrados = parser.filtrar_por_palabra("artículo 2")
        self.assertEqual(len(articulos_filtrados), 1, "Error en el filtrado por palabra clave")
        self.assertEqual(articulos_filtrados[0].titulo, "Título segundo", "Error en el filtrado por palabra clave")

if __name__ == "__main__":
    unittest.main()
