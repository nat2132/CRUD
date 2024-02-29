from django import forms
from .models import Users


class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsersForm,self).__init__(*args, **kwargs)