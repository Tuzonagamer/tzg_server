from app.application.model import db
from sqlalchemy.inspection import inspect


def _get_date():
	return datetime.datetime.now()

def getObject(object):
    return db.session.query(PersitemEnum).filter_by(
        creation_date=object.creation_date,
        modification_date=object.modification_date, 
        discriminator=object.discriminator,
        field=object.field,
        label=object.label,
        show=object.show,
        deleted_at=object.deleted_at
        ).first()


class PersitemEnum(db.Model):
    __tablename__ = 'persistemenum'
    """model entity persistemenum
    :autor: jajoya
    :date: 2022-11-19
    """
    id = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date, onupdate=_get_date)
    modification_date = db.Column(db.Date, onupdate=_get_date)

    discriminator = db.Column(db.String)
    field = db.Column(db.String)
    label = db.Column(db.String)
    show = db.Column(db.Boolean)

    deleted_at = db.Column(db.Date, onupdate=_get_date)
   
    def create(obj):
        db.session.add(obj)
        db.session.commit()
        return getObject(obj) 

    def findPersistemByDiscriminator(discriminator):
        return db.session.query(PersitemEnum).filter(discriminator == discriminator).all()

    def getColumnsByEntityName(obj):
        return [column.name for column in inspect(obj).c]

