from ParserHtml import ParserHtml

# Datos de prueba
articulos = [
    ("Pronóstico del tiempo", "Pablo Pérez", "Para este miércoles, el Servicio Meteorológico Nacional (SMN) prevé una jornada parcialmente nublada, con temperaturas que oscilarán entre los 17° y los 26°. A lo largo de la mañana, es posible que se registren chaparrones."),
    ("El Instituto de Cultura lanzó nuevos cursos de capacitación", "Carla Suárez", "El Instituto Cultural ofrece nuevas capacitaciones abiertas y gratuitas sobre industrias creativas. Se trata de talleres virtuales donde se trabajará en torno a lo audiovisual, el diseño, la fotografía, la gestión cultural y los videojuegos. La inscripción es gratuita, con cupos limitados. Está destinada a hacedores y trabajadores culturales que pretenden promover una mejora continua en los diferentes segmentos de su cadena de producción."),
    ("LG se hace con el control de Bear Robotics", "Martín Díaz", "LG Electronics se ha asegurado una participación mayoritaria del 51% en la 'startup' Bear Robotics, especializada en robots de servicio autónomos impulsados por IA, en línea con la estrategia de la compañía surcoreana de reforzar su presencia en el sector, un área de crecimiento clave para la empresa."),
    ("Suben los precios de los alimentos", "Carla Suárez", "El índice de inflación marcó un aumento del 5% en productos de la canasta básica durante el último mes, según el informe difundido por el Instituto Nacional de Estadísticas. Entre los rubros más afectados se encuentran los lácteos, las carnes y las frutas, que registraron subas de entre el 7% y el 10%. Especialistas advierten que el incremento responde a una combinación de factores, como la sequía prolongada, el aumento de los costos logísticos y las variaciones en el tipo de cambio. Además, se prevé que la tendencia alcista continúe en los próximos meses si no se implementan medidas de contención."),
    ("River fue superior a Boca y ganó el Superclásico en el Monumental", "Ian Colombo", "River hizo los deberes y puso la casa en orden. En el Monumental, el Millonario fue muy superior a Boca y se quedó con una victoria espectacular ante el máximo rival. Con los goles de Franco Mastantuono y Sebastián Driussi, los de Gallardo le dieron una inmensa alegría a la gente."),
    ("Llega a la Argentina la marca de zapatillas On","Ian Colombo","La marca suiza On —famosa por sus zapatillas de running con diseño minimalista y tecnología de alto rendimiento— ya tiene fecha de aterrizaje en la Argentina. El Grupo Bisa, uno de los principales jugadores del mercado deportivo local, cerró un acuerdo para traerla al país y ya tiene planes concretos: en 2026 abrirán los dos primeros locales exclusivos, uno en un shopping y otro a la calle."),
    ("Apagón masivo en España, Portugal y partes de Francia","Carla Suárez","""España sufre un histórico apagón eléctrico masivo que provocó el colapso de la infraestructura de transporte y las comunicaciones de millones de personas desde las 12.30 (hora local).
     Pasadas las 18, el presidente del gobierno, Pedro Sánchez, que había reunido el Consejo de Seguridad Nacional, hizo las primeras declaraciones oficiales sobre el apagón.

    “Los técnicos de red eléctrica están trabajando para determinar las causas”, dijo Sánchez, que dijo que el suministro se restituyó en algunas regiones.

    “Todavía no tenemos información concluyente” sobre la causas y “no descartamos ninguna hipótesis” agregó Sánchez, que no comentó específicamente sobre la versión de un posible ciberataque.
     """),
    ("El Vaticano anuncia que el cónclave para elegir al próximo papa será el 7 de mayo","Guillermo Fonsi","El cónclave comenzará el miércoles 7 de mayo, según decidieron este lunes los cardenales presentes en Roma —tanto los mayores como los menores de 80 años— durante la quinta Congregación General, anunció hoy el Vaticano. En un encuentro con periodistas, el director de la Sala de Prensa del Vaticano, Matteo Bruni, precisó que en la reunión participaron 190 cardenales, de los cuales “un centenar” son menores de 80 años y, por tanto, con derecho a voto."),
    ("Argentina organiza una protesta en Roma por los cambios para obtener la ciudadanía italiana","Pablo Pérez","""Neisy era vecina del barrio porteño de Núñez, estudiante de Ciencias Físicas en la UBA y daba clases particulares de matemática y física a estudiantes del secundario. “Me fui de la Argentina en busca de mejores oportunidades para mi desarrollo profesional y de un país que tuviera una mejor economía”, cuenta esta joven que tiene la ciudadanía italiana gracias a su padre.

    Hoy ella forma parte de un grupo de ítalo-descendientes autoconvocados en Italia y organiza marchas para quejarse por el nuevo decreto Ley.""")
    
]

def main():
    parser = ParserHtml(articulos)
    parser.generar_html()

if __name__ == "__main__":
    main()