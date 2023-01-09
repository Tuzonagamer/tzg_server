from app.application.model import PriceDAO
from app.application.controlers.enum.Enum import Enum
import datetime

def _get_date():
	return datetime.datetime.now()

class PriceCT:
    def __init__(self):
        self.manager = PriceDAO
        self.enum = Enum()

    def build(self, discriminator, name, value):
        return PriceDAO(
            creation_date=_get_date(),
            modification_date=None,
            enum=discriminator,
            name=name,
            value=value,
            deleted_at=None
        )

    def getAll(self):
        
        report = []
        for obj in self.manager.getAll():
            row = {}
            for key in obj.keys():
                if(key != "_sa_instance_state"):
                    row[key] = str(obj[key])
            report.append(row)
        
        obj = self.enum.validatePersistemObject("table","price", "price" )
        
        entity = { 
            "discriminator":obj.discriminator,
            "text":obj.label,
            "value":obj.field
        }
        return {"data":report, "headers":self.enum.getHeadersByDiscriminator("price", PriceDAO), "entity":entity}

    
    def create(self, obj):
        return self.manager.create(obj) 
        
    def add(self, descriminator, code, value):
        return self.create(self.build(descriminator, code, value))