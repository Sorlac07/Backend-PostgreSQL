from router import api
from controllers.usuario import *

api.add_resource('/usuario',UsuarioController)
#api.add_resource(UsuarioController, '/usuario')