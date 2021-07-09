from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _

# Importing Models

from app_db.models import User
from app_db.models import User_Profile
from app_db.models import Student
from app_db.models import Mantaince_Request


class NewUserForm(ModelForm):

    class Meta:

        model = User
        fields = '__all__'


class UserProfileForm(ModelForm):
    class Meta:
        model = User_Profile
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class MantainceRequestForm(ModelForm):
    class Meta:
        model = Mantaince_Request
        fields = '__all__'
