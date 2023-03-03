from flask_restx import Namespace, Resource, fields

api = Namespace("LDevID", description="IEEE 802.1 AR LDevID Service related operations")

@api.route('/key/<name>', endpoint='ldevid-key')
@api.doc(params={'name': 'A name'})
class LDevIDKey(Resource):

    @api.doc("create")
    def post(self, name):
        """Create an LDevID key"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, name):
        """Delete an LDevID key"""
        return {"status": "NotImplemented"}

@api.route('/cert/<name>', endpoint='ldevid-cert')
@api.doc(params={'name': 'A name'})
class LDevIDKey(Resource):

    @api.doc("post")
    def post(self, name):
        """Provision an LDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, name):
        """Delete an LDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, name):
        """Export an LDevID certificate"""
        return {"status": "NotImplemented"}

@api.route('/chain/<name>', endpoint='ldevid-chain')
@api.doc(params={'name': 'A name'})
class LDevIDChain(Resource):

    @api.doc("post")
    def post(self, name):
        """Verify an LDevID certificate against it's chain"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, name):
        """Get the certificate chain of an LDevID"""
        return {"status": "NotImplemented"}




