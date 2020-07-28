# basic-flaskapp
This is a working example of a multi-container flask application with postgres, mongo and redis as the database fronted by the nginx reverse proxy.
Primero hay que correr sudo docker-compose up
obtener el id del contenedor donde esta corriendo mongo
sudo docke ps
sudo docker exec -it <id> bash
contenedor donde esta corriendo mongo
mongo --version
mongo
base de datos
show dbs
use testdb
show collections
para ver los registros
db.users.find()
