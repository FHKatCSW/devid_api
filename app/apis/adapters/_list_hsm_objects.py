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

if __name__ == "__main__":
    main()