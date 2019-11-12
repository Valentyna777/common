from flask import Flask, Blueprint, request
from flask_restful import Resource, Api, fields, reqparse, marshal_with

app = Flask(__name__)
tenants = Blueprint('tenants', __name__)
api = Api(tenants)


class Tenant:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


address_structure = {'city': fields.String,
                     'street': fields.String, }

tenants_structure = {'name': fields.String,
                     'passport_id': fields.String,
                     'age': fields.Integer,
                     'sex': fields.String,
                     'address': fields.Nested(address_structure),
                     'room_number': fields.Integer}

tenants_list = [Tenant('Bro', 'ID234', 26, 'male', {'city': 'Kharkiv', 'street': 'Tsentralna, 8'}, 24),
                Tenant('Mariia', 'ID235', 25, 'female', {'city': 'Chernivtsi', 'street': 'Kyivska, 31'}, 12),
                Tenant('Stasik', 'ID236', 29, 'male', {'city': 'Kyiv', 'street': 'Zhulianska, 18'}, 10)]


parser = reqparse.RequestParser()
parser.add_argument('passport_id', type=str)


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            for tenant in tenants_list:
                if tenant.passport_id == args['passport_id']:
                    return tenant
        return tenants_list

    @marshal_with(tenants_structure)
    def patch(self):
        name = request.args.get('name')
        passport_id = request.args.get('passport_id')
        age = request.args.get('age')
        sex = request.args.get('sex')
        address = request.args.get('address')
        room_number = request.args.get('room_number')
        for tenant in tenants_list:
            if tenant.passport_id == passport_id:
                tenants_list.remove(tenant)
        tenants_list.append(Tenant(name, passport_id, age, sex, address, room_number))
        return 'ok'

    @marshal_with(tenants_structure)
    def delete(self, passport_id):
        for tenant in tenants_list:
            if tenant.passport_id == passport_id:
                tenants_list.remove(tenant)
                return 'Ok'
        return "Person does not exist"


api.add_resource(Tenants, '/tenants', '/tenants/<passport_id>')
