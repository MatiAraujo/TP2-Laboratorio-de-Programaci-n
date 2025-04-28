
from datetime import datetime


navbar_html = """<nav class="navbar navbar-expand-lg navbar-light bg-nav">
            <div class="container-fluid">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContenido" aria-controls="navbarContenido" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarContenido">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="../index.html">INICIO</a>
                    </li>
                    
                </ul>
                </div>
            </div>
        </nav>"""

def navbar_inicio(nav_html):    
    if "../index.html" in nav_html:
        nav_html = nav_html.replace("../index.html","index.html")
    return nav_html

def generar_footer():
    anio_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    pie_pagina = f"""<footer class="foot">
        <p>Noticias del día - Todos los derechos reservados.</p>
        <p>Creado {anio_actual}</p>
    </footer>"""
    return pie_pagina