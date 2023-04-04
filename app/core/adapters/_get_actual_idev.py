from app.core.adapters.cert_handler import CertHandler
from app.core.adapters.hsm_objects import HsmObjects


def main():
    hsm_objects = HsmObjects(
        slot_num=0,
        pin='1234'
    )
    hsm_idev_id = hsm_objects.get_actual_idev_id()

    export_cert = CertHandler(
        pin="1234",
        cert_id=hsm_idev_id,
    )
    export_cert.export_certificate(output_directory="/home/admin/")
    actual_idev = export_cert.parse_certificate()
    print(actual_idev)

if __name__ == "__main__":
    main()