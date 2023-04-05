from flask_restx import Namespace, Resource
from app.apis.adapters.hsm_objects import HsmObjects
from app.apis.adapters.bootstrap_process import BootstrapDevId
from app.apis.adapters.cert_handler import CertHandler
from app.apis.adapters.validate_chain import CertValidator

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
        try:
            slot_num=0
            pin="1234"
            ca_chain_url = "https://campuspki.germanywestcentral.cloudapp.azure.com/ejbca/publicweb/webdist/certdist?cmd=cachain&caid=-1791256346&format=pem"
            hsm_objects = HsmObjects(
                slot_num=slot_num,
                pin=pin)
            hsm_ldev_id = hsm_objects.get_most_recent_ldev_id()
            public_web_validator = CertValidator(hsm_ldev_id)
            public_web_validator._load_ca_certs_via_public_web(ca_chain_url)
            valid = public_web_validator.validate()
            return {"success": True,
                    "message": "Validation checked",
                    "valid": valid}
        except Exception as err:
            return {"success": False,
                    "message": str(err),
                    "valid": None}

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
        try:
            slot_num=0
            pin="1234"
            hsm_objects = HsmObjects(
                slot_num=slot_num,
                pin=pin
            )
            hsm_ldev_id = hsm_objects.get_most_recent_ldev_id()
            export_cert = CertHandler(
                pin=pin,
                cert_id=hsm_ldev_id,
            )
            export_cert.export_certificate(output_directory="/home/admin/")
            actual_ldev = export_cert.parse_certificate()
            return {"success": True,
                    "message": "LDevId with the HSM ID {}".format(hsm_ldev_id),
                    "data": actual_ldev}

        except Exception as err:
            return {"success": False,
                    "message": str(err),
                    "data": None}