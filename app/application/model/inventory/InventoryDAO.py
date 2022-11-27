from app.application.model import db

def _get_date():
	return datetime.datetime.now()

class InventoryDAO(db.Model):
    __tablename__ = 'inventory'
    """model entity device
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    name = db.Column(db.String)
    serial_manual = db.Column(db.String) # is unique 
    description = db.Column(db.String)
    qr_file_path = db.Column(db.String)
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)

    
    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [inventory.__dict__ for inventory in db.session.query(InventoryDAO).all()]

    def getObjectByS(serial):   
        return db.session.query(InventoryDAO).filter_by(serial_manual = serial).first()

    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)    

        
    def get(id):
	    return db.session.query(InventoryDAO).filter_by(id = id).first()
    