from app.application.model import db

def _get_date():
	return datetime.datetime.now()

class ControlerDeviceDAO(db.Model):
    __tablename__ = 'control_device'
    """model entity control_device
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    entry_at = db.Column(db.Date, onupdate=_get_date)
    delivery_at = db.Column(db.Date, onupdate=_get_date)
    
    action_description = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    device_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))    
    state = db.Column(db.String)

    deleted_at = db.Column(db.Date, onupdate=_get_date)


    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [inventory.__dict__ for inventory in db.session.query(InventoryDAO).all()]
       
    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)    

        
    def get(id):
	    return db.session.query(InventoryDAO).filter_by(id = id).first()
    