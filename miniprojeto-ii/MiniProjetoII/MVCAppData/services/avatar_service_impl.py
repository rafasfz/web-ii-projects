from abc import abstractmethod
from dataclasses import dataclass
from ..repositories.avatar_repository import AvatarRepository
from .avatar_service import AvatarService
from ..forms.avatar_form import AvatarForm

@dataclass
class AvatarServiceImpl(AvatarService):
    avatar_repository: AvatarRepository

    def save_avatar(self, request_post):
      avatar_form = AvatarForm(request_post)
      if avatar_form.is_valid():
        avatar = self.avatar_repository.save_avatar(avatar_form)
        return avatar
      return None

    abstractmethod
    def get_avatars(self):
      avatar = self.avatar_repository.get_avatars()
      return avatar