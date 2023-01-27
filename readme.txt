Start the docker redis server on port 6379 (download image automatically)
    docker run -p 6379:6379 -d redis:5

Activate VENV
    source prototype/bin/activate

Start the local django server
    python3 manage.py startserver