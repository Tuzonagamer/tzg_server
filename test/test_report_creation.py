from test import app, client, db, ctx
from test.test_registry_bbx import test_get_post_new_bbx_with_some_ok_data
from app.application.controlers.work.BoundingBoxClassCounter import BoundingBoxClassCounter
from app.application.model.task.reports.TaskReportDAO import TaskReportDAO
from .tools.utilities import *

from app.application.controlers.task.TaskCT import TaskCT
from app.application.controlers.task.TaskReportCT import TaskReportCT



bounding_boxes = [
    {
        "x_min": 2578.0, "x_max": 2856.0, "y_min": 2729.0, "y_max": 2915.0, "clase": "P1.1", "probabilidad": 85.0,
        "model_data": "model_data[vc1,vc2,vc3,....,cp1,cp2,..]"
    },
    {
        "x_min": 2578.0, "x_max": 2856.0, "y_min": 2729.0, "y_max": 2915.0, "clase": "P2.1", "probabilidad": 85.0,
        "model_data": "model_data[vc1,vc2,vc3,....,cp1,cp2,..]"
    },
    {
        "x_min": 2578.0, "x_max": 2856.0, "y_min": 2729.0, "y_max": 2915.0, "clase": "P2.1", "probabilidad": 85.0,
        "model_data": "model_data[vc1,vc2,vc3,....,cp1,cp2,..]"
    },
    {
        "x_min": 2578.0, "x_max": 2856.0, "y_min": 2729.0, "y_max": 2915.0, "clase": "P8.4", "probabilidad": 85.0,
        "model_data": "model_data[vc1,vc2,vc3,....,cp1,cp2,..]"
    }
]

def test_counting_the_class_of_each_bbx():


    bbx_controller = BoundingBoxClassCounter()
    report = bbx_controller.count_classes(bounding_boxes)

    assert report == {
        "class_1": 1,
        "class_2": 2,
        "class_3": 0,
        "class_4": 0,
        "class_5": 0,
        "class_6": 0,
        "class_7": 0,
        "class_8": 0,
        "class_9": 0,
        "class_10": 0,
        "class_11": 0,
        "class_12": 0,
        "class_13": 1,
    }
    return report

def test_insert_report_on_db( ctx ) :
        
    imageDAO =  createImage("12", "09", "image_1")
    createWorker("test_worker", "192.168.0.1") 
    taskct = TaskCT()
    task = taskct.getNewTask("test_worker")
    
    bbx_controller = BoundingBoxClassCounter()
    counting_report = bbx_controller.count_classes(bounding_boxes)
    
    taskReportDAO = TaskReportDAO( 
            metadata_image_id=imageDAO.id,
            task_id = task["task_id"], 
            **counting_report ) 
    taskReportDAO.create()
    
    assert taskReportDAO.id == 1



def test_create_report_controller( ctx ) :
        
    imageDAO =  createImage("12", "09", "image_1")
    createWorker("test_worker", "192.168.0.1") 
    taskct = TaskCT()
    task = taskct.getNewTask("test_worker")
    
    taskDAO = taskct.findTask(task["task_id"])
    taskReportCT = TaskReportCT()
    
    taskReportDAO = taskReportCT.create(taskDAO , bounding_boxes )
    
    assert taskReportDAO.id == 1