from app.application.model import db

def _get_date():
	return datetime.datetime.now()


class ClientDAO(db.Model):
    __tablename__ = 'client'
    """model entity client
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    name = db.Column(db.String)
    doc = db.Column(db.String)
    tipo_doc = db.Column(db.String)
    address = db.Column(db.String)
    telephone = db.Column(db.String)

    deleted_at = db.Column(db.Date, onupdate=_get_date)
    
    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [inventory.__dict__ for inventory in db.session.query(ClientDAO).all()]
       
    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)    

        
    def get(id):
	    return db.session.query(ClientDAO).filter_by(id = id).first()
    
