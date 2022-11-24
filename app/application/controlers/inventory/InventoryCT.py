from app.application.model import InventoryDAO
from app.application.controlers.enum.Enum import Enum
class InventoryCT():
    def __init__(self):
        self.manager = InventoryDAO
        self.enum = Enum()
    
    def getAll(self):
        report = []
        for obj in self.manager.getAll():
            row = {}
            for key in obj.keys():
                if(key != "_sa_instance_state"):
                    row[key] = str(obj[key])
            report.append(row)
        
        return {"data":report, "headers":self.enum.getHeadersByDiscriminator("inventory", InventoryDAO)}
        