import multiprocessing
import os

from config import Config

# listen to port 5858 on all available network interfaces
bind = "{0}:{1}".format(Config.APP_HOST, Config.APP_PORT)

# run the app in multiple processes
workers = 4 if (multiprocessing.cpu_count() * 2 + 1)>=Config.WORKERS_NUMBER else 2 #dice que con 4-12 pueden manejar de cientos a miles de solicitudes deje 4 maxi
#https://docs.gunicorn.org/en/stable/design.html
#(Always remember, there is such a thing as too many workers. After a point your worker processes will
#start thrashing system resources decreasing the throughput of the entire system. )
worker_class = 'sync'
#logs gunicorn

timeout = Config.TIMEOUT


if not os.path.exists("log"):
    os.makedirs("log")
accesslog = "log/access-logfile.log"
errorlog = "log/error-logfile.log"