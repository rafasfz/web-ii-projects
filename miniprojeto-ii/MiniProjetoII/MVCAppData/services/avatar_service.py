from abc import abstractmethod
from dataclasses import dataclass
from ..repositories.avatar_repository import AvatarRepository

@dataclass
class AvatarService:
    avatar_repository: AvatarRepository

    @abstractmethod
    def save_avatar(self, request_post):
        pass

    abstractmethod
    def get_avatars(self):
        pass