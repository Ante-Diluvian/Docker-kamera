#!/bin/bash

# Ustavi in odstrani kontejnerja (strežnik in odjemalec)
docker stop server client
docker rm server client

# Odstrani Docker omrežje
docker network rm cam_network

echo "Done"
