from app import db


class Country(db.Model):

    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    min_lon = db.Column(db.Float, nullable=False)
    max_lon = db.Column(db.Float, nullable=False)
    min_lat = db.Column(db.Float, nullable=False)
    max_lat = db.Column(db.Float, nullable=False)

    def __init__(self, name, min_lon, max_lon, min_lat, max_lat):
        self.name = name
        self.min_lon = min_lon
        self.max_lon = max_lon
        self.min_lat = min_lat
        self.max_lat = max_lat

    def __repr__(self):
        return '<country {}>'.format(self.name)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    chat_id = db.Column(db.String, nullable=False)
    win = db.Column(db.Integer, default=0)
    lose = db.Column(db.Integer, default=0)
    state = db.Column(db.Integer, default=0)
    last_country = db.Column(db.String, nullable=True)

    def __init__(self, name, chat_id):
        self.name = name
        self.chat_id = chat_id

    def __repr__(self):
        return '<user {}>'.format(self.name)



