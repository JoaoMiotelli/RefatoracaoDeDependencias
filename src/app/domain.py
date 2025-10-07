from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str
    active: bool = True

def welcome_message(user: User) -> str:
    return f"Olá {user.name}, bem-vindo ao sistema!"