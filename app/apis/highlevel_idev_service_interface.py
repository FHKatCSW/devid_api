from flask_restx import Namespace, Resource, fields
from app.core.adapters.hsm_objects import HsmObjects
from app.core.adapters.bootstrap_process import BootstrapDevId

api = Namespace("Highlevel-IDevID", description="Highlevel REST API Calls for the IDevID module")

@api.route('/delete', endpoint='highlvl-idev-del')
class HighLvlIDevDelete(Resource):

    @api.doc("delete")
    def delete(self):
        """Only for demonstration purpose: Delete the actual IDevID (key + cert)"""
        try:
            del_idev = HsmObjects(slot_num=0,
                              pin="1234")
            del_idev.delete_idev_keys()
            return {"success": True,
                    "message": "Keys deleted"}
        except Exception as err:
            return {"success": False,
                    "message": str(err)}


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
        try:
            idevid = BootstrapDevId(pin="1234", slot=0)
            idevid.setup_idev_id()
            idevid.create_key()
            idevid.generate_csr()
            idevid.request_cert(base_url='campuspki.germanywestcentral.cloudapp.azure.com',
                                p12_file='/home/admin/fhk_hmi_setup_v3.p12',
                                p12_pass='foo123',
                                certificate_profile_name='DeviceIdentity-Raspberry',
                                end_entity_profile_name='KF-CS-EE-DeviceIdentity-Raspberry',
                                certificate_authority_name='KF-CS-HMI-2023-CA')
            idevid.import_certificate()
            return {"success": True,
                    "message": "Bootstrap done"}
        except Exception as err:
            return {"success": False,
                    "message": str(err)}



@api.route('/actual', endpoint='highlvl-idev-get')
class HighLvlIDevProvision(Resource):
    @api.doc("get")
    def get(self):
        """Only for demonstration purpose: Provide the content of the actual IDevID certificate"""
        return {"success": True,
                "message": "NotImplemented"}