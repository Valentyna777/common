from flask import Flask

#from blueprints import tenants, staff, rooms
from config import *


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    db.init_app(app)
    db.create_all()
    with app.app_context():
        app.register_blueprint(rooms)
        app.register_blueprint(staff)
        app.register_blueprint(tenants)
        return app


def create_db(app):
    return SQLAlchemy(app)


app = create_app()
db = create_db(app)

if __name__ == "__main__":
    create_app.run(debug=True)