from app.application.model import db
def _get_date():
	return datetime.datetime.now()

class WorkerDAO(db.Model):
    __tablename__ = 'worker'
    """model entity orker
    :autor: jajoya
    :date: 2022-09-22
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    name = db.Column(db.String)
    ip = db.Column(db.String)

    deleted_at = db.Column(db.Date, onupdate=_get_date)

	

    def get(id):
        return db.session.query(WorkerDAO).filter_by(id=id).first()


    def getAll():
        return db.session.query(WorkerDAO).all()

    def getByName(name):
        print(name)
        return db.session.query(WorkerDAO).filter_by(name=name).first()

