## This is a technical test for Nas Daily.

### List of technologies used:

- Django 3 (BackEnd)
- Docker and Docker-compose (DevOps)

### Start by changing the value of LOT_SIZE in .env file according to preference:

```
LOT_SIZE=5
```

### To build the project using docker and docker-compose:

```
docker-compose build
```

### To run the server:

```
docker-compose up -d
```

### To Run database migrations inside docker container:

```
docker exec -it backend-nas-daily python manage.py makemigrations
docker exec -it backend-nas-daily python manage.py migrate
```

### To create a  super user for Django admin access:

```
docker exec -it backend-nas-daily python manage.py createsuperuser
```

### To run tests using pytest:

```
docker exec -it backend-nas-daily pytest
```
