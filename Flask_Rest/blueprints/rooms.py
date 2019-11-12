from flask import Flask, Blueprint, request
from flask_restful import Resource, Api, fields, reqparse, marshal_with

app = Flask(__name__)
rooms = Blueprint('rooms', __name__)
api = Api(rooms)


class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms_structure = {'number': fields.Integer,
                   'level': fields.String,
                   'status': fields.String,
                   'price': fields.Integer}

rooms_list = [Room(101, 'second', 'closed', 250), Room(102, 'second', 'available', 280), Room(202, 'third', 'available', 230)]

parser = reqparse.RequestParser()
parser.add_argument('number', type=int, help='Number should be integer')
parser.add_argument('status', type=str, help='Status should be string: "available" or"closed"')


class Rooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = parser.parse_args()
        if args["number"]:
            for room in rooms_list:
                if room.number == args['number']:
                    return room
        elif args["status"]:
            status_list = []
            for room in rooms_list:
                if room.status == args['status']:
                    status_list.append(room)
                    return status_list
        return rooms_list

    @marshal_with(rooms_structure)
    def post(self):
        number = request.args.get('number')
        level = request.args.get('level')
        status = request.args.get('status')
        price = request.args.get('price')
        rooms_list.append(Room(number, level, status, price))
        return "ok"

    @marshal_with(rooms_structure)
    def patch(self):
        number = request.args.get('number')
        level = request.args.get('level')
        status = request.args.get('status')
        price = request.args.get('price')
        for room in rooms_list:
            if room.number == number:
                rooms_list.remove(room)
        rooms_list.append(Room(number, level, status, price))
        return "Ok"

    @marshal_with(rooms_structure)
    def delete(self, number):
        for room in rooms_list:
            if room.number == int(number):
                rooms_list.remove(room)
                return 'Ok'
        return "Room does not exist"


api.add_resource(Rooms, '/rooms', '/rooms/<number>')
