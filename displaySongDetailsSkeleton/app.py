from flask import Flask
from flask_restful import Api

import load_json as ljson
from songDetails import SongDetailByTitle , SongDetails

app = Flask(__name__)
api = Api(app)

ljson.create_table()
ljson.load_json()

api.add_resource(SongDetailByTitle ,'/detail/<string:title>')
api.add_resource(SongDetails,'/details')


if(__name__ == "__main__"):
    app.run(port=5000, debug=True)