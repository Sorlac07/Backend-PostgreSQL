from flask import Flask
from base_de_datos import conexion
from models.mascota import MascotaModel
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario import UsuariosController,UsuarioController

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('password')

conexion.init_app(app)

Migrate(app=app, db=conexion)

# @app.route('/crear-tablas',methods=['GET'])
#def crearTablas():
#    # creara todas las tablas declaradas en el proyecto
#    conexion.create_all()
#    return {
#        'message': 'Creacion ejecutada exitosamente'
#    }
#
api.add_resource(UsuariosController, '/usuarios')
api.add_resource(UsuarioController, '/usuario/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
