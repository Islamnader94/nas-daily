### To run the server:

```
docker-compose up -d
```

### To Run migrations inside docker container:

```
docker exec -it backend-nas-daily python manage.py migrate
```

### To create a  super user for Django admin access:

```
docker exec -it backend-nas-daily python manage.py migrate
```