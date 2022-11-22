from test import app, client, db, ctx
from app.application.model.worker.WorkerDAO import WorkerDAO
from app.application.model.metadata.MetadataImageDAO import MetadataImageDAO
from app.application.model.task.TaskDAO import TaskDAO
from app.application.controlers.tools.PersistenValue import PersistenValue
from app.application.controlers.task.TaskCT import TaskCT


def createImage(day, mount, image_name):
    obj = MetadataImageDAO(creation_date="2021-{}-{} 10:55:56.559".format(mount, day),
                           block_name=1,
                           ship_name=1,
                           side_name="b",
                           bed_name=0,
                           index=0,
                           latitude=1.0,
                           longitude=2.2,
                           altitude=3.3,
                           creation_image_date="2021-{}-{} 10:55:56.559".format(
                               mount, day),
                           creation_image_time="2021-{}-{} 10:55:56.559".format(
                               mount, day),
                           folder_name="root",
                           image_name=image_name,
                           format_image="jpg",

                           image_width=300,
                           high_width=400,
                           iso=31,
                           opening="ending",
                           exhibition_time=35.0,
                           datalake_route="/path/root",
                           software_version="0.20145",
                           white_balance="0    1",
                           camera_date="2021-{}-{} 10:55:56.559".format(
                               mount, day),
                           local_longitude=98798)
    db.session.add(obj)
    db.session.commit()
    return obj


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


def build_BBX(image_name="DJI_074", task_id="0",  bbx_count=1):
    bbx = {
        "x_min": 2578.0, "x_max": 2856.0, "y_min": 2729.0, "y_max": 2915.0, "clase": "P2.1", "probabilidad": 85.0,
        "model_data": "model_data[vc1,vc2,vc3,....,cp1,cp2,..]"
    }

    return {
        "name": image_name, "finca": "El Rosal",
        "bloque": "42_", "nave": "_8", "lado": "a", "cama": "_2",
        "fecha": "2021-06-11", "image_name": image_name, "task_id": task_id,
        "modelo": "k-14",
        "bounding_boxes": [bbx for b in range(bbx_count)]
    }
