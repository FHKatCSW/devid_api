from flask_restx import Namespace, Resource, fields

api = Namespace("mgmt", description="IEEE 802.1 ARManagement related operations")

@api.route('/logs/<name>', endpoint='logs')
class LDevIDKey(Resource):

    @api.doc("get")
    def get(self):
        """Get the logs of the DevID Management Interface"""
        return {"status": "NotImplemented"}
