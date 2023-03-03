from flask_restx import Namespace, Resource, fields

api = Namespace("ldevid", description="IEEE 802.1 AR LDevID Service related operations")

ldevid = api.model(
    "LDevID",
    {
        "status": fields.String(required=False, description="The setup status of the HSM (none, build, active)")
    },
)



@api.response(404, "Status not found")
class Setup(Resource):

    @api.doc("status")
    @api.marshal_with(ldevid)
    def status(self):
        """Fetch the status of the HSM"""
        return {"status": "NotImplemented"}

    @api.doc("verify_idevid")
    @api.marshal_with(ldevid)
    def verify_idevid(self):
        """Create an IDevID key"""
        return {"status": "NotImplemented"}

