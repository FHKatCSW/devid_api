from flask import Flask, Blueprint
from flask_restx import Api

from endpoints import ns_ideen  # Importieren der API-Endpoints
from endpoints import ns_kategorien  #

app = Flask(__name__)  # ohne Starten der Hauptanwendung testen


api = Api(  # Metadaten der API
    title="Ideenbriefkasten API",
    version="1.0",
    description="API für den Ideenbriefkasten der Beispiel AG")

api.add_namespace(ns_ideen, path="/ideen")  # Initialisieren der Endpoints
api.add_namespace(ns_kategorien, path="/kategorien")  #

bp = Blueprint('api', __name__, url_prefix='/api')  # Initialisieren der API unter der URL /api
api.init_app(bp)  #

app.register_blueprint(bp)  #

