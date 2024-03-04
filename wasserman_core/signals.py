# wasserman_core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def make_user_inactive(sender, instance, **kwargs):
    if kwargs.get('created', False):  # Le signal est appelé lors de la création de l'utilisateur
        instance.is_active = False
        instance.save()