import os

from dotenv import load_dotenv
from flask_script import Manager

from app import create_app, api, db
from app.controllers.product import ProductController

load_dotenv()

app = create_app(os.environ['APP_SETTINGS'])
manager = Manager(app)

api.add_resource(ProductController, '/product')

if __name__ == '__main__':
    manager.run()
