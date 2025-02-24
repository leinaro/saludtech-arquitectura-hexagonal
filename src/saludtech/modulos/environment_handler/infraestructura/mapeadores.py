""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.image_handler.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from saludtech.modulos.image_handler.dominio.entidades import Environment
from .dto import Upload as UploadDTO
from .dto import Environment as EnvironmentDTO

class MapeadorUpload(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_upload_dto(self, upload_dto: UploadDTO) -> Upload:
        upload_dict = dict()
        
        
        environment = Environment(nombre=None)
        client = "cliente123"
        #fecha = upload_dto.fecha_salida
        dataUrl = upload_dto.fecha_llegada

        upload_dict.setdefault(str(itin.odo_orden),{}).setdefault(str(itin.segmento_orden), {}).setdefault(str(itin.leg_orden), Leg(fecha_salida, fecha_llegada, origen, destino))

        
        return [Itinerario(odos)]

    def _procesar_upload(self, upload: any) -> UploadDTO:
        upload_dto = UploadDTO()

      #  upload_dto.id = "123456"
        upload_dto.url = "qwerty13245"
#        upload_dto.fecha_creacion =

        return upload_dto

    def obtener_tipo(self) -> type:
        return Upload.__class__

    def entidad_a_dto(self, entidad: Upload) -> UploadDTO:
        
        upload_dto = UploadDTO()
        upload_dto.fecha_creacion = entidad.fecha_creacion
        upload_dto.fecha_actualizacion = entidad.fecha_actualizacion
        upload_dto.id = str(entidad.id)

        return upload_dto

    def dto_a_entidad(self, dto: UploadDTO) -> Upload:
        upload = Upload(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        
        return upload