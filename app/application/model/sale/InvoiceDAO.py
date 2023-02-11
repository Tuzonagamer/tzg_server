from app.application.model import db
def _get_date():
	return datetime.datetime.now()

class InvoiceDAO(db.Model):
    __tablename__ = 'invoice'
    """model entity orker
    :autor: jajoya
    :date: 2022-09-22
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    sale_at = db.Column(db.Date, onupdate=_get_date)
    control_device_id =  db.Column(db.Integer, db.ForeignKey('control_device.id'))
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)

	

    def get(id):
        pass#return db.session.query(WorkerDAO).filter_by(id=id).first()


    def getAll():
        pass#return db.session.query(WorkerDAO).all()

    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj)            
