# Sfhmmy2024
An introduction to Django 5.0 with the help of developer.mozilla.org implementing a local library app

# Step 0:
##### Clone the repository
```bash
git clone https://github.com/kbodurri/Sfhmmy2024
```

# Step 1:
##### Change branch from master to step1
```bash
git checkout step1
```

##### Build image for first time and run the app
```bash
docker-compose up -d --build
```

##### Check the logs if everything is up and running
```bash
docker-compose logs -f -t
```

##### Apply migrations from various apps such as admin, auth, contenttypes, sessions
```bash
docker-compose exec web_app ./manage.py migrate
```

##### Restart the web_app
```bash
docker-compose restart web_app
```
