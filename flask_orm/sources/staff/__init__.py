from flask_restful import Api
from flask import Blueprint

from sources.staff.resources import StaffResource

staff_blueprint = Blueprint("staff", __name__)
staff_api = Api(staff_blueprint)

staff_api.add_resource(StaffResource, '/staff', '/staff/<value>')
