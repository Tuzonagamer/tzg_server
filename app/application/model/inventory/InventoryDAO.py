from app.application.model import db

def getObject(obj):   
        return db.session.query(InventoryDAO).filter_by(name = obj.name, serial_manual=obj.serial_manual, description=obj.description, qr_file_path=obj.qr_file_path).first()

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
        
        ans_obj = {"message":None, "act":None}
        
        if(getObject(obj) == None): 
            db.session.add(obj)
            db.session.commit()
            ans_obj["message"] = "Registro Exitoso"
            ans_obj["act"] = True
        else:
            ans_obj["message"] = "Registro Existente"
            ans_obj["act"] = False 
            
        return getObject(obj).__dict__ , ans_obj
        
    def get(id):
	    return db.session.query(InventoryDAO).filter_by(id = id).first()
    