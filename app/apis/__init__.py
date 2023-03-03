from .management_interface import api as mgmt_interface
from .Idev_service_interface import api as idev_interface
from .Ldev_service_interface import api as ldev_interface
from .setup_interface import api as setup_interface



from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="IEEE 802.1 AR API",
    version="0.1",
    description="Interfaces to communicate with an entity, setup a device and manage DevIDs according to IEEE 802.1 AR"
)

api.add_namespace(setup_interface, path="/setup")
api.add_namespace(mgmt_interface, path="/mgmt")
api.add_namespace(idev_interface, path="/idev")
api.add_namespace(ldev_interface, path="/ldev")