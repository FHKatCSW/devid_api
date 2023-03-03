from flask_restx import Namespace, Resource

ns_kategorien = Namespace("Kategorien", description="Anfragen für die Kategorien")


@ns_kategorien.route("/<int:kid>")
class KategorienItem(Resource):
    def get(self, kid):
        return self.get_kategorie(kid)