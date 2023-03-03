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
    
@api.route('/delete/<name>', endpoint='delete')
@api.doc(params={'name': 'A name'})
class DeleteIDevID(Resource):

    @api.doc("delete")
    def delete(self, name):
        """Delete an LDevID key"""
        return {"status": "NotImplemented"}
    
@api.route('/provision/<name>', endpoint='provision')
@api.doc(params={'name': 'A name'})
class ProvisionIDevID(Resource):

    @api.doc("provision")
    def post(self, name):
        """Provision an LDevID certificate"""
        return {"status": "NotImplemented"}

@api.route('/verify/<name>', endpoint='verify')
@api.doc(params={'name': 'A name'})
class VerifyIDevID(Resource):

    @api.doc("post")
    def post(self, name):
        """Provision an LDevID certificate"""
        return {"status": "NotImplemented"}

@api.route('/ldevid', endpoint='ldevid')
class ldevid(Resource):

    @api.doc("verify")
    @api.marshal_with(ldevid)
    def verify(self):
        """Verify an LDevID"""
        return {"status": "NotImplemented"}

    @api.doc("post")
    @api.marshal_with(ldevid)
    def export(self):
        """Export an LDevID"""
        return {"status": "NotImplemented"}
