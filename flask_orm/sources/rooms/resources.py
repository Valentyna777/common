import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from db import db, Room


rooms_structure = {'number': fields.Integer,
                   'level': fields.String,
                   'status': fields.String,
                   'price': fields.Integer,
                   'tenant_id': fields.Integer}


class RoomsResource(Resource):
    @marshal_with(rooms_structure)
    def get(self, value=None):
        if value:
            return Room.query.get(value)
        elif request.args.get('status'):
            return Room.query.filter_by(status=request.args['status']).all()
        return Room.query.all()

    @marshal_with(rooms_structure)
    def post(self):
        body = json.loads(request.data)
        room = Room(**body)
        db.session.add(room)
        db.session.commit()
        return Room.query.all()

    @marshal_with(rooms_structure)
    def patch(self, value):
        body = json.loads(request.data)
        room = Room.query.get(value)
        room.status = body.get('status')
        room.price = body.get('price')
        room.tenant_id = body.get('tenant_id')
        db.session.commit()
        return Room.query.all()

    @marshal_with(rooms_structure)
    def delete(self, value):
        room = Room.query.get(value)
        db.session.delete(room)
        db.session.commit()
        return Room.query.all()
