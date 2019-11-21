from flask_restful import Api
from flask import Blueprint

from blueprints.rooms.resources import RoomsResource

rooms_blueprint = Blueprint("rooms", __name__)
rooms_api = Api(rooms_blueprint)

rooms_api.add_resource(RoomsResource, '/rooms')