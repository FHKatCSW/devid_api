from flask_restx import Namespace, Resource, fields

api = Namespace("IDevID", description="IEEE 802.1 AR IDevID Service related operations")

@api.route('/key/<name>', endpoint='idevid-key')
@api.doc(params={'name': 'A name'})
class IDevIDKey(Resource):

    @api.doc("create")
    def post(self, name):
        """Create an IDevID key"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, name):
        """Delete an IDevID key"""
        return {"status": "NotImplemented"}

@api.route('/cert/<name>', endpoint='idevid-cert')
@api.doc(params={'name': 'A name'})
class IDevIDKey(Resource):

    @api.doc("post")
    def post(self, name):
        """Provision an IDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, name):
        """Delete an IDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, name):
        """Export an IDevID certificate"""
        return {"status": "NotImplemented"}

@api.route('/chain/<name>', endpoint='idevid-chain')
@api.doc(params={'name': 'A name'})
class IDevIDChain(Resource):

    @api.doc("post")
    def post(self, name):
        """Verify an IDevID certificate against it's chain"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, name):
        """Get the certificate chain of an IDevID"""
        return {"status": "NotImplemented"}




