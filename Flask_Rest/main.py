from flask import Flask
from flask_restful import Api, Resource

from blueprints.rooms import rooms
from blueprints.staff import staff
from blueprints.tenants import tenants
from config import run_config

app = Flask(__name__)
api = Api(app)
app.config.from_object(run_config())
app.register_blueprint(rooms)
app.register_blueprint(tenants)
app.register_blueprint(staff)


if __name__ == '__main__':
    app.run(debug=True)