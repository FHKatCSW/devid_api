# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

import json

class Datas():

    id           = db.Column(db.Integer()   , primary_key=True)
    data         = db.Column(db.String(256) , nullable=False)
    date_created = db.Column(db.DateTime()  , default=datetime.utcnow)

    def __repr__(self):
        return str( self.id ) 

    def update_data(self, new_data):
        self.data = new_data

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['data'] = self.data

        return cls_dict

    def toJSON(self):

        return self.toDICT()
