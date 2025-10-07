from typing import Optional
import json
from urllib import request, error
from .ports import ExternalUserApi

class JsonPlaceholderClient(ExternalUserApi):
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self._base_url = base_url

    def get_user(self, user_id: int) -> Optional[dict]:
        url = f"{self._base_url}/users/{user_id}"
        try:
            with request.urlopen(url, timeout=5) as resp:
                if resp.status == 200:
                    return json.loads(resp.read().decode())
        except error.HTTPError:
            return None
        except error.URLError:
            return None
        return None