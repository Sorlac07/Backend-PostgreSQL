from base_de_datos import conexion
from models.usuario import UsuarioModel
from flask_restful import Resource, request

class UsuarioController(Resource):
    def get(self):
        return {    
            'message': 'Hola desde el controlador'
        }
    def post(self):
        data = request.json
        nuevoUsuario=UsuarioModel(nombre=data.get('nombre',''),apellido=data.get('apellido',''),correo=data.get('correo'),telefono=data.get('telefono'),
        linkedinUrl=data.get('linkedinUrl'))
        conexion.session.add(nuevoUsuario)
        conexion.session.commit()
        return {
            'message': 'Hola desde el post'
        }