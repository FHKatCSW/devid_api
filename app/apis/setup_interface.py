from flask_restx import Namespace, Resource, fields

api = Namespace("setup", description="IEEE 802.1 AR Service related operations")

setup = api.model(
    "Setup",
    {
        "stack": fields.String(required=False, description="The stack")
    },
)

@api.response(404, "Status not found")
class Setup(Resource):

    @api.doc("get_status")
    @api.marshal_with(setup)
    def status(self):
        """Fetch the status of the HSM"""
        return {"status": "NotImplemented"}


    @api.doc("hsm")
    @api.marshal_with(setup)
    def setup_hsm(self):
        """Setup HSM for end device (PKCS#11)"""
        return {"status": "NotImplemented"}

    @api.doc("azure")
    @api.marshal_with(setup)
    def setup_azure(self):
        """Setup Azure IoT stack for end device"""
        return {"status": "NotImplemented"}

    @api.doc("aws")
    @api.marshal_with(setup)
    def setup_aws(self):
        """Setup aws IoT stack for end device"""
        return {"status": "NotImplemented"}
