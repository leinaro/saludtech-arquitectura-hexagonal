"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor, Codigo

from datetime import datetime
from enum import Enum


class TipoImagen(Enum):
    JPG = "jpg"
    png = "png"

@dataclass(frozen=True)
class Imagen(ObjetoValor):
    ...

@dataclass(frozen=True)
class NombreEnv():
    nombre: str

@dataclass(frozen=True)
class DataUrl():
    url: str