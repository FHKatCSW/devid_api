from flask_restx import Namespace, Resource, fields

from app.core.adapters.service_adapter import ServiceManager

api = Namespace("Highlevel-IDevID", description="Highlevel REST API Calls for the IDevID module")

@api.route('/delete', endpoint='highlvl-idev-del')
class HighLvlIDevDelete(Resource):

    @api.doc("delete")
    def delete(self):
        """Only for demonstration purpose: Delete the actual IDevID (key + cert)"""
        # del_idev = ServiceManager()
        # certificates = del_idev.enumerate_certificates()
        # del_idev.delete_key()
        # del_idev.delete_certificate()
        return {"success": True,
                "message": "NotImplemented"}

@api.route('/validate', endpoint='highlvl-idev-val')
class HighLvlIDevValidate(Resource):

    @api.doc("post")
    def post(self):
        """Only for demonstration purpose: Delete the actual IDevID cert"""
        return {"success": True,
                "message": "NotImplemented"}

@api.route('/provision', endpoint='highlvl-idev-prov')
class HighLvlIDevProvision(Resource):

    @api.doc("post")
    def post(self):
        """Only for demonstration purpose: Provision a new IDevID (key + cert)"""
        return {"success": True,
                "message": "NotImplemented"}

@api.route('/actual', endpoint='highlvl-idev-get')
class HighLvlIDevProvision(Resource):
    @api.doc("post")
    def post(self):
        """Only for demonstration purpose: Provide the content of the actual IDevID certificate"""
        return {"success": True,
                "message": "NotImplemented"}