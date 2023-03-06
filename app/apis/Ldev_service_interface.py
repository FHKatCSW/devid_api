from flask_restx import Namespace, Resource, fields

api = Namespace("LDevID", description="IEEE 802.1 AR LDevID Service related operations")

@api.route('/key/generate/<keyIndex>', endpoint='ldevid-key')
@api.doc(params={'keyIndex': 'The keyIndex of the LDevID'})
class LDevIDKey(Resource):

    @api.doc("delete")
    def delete(self, keyIndex):
        """LDevID key delete (7.2.10): The DevID module performs cryptographic zeroization on LDevID key storage as part of the delete
process, removing both private and public key material."""
        return {"status": "NotImplemented"}

@api.route('/key/generate/<keyIndex>', endpoint='ldevid-key-generate')
@api.doc(params={'keyIndex': 'The keyIndex of the LDevID'})
class LDevIDKeyGenerate(Resource):

    @api.doc("create")
    def post(self, keyIndex):
        """LDevID key generate (7.2.8): This operation allows the device administrator to generate an additional LDevID key within the DevID
module. Newly generated keys are disabled and need to be explicitly enabled before use."""
        return {"status": "NotImplemented"}

@api.route('/key/insert/<keyIndex>', endpoint='ldevid-key-insert')
@api.doc(params={'keyIndex': 'The keyIndex of the LDevID'})
class LDevIDKeyInsert(Resource):
    @api.doc("post")
    def post(self, keyIndex):
        """LDevID key insert (7.2.9): This operation allows the device administrator to insert an externally generated LDevID key into the DevID
module."""
        return {"status": "NotImplemented"}

@api.route('/cert/<certificateIndex>', endpoint='ldevid-cert')
@api.doc(params={'certificateIndex': 'The certificateIndex of an LDevID certificate'})
class LDevIDCert(Resource):

    @api.doc("post")
    def post(self, certificateIndex):
        """Provision an LDevID certificate"""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, certificateIndex):
        """LDevID certificate delete (7.2.13): This operation implicitly deletes any certificate chain associated with the deleted certificate, it does not
remove the associated DevID secret. This operation does not delete an IDevID certificate even if identified
by the certificateIndex. The DevID module performs cryptographic zeroization on LDevID certificate material as part of the
delete process."""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, certificateIndex):
        """LDevID certificate export (NOT STANDARDIZED): Exports a certificate associated to a certificateIndex."""
        return {"status": "NotImplemented"}

@api.route('/chain/<certificateIndex>', endpoint='ldevid-chain')
@api.doc(params={'certificateIndex': 'The certificateIndex of the certificate associated with the certificate chain.'})
class LDevIDChain(Resource):

    @api.doc("post")
    def post(self, certificateIndex):
        """LDevID certificate chain insert (7.2.12): A certificate chain to be associated with a certificateIndex"""
        return {"status": "NotImplemented"}

    @api.doc("get")
    def get(self, certificateIndex):
        """LDevID certificate chain export (NOT STANDARDIZED): Exports a certificate chain associated to a certificateIndex."""
        return {"status": "NotImplemented"}

    @api.doc("delete")
    def delete(self, certificateIndex):
        """LDevID certificate chain delete (7.2.14): The DevID module performs cryptographic zeroization on LDevID certificate chain material as part of
the delete process."""
        return {"status": "NotImplemented"}




