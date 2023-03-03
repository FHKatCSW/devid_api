from flask_restx import Namespace, Resource, fields

api = Namespace("LDevID", description="IEEE 802.1 AR LDevID Service related operations")


@api.route('/<name>', endpoint='create')
@api.doc(params={'name': 'A name'})
class LDevID(Resource):

    @api.doc("create")
    def post(self, name):
        """Create an LDevID key"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, name):
        """Delete an LDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, name):
        """Export an LDevID certificate"""
        return {"status": "NotImplemented"}


@api.route('/provision/<name>', endpoint='provision-ldevid')
@api.doc(params={'name': 'A name'})
class ProvisionLDevID(Resource):

    @api.doc("provision")
    def post(self, name):
        """Provision an LDevID certificate"""
        return {"status": "NotImplemented"}


@api.route('/verify/<name>', endpoint='verify-ldevid')
@api.doc(params={'name': 'A name'})
class VerifyLDevID(Resource):

    @api.doc("post")
    def post(self, name):
        """Verify an LDevID certificate"""
        return {"status": "NotImplemented"}



