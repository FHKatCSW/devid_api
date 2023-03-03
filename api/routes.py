# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request
from flask_restx import Api, Resource, fields

from api.models import Datas

rest_api = Api(version="1.0", title="IDevID API")

"""
API Interface:
   
   - /datas
       - GET: return all items
       - POST: create a new item
   
   - /datas/:id
       - GET    : get item
       - PUT    : update item
       - DELETE : delete item
"""

"""
Flask-RestX models Request & Response DATA
"""

# Used to validate input data for creation
create_model = rest_api.model('CreateModel', {"data": fields.String(required=True, min_length=1, max_length=255)})

# Used to validate input data for update
update_model = rest_api.model('UpdateModel', {"data": fields.String(required=True, min_length=1, max_length=255)})

"""
    Flask-Restx routes
"""

@rest_api.route('/api/datas')
class Items(Resource):

    """
       Return all items
    """
    def get(self):

        items = Datas.query.all()
        
        return {"success" : True,
                "msg"     : "Items found"}, 200

    """
       Create new item
    """
    @rest_api.expect(create_model, validate=True)
    def post(self):

        return {"success": True,
                "msg"    : "Item successfully created"}, 200

@rest_api.route('/api/datas/<int:id>')
class ItemManager(Resource):

    """
       Return Item
    """
    def get(self, id):

        return {"success" : True,
                "msg"     : "Successfully return item"}, 200

    """
       Update Item
    """
    @rest_api.expect(update_model, validate=True)
    def put(self, id):
        return {"success" : True,
                "msg"     : "Item  successfully updated"}, 200

    """
       Delete Item
    """
    def delete(self, id):

        return {"success" : True,
                "msg"     : "Item successfully deleted"}, 200
