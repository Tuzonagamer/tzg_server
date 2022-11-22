from test import app, client, db, ctx
from app.application.model.worker.WorkerDAO import WorkerDAO
from app.application.model.metadata.MetadataImageDAO import MetadataImageDAO
from app.application.model.task.TaskDAO import TaskDAO
from app.application.controlers.tools.PersistenValue import PersistenValue

from .tools.utilities import createImage , createWorker , build_BBX


#def findTask(workerName, state):
#    return db.session.query(
#        TaskDAO,
#        WorkerDAO
#
#    ).filter(TaskDAO.worker_id == WorkerDAO.id
#             ).filter(WorkerDAO.name == workerName
#                      ).filter(TaskDAO.status == state
#                               ).first()
#
#


# //////////////////////////////////////////// 1 test //////////////////////////////////////////////


def test_post_new_bbx_with_no_data(client):
    response = client.post("/insert_bounding_boxes")
    assert response.status_code == 404

# //////////////////////////////////////////// 2 test //////////////////////////////////////////////


def test_post_new_bbx_route_with_some_wrong_data(client):
    params = {
        "name": "", "token": "", "finca": "", "bloque": "", "nave": "", "lado": "", "cama": "", "fecha": "", "image_name": "", "task_id": "",
        "modelo": "",
        "bounding_boxes": [
            {
                "x_min": "", "x_max": "", "y_min": "", "y_max": "", "clase": "", "probabilidad": "", "model_data": ""
            }
        ],
        "worker_name": "test_worker",
        "token": "abecd51a1c29a87482da68435ded4feaa6842608"
    }

    # createWorker("test_worker","localhost")
    response = client.post("/insert_bounding_boxes", data=params)
    assert response.status_code == 404

# //////////////////////////////////////////// 3 test //////////////////////////////////////////////


def test_get_new_bbx_with_some_client_not_exist(ctx, client):

    # Dadas estas condiciones
    params = {
        "name": "", "token": "", "finca": "", "bloque": "", "nave": "", "lado": "", "cama": "", "fecha": "", "image_name": "", "task_id": "",
        "modelo": "",
        "bounding_boxes": [
            {
                "x_min": "", "x_max": "", "y_min": "", "y_max": "", "clase": "", "probabilidad": "", "model_data": ""
            }
        ],
        "worker_name": "test_worker",
        "token": "abecd51a1c29a87482da68435ded4feaa6842608"
    }

    # Se hacer lo siguiente
    response = client.post("/insert_bounding_boxes", query_string=params)

    # Se espera que:

    assert response.status_code == 404

# //////////////////////////////////////////// 4 test //////////////////////////////////////////////


def test_get_post_new_bbx_with_some_ok_data(ctx, client):

    # creacion tarea:
    persiten = PersistenValue()

    # poblate db metadata
    createImage("12", "09", "image_1")
    createImage("11", "08", "image_2")
    createImage("13", "07", "image_3")
    createImage("14", "06", "image_3")

    # poblate db workers
    createWorker("test_worker", "192.168.0.1")

    createWorker("test_worker_1", "localhost")
    createWorker("test_worker_2", "localhost")

    # -------------------------- params --------------------------------

    params = {}  # build_BBX()
    # ///////////////////////// first test  ////////////////////////////

    params["worker_name"] = "test_worker"
    params["token"] = "abecd51a1c29a87482da68435ded4feaa6842608"
    response = client.get("/get_new_image", query_string=params)
    assert response.status_code == 200
    task_data = response.json["data"]

    params = build_BBX()
    params["worker_name"] = "test_worker"
    params["token"] = "abecd51a1c29a87482da68435ded4feaa6842608"
    params["task_id"] = task_data["task_id"]

    # Se hacer lo siguiente

    response = client.post("/insert_bounding_boxes", json=params)
    assert response.status_code == 200

    # ///////////////////////// second test  ////////////////////////////

    params = {}
    params["worker_name"] = "test_worker_2"
    params["token"] = "3487b637d995b6472b3df5dc80e4fa25dd99c90b"
    response = client.get("/get_new_image", query_string=params)
    assert response.status_code == 200
    task_data = response.json["data"]

    params = build_BBX()
    params["worker_name"] = "test_worker_2"
    params["token"] = "3487b637d995b6472b3df5dc80e4fa25dd99c90b"
    params["task_id"] = task_data["task_id"]

    # Se hacer lo siguiente
    response = client.post("/insert_bounding_boxes", json=params)
    assert response.status_code == 200

    # //////////////////////////// third test //////////////////////////3
    params = {}
    params["worker_name"] = "test_worker_1"
    params["token"] = "d28676c4c636a93026e048c82207ec5df9950dc0"
    response = client.get("/get_new_image", query_string=params)
    assert response.status_code == 200
    
    task_data = response.json["data"]
    bbx_count = 3
    params = build_BBX(image_name=task_data["image_name"], bbx_count=bbx_count)

    params["worker_name"] = "test_worker_1"
    params["token"] = "d28676c4c636a93026e048c82207ec5df9950dc0"
    params["task_id"] = task_data["task_id"]

    # Se hace lo siguiente
    response = client.post("/insert_bounding_boxes", json=params)

    assert response.status_code == 200

    data = response.json

    check_output(data, task_data , bbx_count)
    
    
    


def object_responseInsert():
    return {
        "status": None,
        "imagen_procesada": None,
        "bbx_procesados_correctos": None,
        "hora_final": None
    }


def check_output(response, task_data  , bbx_count):

    assert type(response) is dict, " error en la respuesta {}".format(response)

    object = response["data"]
    for ans_key in object.keys():
        assert ans_key in object_responseInsert().keys(
        ), "la llave de repuesta es invalida {} ".format(ans_key)

    assert object["status"] == "ok"
    assert object["imagen_procesada"] == task_data["image_name"]
    assert object["bbx_procesados_correctos"] == bbx_count
    assert type(object["hora_final"]) != "datetime"
