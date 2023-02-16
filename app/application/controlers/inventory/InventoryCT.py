from app.application.model import InventoryDAO
from app.application.controlers.enum.Enum import Enum
from app.application.model import PriceDAO
from app.application.model import PriceInventoryDAO



import datetime

def _get_date():
	return datetime.datetime.now()

class InventoryCT():
    def __init__(self):
        self.manager = InventoryDAO
        self.enum = Enum()

    def build(self, name_, serial_, description_, qr_file_path_):
        return InventoryDAO(
            creation_date=_get_date(),
            modification_date=None,
            name=name_,
            serial_manual=serial_,
            description=description_,
            qr_file_path=qr_file_path_,
            deleted_at=None
        )

    def create(self, obj):
        return self.manager.create(obj)    
    
    def getAll(self):
        report = []
        for obj in self.manager.getAll():
            row = {}
            for key in obj.keys():
                if(key != "_sa_instance_state"):
                    row[key] = str(obj[key])
            report.append(row)
        
        obj = self.enum.validatePersistemObject("table","inventory", "inventory" )
        
        entity = { 
            "discriminator":obj.discriminator,
            "text":obj.label,
            "value":obj.field
        }
        return {"data":report, "headers":self.enum.getHeadersByDiscriminator("inventory", InventoryDAO), "entity":entity}
    
    # add inventory only
    def add(self, object):
        object = self.create(self.build(object["NAME"], object["SERIAL"], object["DESCRIPTION"], object["QRPATH"]))
        row = {}
        for key in object[0].keys():
            if(key != "_sa_instance_state"):
                row[key] = str(object[0][key])
        return row, object[1]

    def getInventoryDetaily(self, id):
        object = {}
        arr = self.manager.getDetail(id, PriceDAO, PriceInventoryDAO)
        object = self.enum.joinToObj(arr)
        
        return object, None        