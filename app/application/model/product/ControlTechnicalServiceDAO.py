from app.application.model import db

def _get_date():
	return datetime.datetime.now()

class ControlTechnicalServiceDAO(db.Model):
    __tablename__ = 'control_technical_service'
    """model entity control_technical_service
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)
    
    control_device_id = db.Column(db.Integer, db.ForeignKey('control_device.id'))
    #dado que se podria incluir el inventario para calcular futuros valores desde esta entidad
    state = db.Column(db.String)
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)