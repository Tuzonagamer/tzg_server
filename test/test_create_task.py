from test import app, client, db, ctx
from app.application.model.worker.WorkerDAO import WorkerDAO
from app.application.model.metadata.MetadataImageDAO import MetadataImageDAO
from app.application.model.task.TaskDAO import TaskDAO
from app.application.controlers.tools.PersistenValue import PersistenValue
from app.application.controlers.task.TaskCT import TaskCT

from .tools.utilities import createImage
from .tools.utilities import createWorker

import pytest

def keysObjectTask(taskObject):
    keys = ["finca",  "bloque", "nave",  "lado", "cama", "fecha", "hora", "image_name", "image_id",   "task_id", "worker_id"]

    verdict = True
    for key in taskObject.keys():
        if(key not in keys):
            verdict = False
    return verdict
    
def test_taskcontroler(ctx):

    # poblate db metadata
    createImage("12", "09", "image_1")
    createImage("11", "08", "image_2")
    createImage("13", "07", "image_3")
    createImage("14", "06", "image_3")

    # poblate db workers
    createWorker("test_worker", "192.168.0.1")

    createWorker("test_worker_1", "localhost")
    createWorker("test_worker_2", "localhost")

    taskct = TaskCT()

    obj = taskct.getNewTask("test_worker")
    assert keysObjectTask(obj)
    
    obj = taskct.getNewTask("test_worker_1")
    assert keysObjectTask(obj)
    
    obj = taskct.getNewTask("test_worker_2")
    assert keysObjectTask(obj)

    with pytest.raises(Exception) as e:
        obj = taskct.getNewTask("test_worker_3")
    #print("here exception ",e.value)

    assert str(e.value) == "No se encontro un worker asociado al nombre {} \n porfavor comuniquese con el administrador".format(
        "test_worker_3")
