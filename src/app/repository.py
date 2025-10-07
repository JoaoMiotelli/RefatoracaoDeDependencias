from typing import Dict, Optional, Iterable
from .domain import User
from .ports import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._counter = 0

    def next_id(self) -> int:
        self._counter += 1
        return self._counter

    def add(self, user: User) -> None:
        self._users[user.id] = user

    def list_all(self) -> Iterable[User]:
        return list(self._users.values())

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    def save(self, user: User) -> None:
        self._users[user.id] = user