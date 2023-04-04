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
        try:
            ldevid = BootstrapDevId(pin="1234", slot=0)
            ldevid.setup_ldev_id()
            ldevid.validate_idev_certifificate(
                ca_chain_url="https://campuspki.germanywestcentral.cloudapp.azure.com/ejbca/publicweb/webdist/certdist?cmd=cachain&caid=-1791256346&format=pem")
            ldevid.create_key()
            ldevid.generate_csr()
            ldevid.request_cert(base_url='campuspki.germanywestcentral.cloudapp.azure.com',
                                p12_file='/home/admin/certs/fhk_hmi_setup_v3.p12',
                                p12_pass='foo123',
                                certificate_profile_name='DeviceIdentity-Raspberry',
                                end_entity_profile_name='KF-CS-EE-DeviceIdentity-Raspberry',
                                certificate_authority_name='KF-CS-HMI-2023-CA')
            ldevid.import_certificate()
            ldevid.configure_azure()
            return {"success": True,
                    "message": "Bootstrap done"}
        except Exception as err:
            return {"success": False,
                    "message": str(err)}

@api.route('/actual', endpoint='highlvl-ldev-get')
class HighLvlLdevProvision(Resource):

    @api.doc("get")
    def get(self):
        """Only for demonstration purpose: Provide the content of the most recent LDevID certificate"""
        return {"success": True,
                "message": "NotImplemented"}