from twit.models import Profile,Twitter
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=Profile)
def first_create_message(sender,instance,created,**kwargs):
    if created:
        Twitter.objects.create(
        profile_user=instance,
        twit= f"{instance.user.username} Klube Katildi"
        )