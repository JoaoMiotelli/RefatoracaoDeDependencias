from typing import Iterable, Optional
from .domain import User, welcome_message
from .ports import UserRepository, EmailSender, ExternalUserApi

def add_user(name: str, email: str, repo: UserRepository, email_sender: EmailSender) -> User:
    new_user = User(id=repo.next_id(), name=name, email=email, active=True)
    repo.add(new_user)
    email_sender.send(new_user.email, welcome_message(new_user))
    return new_user

def list_users(repo: UserRepository) -> Iterable[User]:
    return repo.list_all()

def deactivate_user(user_id: int, repo: UserRepository) -> bool:
    user = repo.get_by_id(user_id)
    if not user:
        return False
    updated = User(id=user.id, name=user.name, email=user.email, active=False)
    repo.save(updated)
    return True

def fetch_user_from_api(user_id: int, api: ExternalUserApi) -> Optional[dict]:
    return api.get_user(user_id)