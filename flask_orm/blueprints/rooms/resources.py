import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from db import db, Room


rooms_structure = {'number': fields.Integer,
                   'level': fields.String,
                   'status': fields.String,
                   'price': fields.Integer,
                   'tenant_id': fields.Integer}

parser = reqparse.RequestParser()
parser.add_argument('number', type=int)
parser.add_argument('status', type=str)


class RoomsResource(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        return Room.query.all()

    @marshal_with(rooms_structure)
    def post(self):
        body = json.loads(request.data)
        room = Room(**body)
        db.session.add(room)
        db.session.commit()

    @marshal_with(rooms_structure)
    def put(self, value):
        body = json.loads(request.data)
        room = Room.query.get(value)
        room.status = body.get('status')
        db.session.commit()
        return Room.query.all()

    @marshal_with(rooms_structure)
    def delete(self, value):
        room = Room.query.get(value)
        db.session.delete(room)
        db.session.commit()
        return Room.query.all()
