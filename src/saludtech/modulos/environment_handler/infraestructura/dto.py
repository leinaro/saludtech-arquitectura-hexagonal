"""DTOs para la capa de infrastructura del dominio de ingesta

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de ingesta

"""

from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Upload(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String, primary_key=True)
    #user_uuid = db.Column(db.String, nullable=False)
    #nombre = db.Column(db.String, nullable=False)
    #tipo = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String, nullable=False)

class Environment(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String, primary_key=True)
    #user_uuid = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    #tipo = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)