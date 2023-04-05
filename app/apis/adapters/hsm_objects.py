import re
import json
import subprocess

from id_manager import IDManager


class HsmObjects:
    def __init__(self, slot_num, pin):
        self.slot_num = slot_num
        self.pin = pin
        objects = self.list_objects_on_hsm()
        self.parsed_objects = None
        self.parse_input_str(objects)

    def list_objects_on_hsm(self):
        # Run the bash script and capture the output
        result = subprocess.check_output(["./bash/list_objects.sh",  str(self.slot_num), self.pin])
        result_str = result.decode('utf-8')  # decode bytes object to string
        return result_str

    def parse_input_str(self, input_str):

        self.parsed_objects = {
            "private_keys": {},
            "public_keys": {},
            "certificates": {}
        }

        current_key_type = None
        current_key_label = None

        for line in input_str.split("\n"):
            line = line.strip()
            if line.startswith("Private Key Object"):
                current_key_type = "private_keys"
            elif line.startswith("Public Key Object"):
                current_key_type = "public_keys"
            elif line.startswith("Certificate Object"):
                current_key_type = "certificates"
            elif line.startswith("label:"):
                current_key_label = line.split(":")[1].strip()
                self.parsed_objects[current_key_type][current_key_label] = {}
            elif line.startswith("ID:"):
                self.parsed_objects[current_key_type][current_key_label]["ID"] = line.split(":")[1].strip()
            elif line.startswith("Usage:"):
                self.parsed_objects[current_key_type][current_key_label]["Usage"] = line.split(":")[1].strip()
            elif line.startswith("Access:"):
                self.parsed_objects[current_key_type][current_key_label]["Access"] = line.split(":")[1].strip()
            elif line.startswith("subject:"):
                self.parsed_objects[current_key_type][current_key_label]["subject"] = "{}: {}".format(line.split(":")[1].strip(), line.split(":")[2].strip())


    def to_dict(self):
        return self.parsed_objects

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def filter_id_by_label(self, key_label):
        keys = self.to_json()
        keys_str = json.loads(keys)
        for key_type in ["private_keys", "public_keys"]:
            if key_label in keys_str[key_type]:
                return keys_str[key_type][key_label]["ID"]

    def get_actual_idev_id(self):

        data = self.to_dict()

        for key, value in data['private_keys'].items():
            if key.startswith('idev'):
                return value['ID']
        return None

    def get_most_recent_ldev_id(self):
        id = IDManager(file_path="/home/admin/certs/ids.json")
        most_recent = id.get_latest_id()
        if self.validate_id_exists(most_recent):
            return most_recent
        return None

    def validate_id_exists(self, id):
        keys = self.to_dict()
        for key_type in keys:
            for key_name in keys[key_type]:
                key_data = keys[key_type][key_name]
                if key_data['ID'] == id:
                    return True
        return False

    def delete_all_objects(self):
        keys = self.to_dict()
        self.delete_objects(keys)

    def delete_ldev_objects(self):
        self.delete_objects_by_type("ldev")


    def delete_idev_objects(self):
        self.delete_objects_by_type("idev")

    def delete_objects_by_type(self, type):
        keys = self.to_dict()
        filtered_dict = {k1: {k2: v2 for k2, v2 in v1.items() if k2.startswith(type)} for k1, v1 in keys.items()}
        self.delete_objects(filtered_dict)

    def delete_objects(self, keys):
        for key_type in keys:
            type = "privkey" if key_type == "private_keys" else "pubkey" if key_type == "public_keys" else "cert"
            for key_name in keys[key_type]:
                key_data = keys[key_type][key_name]
                self.delete_hsm_object(type, key_data['ID'])


    def delete_key_by_label(self, key_label):
        self.filter_id_by_label(key_label)

    def delete_hsm_object(self, type, key_id):
        command = [
            "./bash/delete_keys_on_hsm.sh",
            f'--key_type={type}',
            f'--id={key_id}',
            f'--pin={self.pin}',

        ]

        print("Executing command:", " ".join(command))
        subprocess.call(command)






def main():
    print("--- Print Objects ---")
    hsm_objects = HsmObjects(
        slot_num=0,
        pin='1234'
    )
    print(hsm_objects.to_dict())
    print(hsm_objects.to_json())
    #print(hsm_objects.to_dict())
    print("--- Get key ID ---")
    print("ID: {}".format(hsm_objects.filter_id_by_label(key_label="my_rsa_pvt_86599")))

def most_recent_ldev():
    hsm_objects = HsmObjects(
        slot_num=0,
        pin='1234'
    )
    most_recent = hsm_objects.get_most_recent_ldev_id()
    print(most_recent)

def delete_idev():
    hsm_objects = HsmObjects(
        slot_num=0,
        pin='1234'
    )
    hsm_objects.delete_idev_objects()

def get_actual_idev():
    hsm_objects = HsmObjects(
        slot_num=0,
        pin='1234'
    )
    print(hsm_objects.get_actual_idev_id())

if __name__ == "__main__":
    most_recent_ldev()