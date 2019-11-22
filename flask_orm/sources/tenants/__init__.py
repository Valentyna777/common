from flask_restful import Api
from flask import Blueprint

from sources.tenants.resources import TenantsResource

tenants_blueprint = Blueprint("tenants", __name__)
tenants_api = Api(tenants_blueprint)

tenants_api.add_resource(TenantsResource, '/tenants', '/tenants/<value>')