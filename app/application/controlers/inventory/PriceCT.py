from app.application.model import PriceDAO
from app.application.model import PriceInventoryDAO
from app.application.controlers.enum.Enum import Enum
import datetime

def _get_date():
	return datetime.datetime.now()

class PriceCT:
    def __init__(self):
        self.manager = PriceDAO
        self.managerPriceInventory = PriceInventoryDAO
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

        
    def build_inventory_add(self, inventory, price, description):
        

        inventory = inventory[0]

        return PriceInventoryDAO(
            creation_date=_get_date(),
            modification_date=None,
            inventory_id =  inventory["id"],
            price_id = price["id"],
            version_description = price["value"],
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
        
    def add(self, descriminator, code, value, price, description):
        row = {}
        obj = self.create(self.build(descriminator, code, value))
        for key in obj[0].keys():
            if(key != "_sa_instance_state"):
                row[key] = str(obj[0][key])
        return row, obj[1] 
    
    def assiggendValuePrice(self, price, inventory, description ):
        row = {}
        obj = self.managerPriceInventory.create(self.build_inventory_add(inventory, price, description))
        for key in obj[0].keys():
            if(key != "_sa_instance_state"):
                row[key] = str(obj[0][key])
        return row, obj[1] 