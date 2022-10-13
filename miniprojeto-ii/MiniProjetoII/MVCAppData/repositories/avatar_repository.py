from ..models import Avatar

class AvatarRepository():
  def save_avatar(self, form_avatar):
    avatar = form_avatar.save()
    return avatar
  
  def get_avatars(self):
    return Avatar.objects.all()
