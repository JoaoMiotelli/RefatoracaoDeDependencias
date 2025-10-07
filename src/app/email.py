from datetime import datetime
from pathlib import Path
from .ports import EmailSender

class FileEmailSender(EmailSender):
    def __init__(self, logfile: str = "log_email.txt") -> None:
        self._path = Path(logfile)

    def send(self, to_email: str, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self._path.open("a", encoding="utf-8") as f:
            f.write(f"{timestamp} - {to_email} - {message}\n")