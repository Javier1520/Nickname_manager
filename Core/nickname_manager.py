from typing import List
from nickname_exceptions import NoNickNamesAvailable
import random
import threading

class NickManager:
    def __init__(self, nick_names: List[str]) -> None:
        self.nick_names = nick_names
        self.assigned_nick_names = {}
        self.lock = threading.Lock()

    def assign_nick_name(self, name: str) -> str:
        with self.lock:
            if len(self.nick_names) > 0:
                nick_name = random.choice(self.nick_names)
                self.nick_names.remove(nick_name)
                self.assigned_nick_names[nick_name] = name
                return nick_name
            else:
                raise NoNickNamesAvailable()
    
    def release_nick_name(self, nick_name: str) -> None:
        with self.lock:
            if nick_name in self.assigned_nick_names:                         
                self.nick_names.append(nick_name)
                del self.assigned_nick_names[nick_name]
            else:
                raise ValueError(f"The nickname '{nick_name}' does not exist.")

    def get_name(self, nick_name: str) -> str:
        return self.assigned_nick_names.get(nick_name, None)