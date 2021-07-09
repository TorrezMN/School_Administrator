from django.shortcuts import render
from django.views.generic import TemplateView


# Importing forms.
from .admin_forms import NewUserForm,UserProfileForm,StudentForm,MantainceRequestForm


class Admin_Home(TemplateView):
    template_name = 'admin_home.html'

    def get(self, request):
        cont = {
            'form1':NewUserForm(),
            'form2':UserProfileForm(),
            'form3':StudentForm(),
            'form4':MantainceRequestForm(),
            'head_title': 'Home',
        }
        return render(request, self.template_name, cont)
