#!/bin/bash

# Ustvari Docker omrežje
docker network create cam_network

# Zgradi in zaženi strežnik
docker build -t cam_server ./server
docker run -d --name server --network cam_network cam_server &

# Zgradi in zaženi odjemalca
docker build -t cam_client ./client
docker run -d --name client --network cam_network -p 5001:5001 cam_client &

# Počakaj, da se kontejnerji zgradijo in zaženejo
wait

# Pridobi IP naslov odjemalca
CLIENT_IP=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client)
echo "Odjemalec teče na IP: $CLIENT_IP"
