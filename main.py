from flask import Flask
from flask_restful import Api
from resource.construccion import Construccion
from resource.electricidad import Electricidad
from resource.poda import Poda


app = Flask(__name__)
api = Api(app)

api.add_resource(Construccion, "/construccion/<int:id>")
api.add_resource(Electricidad, "/electricidad/<int:id>")
api.add_resource(Poda, "/poda/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)
