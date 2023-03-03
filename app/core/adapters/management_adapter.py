from marshmallow import ValidationError

from . import AbstractBaseAdapter


class ManagementAdapter(AbstractBaseAdapter):
    """Base adapater for api contract"""

    def __init__(self, usecase, schema):
        self.usecase = usecase()
        self.schema = schema

    def __repr__(self):
        return "{}(entity, usecase)".format(self.__class__.__name__)