import os

APPNAME  = os.environ.get("nameAPP" , None)
APPTIMEOUT = int(os.environ.get("APP_TIME_OUT" , None))
APPSETTINGS = int(os.environ.get("APP_WORKERS" , None))