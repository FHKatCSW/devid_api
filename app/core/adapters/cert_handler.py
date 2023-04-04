import subprocess
import logger
import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend

class CertHandler:
    def __init__(self, pin, cert_id, pkcs11_module='/usr/lib/opensc-pkcs11.so'):
        self.logger = logger.get_logger("CertHandler")

        self.pkcs11_module = pkcs11_module
        self.cert_id = cert_id
        self.pin = pin
        self.output_path = None
        self.cert_content = None
        self.parsed_cert = {}

    def insert_certificate(self, certificate_path, slot, cert_label):
        self.logger.info("-insert certificate")
        self.logger.info("--cert id: {}; cert label: {}".format(self.cert_id, cert_label))

        command = [
            "./bash/insert_cert.sh",
            f'--certificate_path={certificate_path}',
            f'--hsm_slot={slot}',
            f'--hsm_pin={self.pin}',
            f'--id={self.cert_id}',
            f'--label={cert_label}',
        ]

        subprocess.call(command)

    def export_certificate(self, output_directory):
        target_dir = os.path.join(output_directory, "temp_certs")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            self.logger.info(f"Created directory at {target_dir}")
        target_path = os.path.join(target_dir, "{}.pem".format(self.cert_id))

        self.logger.info("-export certificate")
        self.logger.info("--cert id: {}".format(self.cert_id))
        self.logger.info("--output file: {}".format(target_path))
        self.output_path = output_directory

        command = [
            "./bash/export_cert.sh",
            f'--module={self.pkcs11_module}',
            f'--id={self.cert_id}',
            f'--output_file={target_path}',
            f'--pin={self.pin}',
        ]

        subprocess.call(command)
        self.load_cert()

    def load_cert(self):
        # Load the PEM certificate
        with open(self.output_path, 'rb') as f:
            self.cert_content = f.read()

    def parse_certificate(self):
        # Parse the certificate
        cert = x509.load_pem_x509_certificate(self.cert_content, default_backend())

        # Extract the issuer
        self.parsed_cert["issuer"] = cert.issuer

        # Extract the validity period
        self.parsed_cert["validity"] = cert.not_valid_before, cert.not_valid_after

        # Extract the serial number
        self.parsed_cert["serial_number"] = cert.serial_number

        # Extract the subject
        subject = cert.subject

        # Extract the CN, O, and OU fields from the subject
        self.parsed_cert["cn"] = subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
        self.parsed_cert["o"] = subject.get_attributes_for_oid(x509.NameOID.ORGANIZATION_NAME)[0].value
        self.parsed_cert["ou"] = subject.get_attributes_for_oid(x509.NameOID.ORGANIZATIONAL_UNIT_NAME)[0].value

        return self.parsed_cert


def import_certificate():
    insert_cert = CertHandler(
        pin = "1234",
        cert_id = 5,
    )
    insert_cert.insert_certificate(slot=0,
                                   cert_label="test",
                                   certificate_path="/home/admin/certs/test.pem")

def export_certificate():
    export_cert = CertHandler(
        pin = "1234",
        cert_id = 5,
    )
    export_cert.export_certificate(output_directory="/home/admin/")

if __name__ == "__main__":
    import_certificate()
