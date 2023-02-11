
from tkinter import W
from app.application.model.worker.WorkerDAO import WorkerDAO
from . import app , pytest , db , ctx 

@pytest.fixture
def insert_worker(ctx):
    w = WorkerDAO(
    name = "test_worker",
    ip = "192.168.0.1"
    )
    db.session.add(w)
    db.session.commit()
    

def  test_get_worker_by_id(insert_worker):
    w_inserted = WorkerDAO.get(1)
    assert w_inserted.name == "test_worker"
    
    
def test_get_worket_by_existing_name(insert_worker):
    w_inserted = WorkerDAO.getByName("test_worker")
    assert w_inserted.name == "test_worker"
    
    
