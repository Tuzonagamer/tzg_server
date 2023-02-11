from test import app, client, db, ctx
from app.application.model.worker.WorkerDAO import WorkerDAO
from app.application.model.metadata.MetadataImageDAO import MetadataImageDAO
from app.application.model.task.TaskDAO import TaskDAO

from .tools.utilities import *


def object_responseInsert():
    return {
        "status": None,
        "imagen_procesada": None,
        "bbx_procesados_correctos": None,
        "hora_final": None
    }


def check_insert_bbx_output(response, task_data  , bbx_count):

    assert type(response) is dict, " error en la respuesta {}".format(response)

    object = response["data"]
    
    
    for ans_key in object.keys():
        assert ans_key in object_responseInsert().keys(
        ), "la llave de repuesta es invalida {} ".format(ans_key)

    assert object["status"] == "ok"
    assert object["imagen_procesada"] == task_data["image_name"]
    assert object["bbx_procesados_correctos"] == bbx_count
    assert type(object["hora_final"]) != "datetime"




def test_full_solution(ctx, client):

    # -------------------------- creating data on database --------------------------------

    # poblate db metadata
    createImage("12", "09", "image_1")
    createImage("11", "08", "image_2")
    createImage("13", "07", "image_3")
    createImage("14", "06", "image_4")

    # poblate db workers
    createWorker("test_worker", "192.168.0.1")
    createWorker("test_worker_1", "localhost")
    createWorker("test_worker_2", "localhost")

    # -------------------------- getting the image to work --------------------------------

    params = {}
    params["worker_name"] = "test_worker_1"
    params["token"] = "d28676c4c636a93026e048c82207ec5df9950dc0"
    
    response = client.get("/get_new_image", query_string=params)
    assert response.status_code == 200
    
    task_data = response.json["data"]
    # print("task data" , task_data)
    
    """ 
    {'bloque': 1, 
    'cama': 0, 
    'fecha': '2021-08-11', 
    'finca': '', 
    'hora': '10:55:56.559000', 
    'image_id': '',
    'image_name': 'image_2', 
    'lado': 'b', 
    'nave': 1, 
    'task_id': 1, 
    'worker_id': 2} 
    """
    
    # -------------------------- simulating the working --------------------------------

    bbx_count = 3
    
    params = build_BBX(image_name=task_data["image_name"], bbx_count=bbx_count)
    
    params["task_id"] = task_data["task_id"]
    params["worker_name"] = "test_worker_1"
    params["token"] = "d28676c4c636a93026e048c82207ec5df9950dc0"
    #print("inserting bounding box" , params)
    """
    {'name': 'image_2', 
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
    'token': 'd28676c4c636a93026e048c82207ec5df9950dc0'
    }
    """
    
    # -------------------------- inserting the BBX --------------------------------
    
    response = client.post("/insert_bounding_boxes", json=params)
    assert response.status_code == 200

    data = response.json
    
    #print("insert bounding box info" , data)

    check_insert_bbx_output(data, task_data , bbx_count)

    """
    
    {'bbx_procesados_correctos': 3, 
    'hora_final': 'Thu, 13 Oct 2022 12:35:54 GMT',
    'imagen_procesada': 'image_2', 
    'status': 'ok'} 
    """