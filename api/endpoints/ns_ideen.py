from flask_restx import Namespace, Resource

ns_ideen = Namespace("Ideen", description="Anfragen für die ideen")


@ns_ideen.route("")
class IdeenListe(Resource):
    def get(self):
        """
        Zeige eine Liste aller Ideen
        """
        return self.get_alle_ideen()