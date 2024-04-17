# Sfhmmy2024
An introduction to Django 5.0 with the help of developer.mozilla.org implementing a local library app

### Step 0:
0. Clone the repository
```bash
git clone https://github.com/kbodurri/Sfhmmy2024
```

### Step 1:
0. Change branch from master to step1
```bash
git checkout step1
```

1. Build image for first time and run the app
```bash
docker compose up -d --build
```

2. Check the logs if everything is up and running
```bash
docker compose logs -f -t
```

3. Apply migrations from various apps such as admin, auth, contenttypes, sessions
```bash
docker compose exec web_app ./manage.py migrate
```

4. Restart the web_app
```bash
docker compose restart web_app
```
5. Register a new django called catalog
```bash
docker compose exec web_app ./manage.py startapp catalog
```
6. Include the newly created app to INSTALLED_APPS in settings.py
7. Append the catalog urls to URLMapper
8. Add an empty urlpattern list in urls.py from catalog app
### Step 2:
0. Change to step2 branch
1. Create our first migration file
```bash
docker compose exec web_app ./manage.py makemigrations
```
2. Apply the migration file
```bash
docker compose exec web_app ./manage.py migrate
```
3. Generate the migration file for Language Model and apply it
4. Revert it back and go to step3 branch
```
docker compose exec web_app ./manage.py migrate web_app 0001
```

### Step 3:
0. Switch to step3 branch
1. Apply the migrations
```bash
docker compose exec web_app ./manage.py migrate
```
2. Populate the database
```bash
docker compose exec web_app ./manage.py populate_db
```
3. Register the models to the Admin Site
4. Make it prettier <3

### Step 4:
0. Switch to step4 branch
1. Change the `BookInstance` listview to display the book, status, due back date, and id
2. Add an inline listing of `Book` items to the `Author` detail view

### Step 5:
0. Switch to step5 branch
1. Override this block in the `index template` and create a new title for the page.
2. Modify the `view` to generate counts for _genres_ and _books_ that contain a particular word (case insensitive), and pass the results to the `context`

### Step 6:
0. Switch to step6 branch
1. Add list and detail view for Authors

### Step 7:
0. Switch to step7 branch
1. Finito
