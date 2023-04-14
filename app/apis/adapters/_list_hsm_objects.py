from app.apis.adapters.__config__ import Configuration
from app.apis.adapters.hsm_objects import HsmObjects

config = Configuration()


def main():
    print("--- Print Objects ---")
    hsm_objects = HsmObjects(
        slot_num=0,
        pin=config.hsm_pin
    )
    print(hsm_objects.to_dict())

    print("Number of private keys on HSM: {}".format(hsm_objects.count_keys(public=False)))
    print("Number of public keys on HSM: {}".format(hsm_objects.count_keys(private=False)))
    print("Number of certificates on HSM: {}".format(hsm_objects.coun_certificates()))


if __name__ == "__main__":
    main()