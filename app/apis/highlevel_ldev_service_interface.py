from flask_restx import Namespace, Resource, fields
from app.core.adapters.hsm_objects import HsmObjects
from app.core.adapters.bootstrap_process import BootstrapDevId
from app.core.adapters.cert_handler import CertHandler

api = Namespace("Highlevel-LDevID", description="Highlevel REST API Calls for the LDevID module")

@api.route('/delete', endpoint='highlvl-ldev-del')
class HighLvlLdevDelete(Resource):

    @api.doc("delete")
    def delete(self):
        """Only for demonstration purpose: Delete the most recent LDevID (key + cert)"""
        try:
            del_idev = HsmObjects(slot_num=0,
                              pin="1234")
            del_idev.delete_ldev_objects()
            return {"success": True,
                    "message": "Keys deleted"}
        except Exception as err:
            return {"success": False,
                    "message": str(err)}

@api.route('/validate', endpoint='highlvl-ldev-val')
class HighLvlLdevValidate(Resource):

    @api.doc("post")
    def post(self):
        """Only for demonstration purpose: Delete the actual LDev cert"""
        return {"success": True,
                "message": "NotImplemented"}

@api.route('/provision', endpoint='highlvl-ldev-prov')
class HighLvlLdevProvision(Resource):

    @api.doc("post")
    def post(self):
        """Only for demonstration purpose: Provision a new IDevID (key + cert) via Azure"""
        return {"success": True,
                "message": "NotImplemented"}

@api.route('/actual', endpoint='highlvl-ldev-get')
class HighLvlLdevProvision(Resource):

    @api.doc("get")
    def get(self):
        """Only for demonstration purpose: Provide the content of the most recent LDevID certificate"""
        return {"success": True,
                "message": "NotImplemented"}