"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import saludtech.modulos.environment_handler.dominio.objetos_valor as ov
from saludtech.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Environment(Entidad):
    nombre: ov.NombreEnv = field(default_factory=ov.NombreEnv)

    def __str__(self) -> str:
        return self.id

@dataclass
class Upload(Entidad):
    #environment: ov.NombreEnv = field(default_factory=ov.Codigo)
    #client: ov.NombreAero = field(default_factory=ov.NombreAero)
    dataUrl: ov.DataUrl = field(default_factory=ov.DataUrl)