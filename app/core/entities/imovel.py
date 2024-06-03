from app import db
from sqlalchemy_serializer import SerializerMixin

class Imovel(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    condo = db.Column(db.Float)
    size = db.Column(db.Integer)
    rooms = db.Column(db.Integer)
    toilets = db.Column(db.Integer)
    suites = db.Column(db.Integer)
    parking = db.Column(db.Boolean)
    elevator = db.Column(db.Boolean)
    furnished = db.Column(db.Boolean)
    swimming_pool = db.Column(db.Boolean)
    new = db.Column(db.Boolean)
    district = db.Column(db.String(255))
    negotiation_type = db.Column(db.String(50))
    property_type = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f'<Imovel {self.id}>'

    serialize_only = (
        'id',
        'price',
        'condo',
        'size',
        'rooms',
        'toilets',
        'suites',
        'parking',
        'elevator',
        'furnished',
        'swimming_pool',
        'new',
        'district',
        'negotiation_type',
        'property_type',
        'latitude',
        'longitude'
    )