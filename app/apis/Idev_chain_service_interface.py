from flask_restx import Namespace, Resource, fields

api = Namespace("IDevID-Chain", description="IEEE 802.1 AR IDevID Certificate Chain operations")

@api.route('/chain/<certificateIndex>', endpoint='ldevid-chain')
@api.doc(params={'certificateIndex': 'The certificateIndex of the certificate associated with the certificate chain.'})
class IDevIDChain(Resource):

    @api.doc("post")
    def post(self, certificateIndex):
        """IDevID certificate chain insert (NOT STANDARDIZED)"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, certificateIndex):
        """IDevID certificate chain export (NOT STANDARDIZED): Exports a certificate chain associated to a certificateIndex"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, certificateIndex):
        """IDevID certificate chain delete (NOT STANDARDIZED): The DevID module performs cryptographic zeroization on IDevID certificate chain material as part of the delete process"""

        return {"status": "NotImplemented"}




