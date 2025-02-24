""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Reserva
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from saludtech.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaEnvironment(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            environment: Environment = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return environment

@dataclass
class FabricaUpload(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Environment.__class__:
            fabrica_environment = _FabricaEnvironment()
            return fabrica_reserva.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()

