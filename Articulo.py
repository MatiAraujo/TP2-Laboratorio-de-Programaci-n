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
            <h2>{self.titulo}</h2>
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
            .articulo {{
                background-color: #00a5e5;
                color: white;
                border-radius: 8px;
                padding: 5px 5px;
                margin-top: 5px;
                font-size: 0.9em;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
             h1 {{
                color: #ffffff;
            }}
            h4 {{
                color: #d9f3ff;
                font-weight: normal;
                font-size: 0.95em;
            }}
            p {{
                color: #f0f8ff;
                margin: 0;
                line-height: 1.4;
            }}
        a {{
            display: inline-block;
            margin-bottom: 20px;
            color: #007BFF;
        }}
        .articulo_ind{{
                margin-top: 30px;
                background-color: rgba(247,120,56,1);
                border-radius: 8px;
                padding: 16px 12px;
        }}
        
        
    </style>
</head>
<body>
    <a href="index.html">← Volver al inicio</a>
    <div class="articulo_ind">
        <h1>{self.titulo}</h1>
        <h4>Por {self.autor}</h4>
        <p class="articulo">{self.texto}</p>
    </div>
</body>
</html>"""

        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(contenido)

        return nombre_archivo  