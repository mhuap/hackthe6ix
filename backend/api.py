from flask import Flask
from flask_restful import Api, Resource, reqparse
import geo
import run
app = Flask(__name__)
api = Api(app)

class User(Resource):
    def post(self, name): 
        parser = reqparse.RequestParser()
        parser.add_argument("url")
        args = parser.parse_args()

        risk, premium = run.do_scrape(args["url"])
        values = {
            "risk": risk,
            "premium": premium,
        }

        return values, 201

api.add_resource(User, "/user/<string:name>")
app.run(debug=True)