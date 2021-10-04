# Task: Parser for [kingfisher.kz](https://kingfisher.kz/)

### ```GET /save/items```


### ```Docker-compose```
__docker-compose.yml__:<br>
```
        - app
        - db: PostgreSQL
```

Build, (re)create, start, and attache to containers for a service.
```
docker-compose up -d --build
```
Display log outputs
```
docker-compose logs -f
```
Stop containers and remove containers, networks, volumes, and images created by **up**
```
docker-compose down
```
