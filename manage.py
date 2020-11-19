import os

from dotenv import load_dotenv
from flask_script import Manager

from app import create_app, api
from app.controllers.product_controller import ProductController, ProductShowController

load_dotenv()

app = create_app(os.environ['APP_SETTINGS'])
manager = Manager(app)

api.add_resource(ProductController, '/product')
api.add_resource(ProductShowController, '/product/<string:id>')

if __name__ == '__main__':
    manager.run()
