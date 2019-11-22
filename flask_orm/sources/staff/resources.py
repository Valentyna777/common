import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from db import db, Staff


staff_structure = {'passport_id': fields.String,
                   'name': fields.String,
                   'position': fields.String,
                   'salary': fields.Integer}

parser = reqparse.RequestParser()
parser.add_argument('passport_id, type=str')


class StaffResource(Resource):
    @marshal_with(staff_structure)
    def get(self):
        if request.args.get('passport_id'):
            return Staff.query.filter_by(passport_id=request.args['passport_id']).all()
        return Staff.query.all()

    @marshal_with(staff_structure)
    def post(self):
        body = json.loads(request.data)
        staff = Staff(**body)
        db.session.add(staff)
        db.session.commit()
        return Staff.query.all()

    @marshal_with(staff_structure)
    def put(self, value):
        body = json.loads(request.data)
        staff = Staff.query.get(value)
        staff.salary = body.get('salary')
        staff.salary = body.get('position')
        db.session.commit()
        return Staff.query.all()

    @marshal_with(staff_structure)
    def delete(self, value):
        staff = Staff.query.get(value)
        db.session.delete(staff)
        db.session.commit()
        return Staff.query.all()
