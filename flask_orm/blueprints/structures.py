from flask_restful import fields

rooms_structure = {'number': fields.Integer,
                   'level': fields.String,
                   'status': fields.String,
                   'price': fields.Integer,
                   'tenant_id': fields.Integer}

staff_structure = {'passport_id': fields.String,
                   'name': fields.String,
                   'position': fields.String,
                   'salary': fields.Integer}

tenants_structure = {'passport_id': fields.String,
                     'name': fields.String,
                     'age': fields.Integer,
                     'sex': fields.String,
                     'city': fields.String,
                     'address': fields.String}

