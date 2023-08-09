from base_de_datos import conexion
from models.usuario import UsuarioModel
from flask_restful import Resource, request
from dtos.usuario import UsuarioRequestDTO
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

class UsuariosController(Resource):
    def get(self):

        usuarios  = conexion.session.query(UsuarioModel).all()
        dto = UsuarioRequestDTO()
        resultado = dto.dump(usuarios, many=True)
        return {    
            'content': resultado
        }
    def post(self):
        data = request.json
        dto = UsuarioRequestDTO()
        try:
            dataValidada = dto.load(data)
            print(dataValidada)

            nuevoUsuario=UsuarioModel(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            return {
                'message': 'Usuario creado exitosamente'
            }, 201
        except ValidationError as error:
            return {   
                'message': 'Error al crear al usuario',
                'content': error.args
            }, 400
        except IntegrityError as error:
            return {       
                'message': 'Error al crear al usuario',
                'content': 'El usuario ya existe'
            }, 400
        except Exception as error:
            return {       
                'message': 'Error al crear al usuario',
                'content': error.args
            }, 500
        
class UsuarioController(Resource):
    def put(self, id):
        pass
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
        if not usuarioEncontrado:
            return {
                'message': 'Usuario no encontrado'
            }, 404
        data = request.get_json()
        dto = UsuarioRequestDTO()
        try:
            dataValidada = dto.load(data)
            usuarioActualizado = conexion.session.query(UsuarioModel).filter_by(id = id).update(dataValidada)
            print(usuarioActualizado)
            conexion.session.commit()
            return {
                'message': 'Usuario actualizado exitosamente'
            }, 201
        except ValidationError as error:
            return {   
                'message': 'Error al actualizar al usuario',
                'content': error.args
            }, 400
        except IntegrityError as error:
            return {       
                'message': 'Error al actualizar al usuario',
                'content': 'El usuario con ese correo ya existe'
            }, 400
    def delete(self, id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
        if not usuarioEncontrado:
            return {
                'message': 'Usuario no encontrado'
            }, 404
        conexion.session.query(UsuarioModel).filter_by(id = id).delete()
        conexion.session.commit()

        return {   
            'message': 'Usuario eliminado exitosamente'
        }, 200
    def get(self, id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
        if not usuarioEncontrado:
            return {
                'message': 'Usuario no encontrado'
            }, 404
        dto = UsuarioRequestDTO()
        UsuarioConvertido = dto.dump(usuarioEncontrado)
        return {  
            'content': UsuarioConvertido
        }, 200