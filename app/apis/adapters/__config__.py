from app.apis.adapters import logger

class Configuration:
    def __init__(self):
        self.logger = logger.get_logger("Configuration")

        # EJBCA URL and authentication
        self.ejbca_url = None
        self.p12_auth_file_path = None
        self.p12_auth_file_pwd = None

        # IDevID configuration for EJBCA
        self.certificate_profile_name_idev = None
        self.end_entity_profile_name_idev = None
        self.certificate_authority_name_idev = None
        self.ca_chain_url_idev = None

        # LDevID configuration for EJBCA
        self.certificate_profile_name_ldev_basic = None,
        self.end_entity_profile_name_ldev_basic = None,
        self.certificate_authority_name_ldev_basic = None

        self.hsm_pin = "1234"

        self.local_setup()

    def azure_setup(self):
        #self.logger.info("Using the Azure configuration")

        # EJBCA URL and authentication
        self.ejbca_url = 'campuspki.germanywestcentral.cloudapp.azure.com'
        self.p12_auth_file_path = '/home/admin/fhk_hmi_setup_v3.p12'
        self.p12_auth_file_pwd = 'foo123'

        # IDevID configuration for EJBCA
        self.certificate_profile_name_idev = 'DeviceIdentity-Raspberry',
        self.end_entity_profile_name_idev = 'KF-CS-EE-DeviceIdentity-Raspberry',
        self.certificate_authority_name_idev = 'KF-CS-HMI-2023-CA'
        self.ca_chain_url_idev = "https://campuspki.germanywestcentral.cloudapp.azure.com/ejbca/publicweb/webdist/certdist?cmd=cachain&caid=-1791256346&format=pem"
        # LDevID configuration for EJBCA
        self.certificate_profile_name_ldev_basic = 'DeviceIdentity-Raspberry',
        self.end_entity_profile_name_ldev_basic = 'KF-CS-EE-DeviceIdentity-Raspberry',
        self.certificate_authority_name_ldev_basic = 'KF-CS-HMI-2023-CA'

    def local_setup(self):
        #self.logger.info("Using the Local configuration")

        # EJBCA URL and authentication
        self.ejbca_url = '192.168.1.3'
        self.p12_auth_file_path = '/home/admin/certs/RestAdminHmi_0001.p12'
        self.p12_auth_file_pwd = 'foo123'

        # IDevID configuration for EJBCA
        self.certificate_profile_name_idev = 'EndEntityProfile-IDevId',
        self.end_entity_profile_name_idev = 'EndEntity-IDevId',
        self.certificate_authority_name_idev = 'IDevID-CA'
        self.ca_chain_url_idev = "https://ejbca-node1:443/ejbca/publicweb/webdist/certdist?cmd=cachain&caid=-1794496514&format=pem"

        # LDevID configuration for EJBCA
        self.certificate_profile_name_ldev_basic = 'DeviceIdentity-Raspberry',
        self.end_entity_profile_name_ldev_basic = 'KF-CS-EE-DeviceIdentity-Raspberry',
        self.certificate_authority_name_ldev_basic = 'KF-CS-HMI-2023-CA'
