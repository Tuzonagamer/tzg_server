import os

DB_NAME = os.environ.get("dataBaseNameDB" , "postgres")
DB_SCHEMA_NAME = os.environ.get("schemaDB" , "tzg")
DB_HOSTNAME = os.environ.get("hostDB" , "192.168.1.1")
DB_USERNAME = os.environ.get("userDB" , "postgres") 
DB_PASSWORD = os.environ.get("passDB" , "postgres") 
DB_TYPE = os.environ.get("typeDB" ,"postgres+psycopg2") 
DB_PORT = os.environ.get("portDB" , "5432") 
DB_CHARSET = os.environ.get("encodingDB" , None) 
DB_SOCKET = os.environ.get("socketDB" , None) 

