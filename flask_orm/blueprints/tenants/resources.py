import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from db import db, Tenant


tenants_structure = {'passport_id': fields.String,
                     'name': fields.String,
                     'age': fields.Integer,
                     'sex': fields.String,
                     'city': fields.String,
                     'address': fields.String}

parser = reqparse.RequestParser()
parser.add_argument('passport_id, type=str')


class TenantsResource(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        return Tenant.query.all()

    @marshal_with(tenants_structure)
    def post(self):
        body = json.loads(request.data)
        tenant = Tenant(**body)
        db.session.add(tenant)
        db.session.commit()

    @marshal_with(tenants_structure)
    def put(self, value):
        body = json.loads(request.data)
        tenant = Tenant.query.get(value)
        tenant.address = body.get('address')
        db.session.commit()
        return Tenant.query.all()

    @marshal_with(tenants_structure)
    def delete(self, value):
        tenant = Tenant.query.get(value)
        db.session.delete(tenant)
        db.session.commit()
        return Tenant.query.all()
