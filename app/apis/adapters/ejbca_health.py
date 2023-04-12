import json
import requests
from requests_pkcs12 import Pkcs12Adapter
from app.apis.adapters import logger



class EjbcaHealth:
    def __init__(self, base_url, p12_file, p12_pass):
        self.logger = logger.get_logger("CertRequest")

        self.base_url = base_url
        self.p12_file = p12_file
        self.p12_pass = p12_pass



    def health_status(self):
        # Create JSON payload
        try:
            url = f'https://{self.base_url}/ejbca/ejbca-rest-api/v1/ca/status'

            # Send request
            session = requests.Session()
            session.mount(url, Pkcs12Adapter(max_retries=3, pkcs12_filename=self.p12_file, pkcs12_password=self.p12_pass))
            response = session.get(
                url=url,
                headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
                verify=False
            )
            response.raise_for_status()  # raise an HTTPError if status code is >= 400
            response = json.loads(response.text)
            if response['status'] == "OK":
                self.logger.info("-EJBCA up and running ✅")
            else:
                self.logger.info("-EJBCA down ❌")

            #self.logger.info("--Response: {}".format(response))
        except requests.exceptions.HTTPError as err:
            self.logger.error("HTTP error occurred:", err)
        except requests.exceptions.RequestException as err:
            self.logger.error("An error occurred:", err)
        except (json.JSONDecodeError, OSError, KeyError) as e:
            self.logger.error(f"Error requesting certificate: {str(e)}")


if __name__ == "__main__":
    health = EjbcaHealth(
        base_url='campuspki.germanywestcentral.cloudapp.azure.com',
        p12_file='/home/admin/fhk_hmi_setup_v3.p12',
        p12_pass='foo123',
    )
    health.health_status()