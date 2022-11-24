from app.application.model import db

def _get_date():
	return datetime.datetime.now()

class PriceInventoryDAO(db.Model):
    __tablename__ = 'price_inventory'
    """model entity device
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)

    inventory_id =  db.Column(db.Integer, db.ForeignKey('inventory.id'))
    price_id =  db.Column(db.Integer, db.ForeignKey('price.id'))
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)