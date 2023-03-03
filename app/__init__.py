from flask import Flask, jsonify
from flask import make_response
from app.apis import blueprint as api


# flask app factory to create app


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        response = make_response(jsonify('Success'), 200)
        response.headers["Content-type"] = "application/json"
        return response

    app.register_blueprint(api, url_prefix="/v1")
    return app
