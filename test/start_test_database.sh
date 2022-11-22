#! /bin/bash

{
    ## DOCKER SETTINGS

    DOCKER_DATABASE_IMAGE=postgres
    DOCKER_DATABASE_CONTAINER=floresfase_2_datbase
    
    source ../.env	
	
    echo "Starting POSTGRES"

	docker run -d \
	--rm \
	--name $DOCKER_DATABASE_CONTAINER \
	-e POSTGRES_PASSWORD="$DB_PASSWORD" \
	-e POSTGRES_DB="$DB_NAME" \
	-v "$PWD"/dbdata:/var/lib/postgresql/data \
	--net="host" \
	$DOCKER_DATABASE_IMAGE
} || {

	echo "POSTGRES already started "
}	