## Build Commands

```
# Build image
cd dockerfiles/django
docker build -t django_dev .

# Run django
docker run --rm -itd -p 127.0.0.1:8000:8000 -v ~/Documents/10.work/pj-docker/django_dev/src:/code --name django_dev django_dev

# Create project
cd ../../src
docker exec django_dev django-admin startproject pr_django .

# Create apps
docker exec django_dev python3 manage.py startapp diary

# Run django-server
docker exec django_dev python3 manage.py runserver 0.0.0.0:8000
```

## Let's Access Below URL

- http://localhost:8000

## Compose Command

```
# Build
docker-compose up -d

# Rebuild
docker-compose up --build -d

# Run django command
docker-compose exec django python3 manage.py ....

# Collect static files
docker-compose exec django python3 manage.py collectstatic
```

## Let's Access Below URL

- http://localhost:8000
- http://localhost:8000/admin

## Git ignore

```
# Ignore changes
git update-index --skip-worktree docker-build/docker-compose.yml src/pr_django/settings.py

# Not-Ignore changes
git update-index --no-skip-worktree docker-build/docker-compose.yml src/pr_django/settings.py
```

