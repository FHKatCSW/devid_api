from flask_restx import Namespace, Resource, fields

api = Namespace("ldevid", description="IEEE 802.1 AR ldevid Service related operations")

ldevid = api.model(
    "ldevid",
    {
        "status": fields.String(required=False, description="The setup status of the HSM (none, build, active)")
    },
)

@api.route('/create/<name>', endpoint='create')
@api.doc(params={'name': 'A name'})
class CreateIDevID(Resource):

    @api.doc("create")
    def post(self, id):
        """Create an LDevID key"""
        return {"status": "NotImplemented"}

@api.route('/ldevid', endpoint='ldevid')
class ldevid(Resource):

    @api.doc("create")
    @api.marshal_with(ldevid)
    def create(self):
        """Create an LDevID key"""
        return {"status": "NotImplemented"}
    
    @api.doc("delete")
    @api.marshal_with(ldevid)
    def delete(self):
        """Delete an LDevID key"""
        return {"status": "NotImplemented"}

    @api.doc("provision")
    @api.marshal_with(ldevid)
    def provision(self):
        """provision an LDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("verify")
    @api.marshal_with(ldevid)
    def verify(self):
        """Verify an LDevID"""
        return {"status": "NotImplemented"}

    @api.doc("export")
    @api.marshal_with(ldevid)
    def export(self):
        """Export an LDevID"""
        return {"status": "NotImplemented"}
