Global Python task
==================

I completed the challenge in 2:45.
I had fun with this challenge and decided to focus on end to end tests to check the expected endpoints.
I used the pagination system to display the first 100 results for tracks.

# Init the project
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
./manage.py migrate
```

# Run tests
```
./manage.py test
```

# Import data into the db
```
./manage.py import_tracks
```

# Run project
```
./manage.py runserver
```
