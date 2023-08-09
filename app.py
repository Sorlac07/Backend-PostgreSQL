from flask import Flask
from base_de_datos import conexion
from models.mascota import MascotaModel
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario import UsuariosController,UsuarioController
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from os import environ


app = Flask(__name__)
api = Api(app)
CORS(app,origins=['https://editor.swagger.io','http://mifrontend.com'],methods=['GET','POST','PUT','DELETE'],allow_headers=['Content-Type','Authorization','accept'])

SWAGGER_URL = '/docs'
# donde se almacena mi archivo de la documentacion
API_URL='/static/documentacion_swagger.json'

configuracionSwagger = get_swaggerui_blueprint(SWAGGER_URL, API_URL,config={
    # el nombre de la pestaña del navegador
    'app_name':'Documentacion de Directorio de Mascotas' 
})

# agregar otra aplicacion que no sea Flask a nuestro proyecto de Flask
app.register_blueprint(configuracionSwagger)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('password')

conexion.init_app(app)

Migrate(app=app, db=conexion)


api.add_resource(UsuariosController, '/usuarios')
api.add_resource(UsuarioController, '/usuario/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
