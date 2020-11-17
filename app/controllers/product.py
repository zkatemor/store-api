from flask_restful import Resource


class ProductController(Resource):
    def get(self):
        return {'hello': 'hello'}, 200
