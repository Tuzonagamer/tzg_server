from app.application.model.enum.PersitemEnum import PersitemEnum
import datetime
def _get_date():
	return datetime.datetime.now()

class Enum():
    def __init__(self):
        self.manager = PersitemEnum
    
    def getHeadersByDiscriminator(self, discriminator, entity):
        enums = []        
        for obj in self.manager.findPersistemByDiscriminator(discriminator):
            enums.append({"text":obj.label, "value":obj.field})

        return self.validatePersistem(enums, entity, discriminator)

    def validatePersistem(self, enums, entity, discriminator):
        if(len(enums) == 0):
            keys = self.manager.getColumnsByEntityName(entity)
            print(keys)
            for key in keys:
                enums.append(self.create(discriminator, key, key ))
        return enums

    def create(self, discriminator_, field_, label_):
        obj = PersitemEnum(creation_date=_get_date(),
        modification_date=None, 
        discriminator=discriminator_,
        field=field_,
        label=label_,
        show=True,
        deleted_at=None)
        return self.manager.create(obj)