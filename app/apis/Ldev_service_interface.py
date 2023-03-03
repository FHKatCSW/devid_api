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
    @api.doc(params={'test': 'A test'})
    def get(self, name):
        """Export an LDevID certificate"""
        return {"status": "NotImplemented"}




