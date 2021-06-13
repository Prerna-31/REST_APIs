from flask import Flask
from flask_restful import Api

from product import Product
from emails import Emails

app = Flask(__name__)

api = Api(app)

api.add_resource(Product,'/product')
api.add_resource(Emails,'/email')

if(__name__ == '__main__'):
    app.run(port=5000, debug=True)