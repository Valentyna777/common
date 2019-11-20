from main import db


class Room(db.Model):
    __tablename__ = 'rooms'
    number = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tenant_id = db.Column(db.Integer, nullable=False)


class Tenant(db.Model):
    __tablename__ = 'tenants'
    passport_id = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)


class Staff(db.Model):
    __tablename__ = 'staff'
    passport_id = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)





