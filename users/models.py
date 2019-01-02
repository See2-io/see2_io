# Import Django modules here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import third party modules here.


# Import local See2 modules here.
from communities.models import Member


class User_Profile(models.Model):
    '''
    This :class: is automatically created when a user signs-up to See2.
    The attributes are usually explicitly set by the user.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    job_title = models.CharField(max_length=64, blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    org = models.CharField(max_length=64, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True,)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()


class Inferred_Profile(models.Model):
    '''
    This :class: is automatically created when a user signs-up to See2.
    The attributes are dynamic and generated by the user's compass bots.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_inferred_profile(sender, instance, created, **kwargs):
    if created:
        Inferred_Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_inferred_profile(sender, instance, **kwargs):
    instance.inferred_profile.save()


class Wallet(models.Model):
    '''

    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=100.0)


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()
