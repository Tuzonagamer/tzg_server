from app.application.model import db
def _get_date():
	return datetime.datetime.now()

class PriceDAO(db.Model):
    __tablename__ = 'price'
    """model entity orker
    :autor: jajoya
    :date: 2022-09-22
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    enum = db.Column(db.String)
    name = db.Column(db.String)
    value = db.Column(db.String)
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)