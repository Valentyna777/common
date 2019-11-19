from flask import Flask, Blueprint, request
from flask_restful import Resource, Api, fields, reqparse, marshal_with

app = Flask(__name__)
staff = Blueprint('staff', __name__)
api = Api(staff)


class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff_structure = {'name': fields.String,
                   'passport_id': fields.String,
                   'position': fields.String,
                   'salary': fields.Integer}

staff_list = [Staff('Alex', 'ID123', 'driver', 800), Staff('Melisa',
              'ID124', 'waiter', 750), Staff('Jack', 'ID125', 'dancer', 780)]

parser = reqparse.RequestParser()
parser.add_argument('passport_id', type=str)


class StaffR(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            for st in staff_list:
                if st.passport_id == args['passport_id']:
                    return st
        return staff_list

    @marshal_with(staff_structure)
    def patch(self):
        content = request.json
        passport_id = content.get('passport_id')
        for st in staff_list:
            if st.passport_id == passport_id:
                staff_list.remove(st)
                staff_list.append(Staff(content['name'], content['passport_id'], content['position'], content['salary']))
                return staff_list

    def delete(self, passport_id):
        for st in staff_list:
            if st.passport_id == passport_id:
                staff_list.remove(st)
                return 'Staff is deleted'
        return "Person does not exist"


api.add_resource(StaffR, '/staff', '/staff/<passport_id>')
