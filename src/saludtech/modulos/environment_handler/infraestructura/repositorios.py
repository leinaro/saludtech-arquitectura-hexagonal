""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from saludtech.config.db import db
from saludtech.modulos.environment_handler.dominio.repositorios import RepositorioUpload, RepositorioEnvironment
from saludtech.modulos.environment_handler.dominio.objetos_valor import NombreEnv, DataUrl
from saludtech.modulos.environment_handler.dominio.entidades import Upload, Environment
from saludtech.modulos.environment_handler.dominio.fabricas import FabricaUpload
from .dto import Upload as UploadDTO
from .mapeadores import MapeadorUpload
from uuid import UUID


class RepositorioUploadSQLite(RepositorioUpload):

    def __init__(self):
        self._fabrica_upload: FabricaUpload = FabricaUpload()

    @property
    def fabrica_upload(self):
        return self._fabrica_upload

    def obtener_por_id(self, id: UUID) -> Upload:
        upload_dto = db.session.query(UploadDTO).filter_by(id=str(id)).one()
        return self.fabrica_upload.crear_objeto(upload_dto, MapeadorUpload())

    def obtener_todos(self) -> list[Upload]:
        # TODO
        raise NotImplementedError

    def agregar(self, upload: Upload):
        upload_dto = self.fabrica_upload.crear_objeto(upload, MapeadorUpload())
        db.session.add(upload_dto)
        db.session.commit()

    def actualizar(self, upload: Upload):
        # TODO
        raise NotImplementedError

    def eliminar(self, upload_id: UUID):
        # TODO
        raise NotImplementedError