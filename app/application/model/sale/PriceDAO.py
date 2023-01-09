from app.application.model import db
def _get_date():
	return datetime.datetime.now()

def getObject(obj):   
        return db.session.query(InventoryDAO).filter_by(enum = obj.enum, name=obj.name, value=obj.value).first()

class PriceDAO(db.Model):
    __tablename__ = 'price'
    """model entity orker
    :autor: jajoya
    :date: 2022-09-22
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    enum = db.Column(db.String) # unique
    name = db.Column(db.String)
    value = db.Column(db.String)
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)

    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [price.__dict__ for price in db.session.query(PriceDAO).all()]

    def get(id):
	    return db.session.query(PriceDAO).filter_by(id = id).first()	 

    
    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)    
