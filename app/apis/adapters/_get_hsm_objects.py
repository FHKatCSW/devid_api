from cert_handler import CertHandler
from hsm_objects import HsmObjects


def main():
    hsm_objects = HsmObjects(
        slot_num=0,
        pin='1234'
    )
    print(hsm_objects.to_json())

if __name__ == "__main__":
    main()