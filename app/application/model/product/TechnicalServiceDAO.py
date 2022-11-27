from app.application.model import db

def _get_date():
	return datetime.datetime.now()

class TechnicalServiceDAO(db.Model):
    __tablename__ = 'technical_service'
    """model entity technical_service
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    action_description = db.Column(db.String)
    general_description = db.Column(db.String)
    controlTechnicalServiceDAO_id = db.Column(db.Integer, db.ForeignKey('control_technical_service.id'))
    
    deleted_at = db.Column(db.Date, onupdate=_get_date) 

        
    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [technical.__dict__ for technical in db.session.query(TechnicalServiceDAO).all()]
       
    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)    

        
    def get(id):
	    return db.session.query(TechnicalServiceDAO).filter_by(id = id).first()
    