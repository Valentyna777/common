from flask import Flask

from blueprints.staff import staff_blueprint
from blueprints.tenants import tenants_blueprint
from config import *
from blueprints.rooms import rooms_blueprint
from db import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    db.init_app(app)
    app.register_blueprint(rooms_blueprint)
    app.register_blueprint(staff_blueprint)
    app.register_blueprint(tenants_blueprint)
    db.create_all(app=app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)