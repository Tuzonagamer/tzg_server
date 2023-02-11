from app.application.model.enum.PersitemEnum import PersitemEnum
import datetime
def _get_date():
	return datetime.datetime.now()

class Enum():
    def __init__(self):
        self.manager = PersitemEnum
    
    def getHeadersByDiscriminator(self, discriminator, entity):
        enums = []        

        listobj =  self.manager.findPersistemByDiscriminator(discriminator)       
        #print(" \n {} \n {}".format(listobj, discriminator))
        for obj in listobj:
            # print({"text":obj.label, "value":obj.field})
            if(obj.show):
                enums.append({"text":obj.label, "value":obj.field})

        return self.validatePersistem(enums, entity, discriminator)

    def validatePersistem(self, enums, entity, discriminator):
        if(len(enums) <= 1):
            keys = self.manager.getColumnsByEntityName(entity)
            print(keys)
            for key in keys:
                obj = self.create(discriminator, key, key )
                enums.append({"text":obj.label, "value":obj.field})
        return enums

    def validatePersistemObject(self, discriminator, field, label ):
        object = None
        object = self.manager.getObjectByValues(discriminator, field, label)
        if(object == None):
            object = self.create(discriminator, field, label )
        print(object)    
        return object

    def create(self, discriminator_, field_, label_):
        obj = PersitemEnum(creation_date=_get_date(),
        modification_date=None, 
        discriminator=discriminator_,
        field=field_,
        label=label_,
        show=True,
        deleted_at=None)
        return self.manager.create(obj)
    
        
    def getAll():
        #return db.session.query(InventoryDAO).all()
        return [inventory.__dict__ for inventory in db.session.query(InventoryDAO).all()]
