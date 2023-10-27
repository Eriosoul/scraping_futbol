import os.path
from lb.data_class import League
import requests
from requests import Response


class LFP:
    def __init__(self):
        self.spain: str = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/es.1.clubs.json'
        self.german: str = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/de.1.clubs.json'
        self.italy: str = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json'
        self.aus: str = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json'
        self.english: str = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.clubs.json'

    def get_futbool_data(self, selected: str) -> League:
        try:
            r: Response = requests.get(selected)
            # comprobamos el estado del servidor
            if r.status_code != 200:
                print("Error al intentar acceder a los datos, no se ha podido conectar con el servidor")
                return League(name="", clubs=[])
            # asignamos json a una variable y procedemos a ver los datos del dicionario
            data: dict = r.json()
            titulo: str = data["name"]
            print("Nombre de la competicion: ", titulo)
            # clubs = data["clubs"]
            league: League = League(name=data["name"], clubs=data["clubs"])
            print("Clubes:")
            # recorremos los datos
            for club in league.clubs:
                name: str = club["name"]
                code: str = club["code"]
                contry_data: str = club["country"]
                # en este caso se muestra todo pero en la siguente funcion solo se obtiene el nombre y codigo
                print(f"Nombre: {name}, Codigo: {code}, Pais: {contry_data}")
            return league
        except Exception as x:
            print("Error al obtener los datos. Código de estado:", x)
            return League(name="", clubs=[])

    def write_file(self, league: League, name_file: str):
        # comprobacion del estado del fichero
        if os.path.exists(name_file):
            print("\n \n El fichero ya existe, ¿Que deseas hacer?")
            user_choice: str = input("Presiona 'Y' para reescribir el fichero, 'N' para no reescribir: ").lower()
            if user_choice == "y":
                os.remove(name_file)
            else:
                print("El fichero no se volvio a sobreescribir, Gracias.")
                return  # No hace nada en caso de que seleciones no sobreescribir
        # Procedemos a abrir el fichero y a realizar un append para que no se vaya sobreescribiendo en la misma linea
        with open(name_file, 'a', encoding='utf-8') as file:
            file.write(f"League Name: {league.name}\n")

            # Informacion del club
            file.write("Clubs:\n")
            for club in league.clubs:
                # file.write(f"Code: {club['code']}, Name: {club['name']}, Country: {club['contry_data']} \n")
                file.write(f"Code: {club['code']}, Name: {club['name']} \n")

        print(f"Se reescribio : {name_file}.\n")

    def menu(self):
        option: int = 0
        selected: str = ""
        # Menu con opcion entre 1 y 5
        while option < 1 or option > 5:
            print("==========  Menu ===========")
            print("1. Seleccion española")
            print("2. Seleccion alemana")
            print("3. Seleccion italiana")
            print("4. Seleccion austriaca")
            print("5. Seleccion inglesa")
            print("=======================")
            option_select = input("Seleccione una opcion: ")
            # segun la opcion selecionada llama a una funcion y otorga nombre al fichero.txt
            try:
                option: int = int(option_select)
                if option == 1:
                    selected = self.spain
                    name_file: str = "Spain.txt"
                elif option == 2:
                    selected = self.german
                    name_file: str = "German.txt"
                elif option == 3:
                    selected = self.italy
                    name_file: str = "Italy.txt"
                elif option == 4:
                    selected = self.aus
                    name_file: str = "Austria.txt"
                elif option == 5:
                    selected = self.english
                    name_file: str = "English.txt"
                else:
                    print("Opcion no valida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un numero valido.")
        return selected, name_file
