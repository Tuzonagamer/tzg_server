## Project: T.Z.G_SERVER
- is services type charts api rest

# description
- server with managament bussin T.Z.G  platform, *(web, devices, desktop)

# Requeriments
- docker.
- access db machine

# Prepare Install  .env
```bash
# General Settings 
nameAPP=server
versionApp=1.0


# run on...
hostAPP=localhost
portAPP=8080
APP_DEBUG=true
APP_KEY=secret
APP_TIME_OUT=10000
APP_WORKERS=2

# setting enviroment db settings

hostDB=192.168.1.1
portDB=5432

# credentials
userDB=postgres
passDB=postgres

# specification
schemaDB=tzg
dataBaseNameDB=postgres

# settings DB
encodingDB=enconding
typeDB=postgres+psycopg2
socketDB=None

```
# launch on local mode out dopcker enviroment:
- first install dependencys save on route:
    - yourdirectory/rootfolder/docker/Dockerfile

# by run execute command in root folder
- flask run <- on case execute on local machine out local lan
- flask run --host 127.0.0.1 --port 5000 <- on case execute without and with local machine and local lan.



# accound support
-   tuzonapcgamersppt@gmail.com