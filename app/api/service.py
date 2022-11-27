import os
import httpx

AUTHOR_SERVICE_HOST_URL = 'http://localhost:8000/api/v1/authors/'

url = os.environ.get('AUTHOR_SERVICE_HOST_URL') or AUTHOR_SERVICE_HOST_URL

def is_author_present(author_id: int):
    r = httpx.get(f"{url}{author_id}")
    return True if r.status_code == 200 else False
