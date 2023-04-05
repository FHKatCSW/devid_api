from cert_handler import CertHandler
from hsm_objects import HsmObjects


def main(id):
    export_cert = CertHandler(
        pin="1234",
        cert_id=id,
    )
    export_cert.export_certificate(output_directory="/home/admin/")
    actual_idev = export_cert.parse_certificate()
    print(actual_idev)

if __name__ == "__main__":
    main("10fa29a47f0000001000000000000000")