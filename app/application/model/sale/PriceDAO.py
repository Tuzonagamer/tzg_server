from app.application.model import db
from sqlalchemy import Column, Integer, DateTime
import datetime

def _get_date():
	return datetime.datetime.now()

def getObject(obj):   
        return db.session.query(PriceDAO).filter_by(enum = obj.enum, name=obj.name, value=obj.value).first()

class PriceDAO(db.Model):
    __tablename__ = 'price'
    """model entity orker
    :autor: jajoya
    :date: 2022-09-22
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    modification_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    enum = db.Column(db.String) # unique
    name = db.Column(db.String)
    value = db.Column(db.String)
    
    deleted_at = db.Column(db.Date, onupdate=_get_date)

    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [price.__dict__ for price in db.session.query(PriceDAO).all()]

    def get(id):
	    return db.session.query(PriceDAO).filter_by(id = id).first().__dict__	 

    
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