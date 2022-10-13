from django.forms import ModelForm
from ..models import Avatar

class AvatarForm(ModelForm):
  class Meta:
    model = Avatar
    fields = ['fantasy_name', 'student']
