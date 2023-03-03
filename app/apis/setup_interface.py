from flask_restx import Namespace, Resource, fields

api = Namespace("setup", description="IEEE 802.1 AR Service related operations")

@api.route('/hsm/<name>', endpoint='hsm')
class HsmSetup(Resource):

    @api.doc("post")
    def post(self):
        """Setup the HSM"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self):
        """Get the status of the HSM"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self):
        """Delete the HSM setup"""
        return {"status": "NotImplemented"}


@api.route('/azure/<name>', endpoint='azure')
class AzureSetup(Resource):

    @api.doc("post")
    def post(self):
        """Setup the Azure IoT stack"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self):
        """Get the status of the Azure IoT stack"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self):
        """Delete the Azure IoT stack setup"""
        return {"status": "NotImplemented"}
