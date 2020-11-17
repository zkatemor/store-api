from flask import request, Response
from flask_restful import Resource

from models.product import Product


class ProductController(Resource):
    def post(self):
        try:
            body = request.get_json()
            movie = Product(**body).save()
            id = movie.id
            return {'id': str(id)}, 201
        except Exception as e:
            return {
                       "error": {
                           "message": str(e)
                       }
                   }, 422

    def get(self):
        try:
            movies = Product.objects().to_json()
            return Response(movies, mimetype="application/json", status=200)
        except Exception as e:
            return {
                       "error": {
                           "message": str(e)
                       }
                   }, 422
