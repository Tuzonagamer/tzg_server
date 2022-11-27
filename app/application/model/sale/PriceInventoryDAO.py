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
    version_description = db.Column(db.String)
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)

    
    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [price.__dict__ for price in db.session.query(PriceInventoryDAO).all()]
       
    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)    

        
    def get(id):
	    return db.session.query(PriceInventoryDAO).filter_by(id = id).first()
    