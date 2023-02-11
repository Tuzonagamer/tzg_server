
from app.application.model.boundingBox.BoundingBoxDAO import BoundingBoxDAO
from test import app , client , db , ctx 
from app.application.model.worker.WorkerDAO import WorkerDAO
from app.application.model.metadata.MetadataImageDAO import MetadataImageDAO
from app.application.model.task.TaskDAO import TaskDAO
from app.application.controlers.tools.PersistenValue import PersistenValue

from .tools.utilities import *

def test_insert_bbx_by_img(ctx , client):
    
    ### Dadas estas condiciones
    w = WorkerDAO(
        name = "test_worker_1",
        ip = "192.168.0.1"
    )
    db.session.add(w)
    
    image = createImage("12", "09", "image_1")
    
    bbx_count = 3
    
    # when 
    params = build_BBX(image_name="image_1", bbx_count=bbx_count)
    
    params["worker_name"] = "test_worker_1"
    
    """
    {'name': 'image_1', 
    'finca': '', 
    'bloque': '1', 
    'nave': '1', 
    'lado': 'b', 
    'cama': '0', 
    'fecha': '2021-08-11', 
    'image_name': 'image_2', 
    'task_id': 1, 
    'modelo': 'YOLOV5 - classificador 34RNN V1.1', 
    'bounding_boxes': 
    [
        {'x_min': 2578.0, 'x_max': 2856.0, 'y_min': 2729.0, 'y_max': 2915.0, 'clase': 'P2.1', 'probabilidad': 85.0, 'model_data': 'model_data[vc1,vc2,vc3,....,cp1,cp2,..]'},
        {'x_min': 2578.0, 'x_max': 2856.0, 'y_min': 2729.0, 'y_max': 2915.0, 'clase': 'P2.1', 'probabilidad': 85.0, 'model_data': 'model_data[vc1,vc2,vc3,....,cp1,cp2,..]'}, 
        {'x_min': 2578.0, 'x_max': 2856.0, 'y_min': 2729.0, 'y_max': 2915.0, 'clase': 'P2.1', 'probabilidad': 85.0, 'model_data': 'model_data[vc1,vc2,vc3,....,cp1,cp2,..]'}
    ], 
    'worker_name': 'test_worker_1', 
    }
    """
    
    response = client.post("/insert_bounding_boxes_by_image" , json = params)
    
     
    # Se espera que: 
     
    assert response.status_code == 200  

    # se registra la tarea? 
    task = TaskDAO.find(1)
    assert task.status == "success" , "La tarea no está terminada"
    assert task.metadata_image_id == image.id , "No se registro la tarea con el metadata image correspondiente"
    assert task.worker_id == w.id
    
    
    # se ingresaron los bounding boxes
    bbx = BoundingBoxDAO.getAll()
    
    assert len(bbx) == 3 , "se deberian haber registrado 3 bbx"
    
    for b in bbx :
        assert b.task_id == task.id  , "Los bbx no tienen el correspondiente id"
        assert b.metadata_image_id == image.id , "No se registró el bbx con el id de la imagen correspondiente"
        
        