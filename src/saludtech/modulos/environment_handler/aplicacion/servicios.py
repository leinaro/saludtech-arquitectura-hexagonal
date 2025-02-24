from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.vuelos.dominio.entidades import Reserva
from saludtech.modulos.vuelos.dominio.fabricas import FabricaVuelos
from saludtech.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
from .mapeadores import MapeadorReserva

from .dto import UploadDTO

class ServicioCargar(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def crear_reserva(self, reserva_dto: ReservaDTO) -> ReservaDTO:
        reserva: Reserva = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        repositorio.agregar(reserva)

        return self.fabrica_vuelos.crear_objeto(reserva, MapeadorReserva())

    def obtener_reserva_por_id(self, id) -> ReservaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        return repositorio.obtener_por_id(id).__dict__

