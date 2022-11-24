import os
import json
import sys

from configurations import Database , HostApp , Settings

class Config(object):

    #SETTINGS DB
     
    DB_HOSTNAME = Database.DB_HOSTNAME
    DB_NAME = Database.DB_NAME
    DB_SCHEMA_NAME = Database.DB_SCHEMA_NAME
    DB_USERNAME = Database.DB_USERNAME
    DB_PASSWORD = Database.DB_PASSWORD
    DB_TYPE = Database.DB_TYPE
    DB_SOCKET = Database.DB_SOCKET
    DB_ṔORT = Database.DB_PORT
    DB_CHARSET = Database.DB_CHARSET
    
    #SETTINGS PATHS
    

    APP_NAME = Settings.APPNAME

    #SETTINGS APP HOST 
    
    APP_HOST = HostApp.APP_HOST
    APP_PORT = HostApp.APP_PORT
    APP_DEBUG = HostApp.APP_DEBUG
    APP_KEY = HostApp.APP_KEY 
    #uri db
    
    SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(DB_TYPE, DB_USERNAME, DB_PASSWORD, DB_HOSTNAME, DB_ṔORT,        DB_NAME)
    if(SQLALCHEMY_DATABASE_URI == "/postgres1.1copg2"):
        print("let's go!!")
    else:
        print("Fail!!")
        print(SQLALCHEMY_DATABASE_URI)
    
    # settings gunicorn
    
    TIMEOUT = Settings.APPTIMEOUT
    WORKERS_NUMBER = Settings.APPSETTINGS

    
class test_config(Config):
    
    DB_SCHEMA_NAME = "test"
    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        Config.DB_TYPE, 
        Config.DB_USERNAME, 
        Config.DB_PASSWORD, 
        Config.DB_HOSTNAME, 
        Config.DB_ṔORT,        
        Config.DB_NAME)