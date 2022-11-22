import os

DB_NAME = os.environ.get("dataBaseNameDB" , None)
DB_SCHEMA_NAME = os.environ.get("schemaDB" , None)
DB_HOSTNAME = os.environ.get("hostDB" , None)
DB_USERNAME = os.environ.get("userDB" , None) 
DB_PASSWORD = os.environ.get("passDB" , None) 
DB_TYPE = os.environ.get("typeDB" ,None) 
DB_PORT = os.environ.get("portDB" , None) 
DB_CHARSET = os.environ.get("encodingDB" , None) 
DB_SOCKET = os.environ.get("socketDB" , None) 

