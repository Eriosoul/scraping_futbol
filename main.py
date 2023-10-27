# # Como hicimos tan buen trabajo en los ejercicios de autoevaluación a la hora de leer datos futbolísticos,
# # la LFP se ha fijado en nuestro equipo de desarrollo y nos ha pedido una serie de tareas,
# # para evaluar si trabaja con nosotros de ahora en adelante. Nos plantean los siguientes retos.
# #
# # Acceder a la información JSON de
# # https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/es.1.clubs.json y:
# # Averiguar cuántos equipos han participado en esta liga.
# # Mostrar todos los nombres de club de esta temporada, así como su código de 3 letras que 'casi'
# # todos los equipos tienen.
# # Extraer esa información del JSON original y guardarla en un fichero TXT.
# # Para asegurarse de que nos pueden dar el contrato, quieren que nuestro algoritmo sea estándar
# # a la hora de cargar información JSON de cualquier liga, por lo que nos proponen que nuestro código
# # funcione al cargar los datos de:
# #
# # Liga alemana
# # https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/de.1.clubs.json
# # Liga italiana
# # (https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json)
# # Liga austríaca
# # https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json
# # Liga inglesa
# # https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.clubs.json
# # Se ha de hacer con la menor cantidad de código posible y presentándole al usuario la posibilidad,
# # mediante un menú, de cargar la información de la liga que prefiera.

from date_futbol.get_futbol_data import LFP

if __name__ == '__main__':
    lfp: LFP = LFP()
    selected_option, name_file = lfp.menu()  # Call menu once and store the result
    league = lfp.get_futbool_data(selected_option)
    lfp.write_file(league, name_file)
