from datetime import datetime
from product import db

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.String(11), nullable=False, unique=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price  = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    