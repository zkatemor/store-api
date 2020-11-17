from flask_restful import Resource


class ProductController(Resource):
    def post(self):
        try:
            title, definition, link, token = self.create_params()
        except Exception as e:
            return {
                       "error": {
                           "message": "title, definition, link, token is required"
                       }
                   }, 422
