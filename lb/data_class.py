from dataclasses import dataclass
from typing import List, Dict, Union


@dataclass
class League:
    name: str
    clubs: List[Dict[str, Union[str, None]]]

    # __post_init__ para ejecutar automaticamente despues de la inicializacion de un objeto de esa clase
    def __post_init__(self):
        # instancia de la clase, y oobtencion de la lista para filtrar la instancia
        self.clubs = [club for club in self.clubs if club["code"] is not None]

