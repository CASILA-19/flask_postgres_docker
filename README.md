Cómo Ejecutar el Proyecto

 Clonar el Repositorio  
 
git clone https://github.com/CASILA-19/flask_postgres_docker.git
cd flask_postgres_docker

CONSTRUIR Y LEVANTAR LOS CONTENEDORES
docker-compose up --build

VERIFICAMOS QUE ESTEN BIEN
docker ps

Y YA SE PUEDE PROBAR
curl -X GET http://localhost:5000/students
curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"nombre": "Juan", "edad": 22, "carrera": "Ingeniería"}'
curl -X PUT http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{"nombre": "Juan Perez"}'
curl -X DELETE http://localhost:5000/students/1

