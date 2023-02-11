from app.application.model import db

def _get_date():
	return datetime.datetime.now()

def getObject(obj):   
    return db.session.query(PriceInventoryDAO).filter_by(inventory_id = obj.inventory_id, price_id=obj.price_id, version_description=obj.version_description).first()

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
        object = getObject(obj)
        ans_obj = {"message":None, "act":None}
        if(object == None):
            db.session.add(obj)
            db.session.commit()
            ans_obj["message"] = "Registro Exitoso"
            ans_obj["act"] = True
            object = getObject(obj).__dict__
        else:
            ans_obj["message"] = "Registro Existente"
            ans_obj["act"] = False 
            object = object.__dict__
        
        return object, ans_obj    
        
    def get(id):
	    return db.session.query(PriceInventoryDAO).filter_by(id = id).first()
    