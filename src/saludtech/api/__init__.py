import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import saludtech.modulos.cliente.infraestructura.dto
    import saludtech.modulos.hoteles.infraestructura.dto
    import saludtech.modulos.pagos.infraestructura.dto
    import saludtech.modulos.precios_dinamicos.infraestructura.dto
    import saludtech.modulos.vehiculos.infraestructura.dto
    import saludtech.modulos.vuelos.infraestructura.dto

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    if configuracion is not None and configuracion["TESTING"]:
        app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + configuracion["DATABASE"]
    
    # Configuracion de BD
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from saludtech.config.db import init_db
    init_db(app)

    from saludtech.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

     # Importa Blueprints
    from . import cliente, hoteles, pagos, precios_dinamicos, vehiculos, vuelos

    # Registro de Blueprints
    app.register_blueprint(cliente.bp)
    app.register_blueprint(hoteles.bp)
    app.register_blueprint(pagos.bp)
    app.register_blueprint(precios_dinamicos.bp)
    app.register_blueprint(vehiculos.bp)
    app.register_blueprint(vuelos.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.1"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/ping")
    def health():
        return {"status": "up"}

    return app
