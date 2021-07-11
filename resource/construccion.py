from flask_restful import Resource, reqparse
from logic.construccion_logic import ConstruccionLogic


class Construccion(Resource):
    def __init__(self):
        self.construccion_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre producto", type=str, help="nombre del producto")
        args.add_argument(
            "tipo", type=str, help="Tipo de producto(herramienta, equipo o material)"
        )
        args.add_argument("descripcion", type=str, help="descripcion del producto")
        args.add_argument("precio", type=int, help="precio del producto")
        args.add_argument(
            "tienda", type=str, help="tienda donde se encuentra el producto"
        )
        args.add_argument("link", type=str, help="link")

        return args

    # Solo definir metodos get y post

    def get(self, id):
        logic = ConstruccionLogic()
        result = logic.getConstruccionById(id)
        if len(result) == 0:
            return {}
        return result[0], 200

    def post(self, id):
        logic = ConstruccionLogic()
        result = logic.getConstruccionAll()
        if len(result) == 0:
            return {}
        return result[0], 200
