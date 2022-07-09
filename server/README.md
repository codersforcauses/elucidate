# Elucidate Backend

## Getting started

### Development server

After setting up your development workspace in the main guide, you can launch a Django development server by running `python manage.py runserver`. Note, you must be in the `server` folder inside the docker container for this to work.

### Running tests

Tests can be run with the command `python manage.py test`

If you are running through container

```bash
docker exec -t -i elucidate_server python manage.py
test
```
