

from test import app , client , db , ctx 
from app.application.model.worker.WorkerDAO import WorkerDAO
from app.application.model.metadata.MetadataImageDAO import MetadataImageDAO
from app.application.model.task.TaskDAO import TaskDAO
from app.application.controlers.tools.PersistenValue import PersistenValue

def test_get_new_image_with_no_data(client):
    response = client.get("/get_new_image")
    assert response.status_code == 404
    
    

    
    

def test_get_new_image_route_with_some_wrong_data(client):
    params = {
        "asdf" : "asdfasdf",
        "asdfasd" : "asdfasdf"
    }
    response = client.get("/get_new_image" , query_string = params)
    assert response.status_code == 404
    
    
    
def get_new_image_route_with_some_ok_data(ctx , client):
    
    ### Dadas estas condiciones
    w = WorkerDAO(
        name = "test_worker",
        ip = "192.168.0.1"
    )
    db.session.add(w)
    params = {
        "worker_name" : "test_worker",
        "token" : "abecd51a1c29a87482da68435ded4feaa6842608"
    }
    
    # Se hacer lo siguiente
    response = client.get("/get_new_image" , query_string = params)
    
    
    # Se espera que: 
     
    assert response.status_code == 200  
    
    
def test_get_new_image_route_with_some_client_not_exist(ctx , client):
    
    ### Dadas estas condiciones
    w = WorkerDAO(
        name = "test_worker_3",
        ip = "192.168.0.1"
    )
    db.session.add(w)
    params = {
        "worker_name" : "test_worker",
        "token" : "abecd51a1c29a87482da68435ded4feaa6842608"
    }
    
    # Se hacer lo siguiente
    response = client.get("/get_new_image" , query_string = params)
    
    
    # Se espera que: 
    
    assert response.status_code == 404   



def createImage(day, mount, image_name):
    obj = MetadataImageDAO(creation_date = "2021-{}-{} 10:55:56.559".format(mount, day),
    block_name = 1,
    ship_name = 1,
    side_name = "b",
    bed_name = 0,
    index = 0,	
    latitude = 1.0,
    longitude = 2.2,
    altitude = 3.3,	
    creation_image_date = "2021-{}-{} 10:55:56.559".format(mount, day),
    creation_image_time = "2021-{}-{} 10:55:56.559".format(mount, day),
    folder_name = "root",
    image_name = image_name,
    format_image = "jpg",

    image_width = 300, 
    high_width = 400, 
    iso = 31, 
    opening = "ending",
    exhibition_time = 35.0,
    datalake_route = "/path/root",
    software_version = "0.20145",
    white_balance = "0    1",
    camera_date = "2021-{}-{} 10:55:56.559".format(mount, day),
    local_longitude = 98798)  
    db.session.add(obj)
    db.session.commit()

def createWorker(name, ip):
    obj = WorkerDAO(
        creation_date="2022-09-30 10:55:56.559",
        modification_date="2022-09-30 10:55:56.559",
        name=name,
        ip=ip,
        deleted_at="2022-09-30 10:55:56.559"
    )  
    db.session.add(obj)
    db.session.commit()

def findTask(workerName, state):
    return db.session.query(
			TaskDAO, 
			WorkerDAO
		
		).filter(TaskDAO.worker_id == WorkerDAO.id
		).filter(WorkerDAO.name == workerName
        ).filter(TaskDAO.status == state
        ).first()

    
def test_get_new_image_route_with_some_ok_data(ctx , client):
    persiten = PersistenValue()
    ### Dadas estas condiciones
    """
    w = WorkerDAO(
        name = "test_worker",
        ip = "192.168.0.1"
    )
    db.session.add(w)
    db.session.commit()
    """

    # poblate db metadata
    createImage("12", "09", "image_1")
    createImage("11", "08", "image_2")
    createImage("13", "07", "image_3")
    createImage("14", "06", "image_3")
    
    #poblate db workers
    createWorker("test_worker","192.168.0.1")
    
    createWorker("test_worker_1","localhost")
    createWorker("test_worker_2","localhost")

    # ----------------------------------------------------------
    
    params = {
        "worker_name" : "",
        "token" : ""
    }
    
    # first test
    params["worker_name"] = "test_worker"
    params["token"] = "abecd51a1c29a87482da68435ded4feaa6842608"
    response = client.get("/get_new_image" , query_string = params)
    assert response.status_code == 200 

    task = findTask(params["worker_name"], persiten.state_task.in_process)
    assert task is not None, "No se registro la tarea para el worker {}".format(params["worker_name"])

    # second  test
    params["worker_name"] = "test_worker_1"
    params["token"] = "d28676c4c636a93026e048c82207ec5df9950dc0"
    response = client.get("/get_new_image" , query_string = params)
    assert response.status_code == 200 
    
    task = findTask(params["worker_name"], persiten.state_task.in_process)
    assert task is not None, "No se registro la tarea para el worker {}".format(params["worker_name"])

    # third  test
    params["worker_name"] = "test_worker_2"
    params["token"] = "3487b637d995b6472b3df5dc80e4fa25dd99c90b"
    response = client.get("/get_new_image" , query_string = params)
    assert response.status_code == 200 
    
    task = findTask(params["worker_name"], persiten.state_task.in_process)
    assert task is not None, "No se registro la tarea para el worker {}".format(params["worker_name"]) 


    # ------------ get error -------

    # first test
    """
    """
    
    params["worker_name"] = "test_worker"
    params["token"] = "abecd51a1c29a87482da68435ded4feaa6842608"
    response = client.get("/get_new_image" , query_string = params)
    assert response.status_code == 404 

     
