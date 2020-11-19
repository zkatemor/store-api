from flask_restful import Resource, reqparse

from models.product import Product


class ProductController(Resource):
    def create_params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('params', type=dict, action="append", required=True)
        args = parser.parse_args()
        return args['name'], args['description'], args['params']

    def show_params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=False)
        parser.add_argument('params', type=dict, action="append", required=False)
        args = parser.parse_args()
        return args['name'], args['params']

    def schema(self, products):
        return {"result": [{"id": str(product.id), "name": product.name} for product in products]}

    def post(self):
        try:
            name, description, params = self.create_params()
            product = Product(name=name, description=description, params=params).save()
            return {
                       "successful": {
                           "id": str(product.id)}
                   }, 201
        except Exception as e:
            return {
                       "error": {
                           "message": str(e)
                       }
                   }, 422

    def get(self):
        try:
            name, params = self.show_params()
            if name is not None and params is not None:
                products = Product.objects(name=name, params__in=params)
            elif name is not None:
                products = Product.objects(name=name)
            elif params is not None:
                products = Product.objects(params__in=params)
            else:
                products = Product.objects()

            return self.schema(products), 200
        except Exception as e:
            return {
                       "error": {
                           "message": str(e)
                       }
                   }, 422


class ProductShowController(Resource):
    def schema(self, product):
        return {"result": {"name": product.name, "description": product.description, "params": product.params}}

    def get(self, id):
        try:
            product = Product.objects.get(id=id)

            return self.schema(product), 200
        except Exception as e:
            return {
                       "error": {
                           "message": "not found"
                       }
                   }, 404
