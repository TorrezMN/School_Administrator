from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, User_Profile


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


#########################################
#       Crear Perifil Personal          #
#########################################

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(profile_user=instance).save()
