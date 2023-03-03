from flask_restx import Namespace, Resource, fields

api = Namespace("idevid", description="IEEE 802.1 AR IDevID Service related operations")


@api.route('/create/<name>', endpoint='create')
@api.doc(params={'name': 'A name'})
class CreateIDevID(Resource):

    @api.doc("create")
    def post(self, id):
        """Create an IDevID key"""
        return {"status": "NotImplemented"}
    
@api.route('/delete-cert/<name>', endpoint='delete-cert')
@api.doc(params={'name': 'A name'})
class DeleteIDevIDCert(Resource):

    @api.doc("delete")
    def delete(self, name):
        """Delete an IDevID certificate"""
        return {"status": "NotImplemented"}
    
@api.route('/provision/<name>', endpoint='provision')
@api.doc(params={'name': 'A name'})
class ProvisionIDevID(Resource):

    @api.doc("provision")
    def post(self, name):
        """Provision an IDevID certificate"""
        return {"status": "NotImplemented"}

@api.route('/verify/<name>', endpoint='verify')
@api.doc(params={'name': 'A name'})
class VerifyIDevID(Resource):

    @api.doc("post")
    def post(self, name):
        """Verify an IDevID certificate"""
        return {"status": "NotImplemented"}

@api.route('/export/<name>', endpoint='export')
@api.doc(params={'name': 'A name'})
class VerifyIDevID(Resource):

    @api.doc("get")
    def get(self, name):
        """Export an IDevID certificate"""
        return {"status": "NotImplemented"}

