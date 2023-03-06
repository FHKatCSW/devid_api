from flask_restx import Namespace, Resource, fields

api = Namespace("IDevID", description="IEEE 802.1 AR IDevID Service related operations")

@api.route('/key/generate/<keyIndex>', endpoint='idevid-key')
@api.doc(params={'keyIndex': 'The keyIndex of the IDevID'})
class IDevIDKey(Resource):

    @api.doc("delete")
    def delete(self, keyIndex):
        """IDevID key delete (7.2.10): The DevID module performs cryptographic zeroization on IDevID key storage as part of the delete
process, removing both private and public key material."""
        return {"status": "NotImplemented"}

@api.route('/key/generate/<keyIndex>', endpoint='idevid-key-generate')
@api.doc(params={'keyIndex': 'The keyIndex of the IDevID'})
class IDevIDKeyGenerate(Resource):

    @api.doc("create")
    def post(self, keyIndex):
        """IDevID key generate (NOT STANDARDIZED): This operation allows the device administrator to generate an  IDevID key within the DevID
module. Newly generated keys are disabled and need to be explicitly enabled before use."""
        return {"status": "NotImplemented"}

@api.route('/cert/<certificateIndex>', endpoint='idevid-cert')
@api.doc(params={'certificateIndex': 'The certificateIndex of an IDevID certificate'})
class IDevIDCert(Resource):

    @api.doc("post")
    def post(self, certificateIndex):
        """Provision an IDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, certificateIndex):
        """IDevID certificate delete (NOT STANDARDIZED): This operation implicitly deletes any certificate chain associated with the deleted certificate, it does not
remove the associated DevID secret. The DevID module performs cryptographic zeroization on IDevID certificate material as part of the
delete process."""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, certificateIndex):
        """IDevID certificate export (NOT STANDARDIZED): Exports a certificate associated to a certificateIndex."""
        return {"status": "NotImplemented"}

@api.route('/chain/<certificateIndex>', endpoint='idevid-chain')
@api.doc(params={'certificateIndex': 'The certificateIndex of the certificate associated with the certificate chain.'})
class IDevIDChain(Resource):

    @api.doc("post")
    def post(self, certificateIndex):
        """IDevID certificate chain insert (NOT STANDARDIZED): A certificate chain to be associated with a certificateIndex"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, certificateIndex):
        """IDevID certificate chain export (NOT STANDARDIZED): Exports a certificate chain associated to a certificateIndex."""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, certificateIndex):
        """IDevID certificate chain delete (NOT STANDARDIZED): The DevID module performs cryptographic zeroization on IDevID certificate chain material as part of
the delete process."""
        return {"status": "NotImplemented"}




