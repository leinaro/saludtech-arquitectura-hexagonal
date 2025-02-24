from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class EnvironmentDTO(DTO):
    id: str
    nombre: str


@dataclass(frozen=True)
class UploadDTO(DTO):
    enviroment: str
    client: str
    #fecha: str
    dataUrl: str = field(default_factory=str)
