from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def assign_user_permission(sender, instance: User, created: bool, **kwargs):
    if created:
        try:
            # Get the content type for the User model
            user_content_type = ContentType.objects.get_for_model(User)

            view_permission = Permission.objects.get(codename="view_user",
                                                     content_type=user_content_type)
            change_permission = Permission.objects.get(codename="change_user",
                                                       content_type=user_content_type)

            instance.user_permissions.add(view_permission, change_permission)
            instance.save()
        except Exception as e:
            print(f"Error assigning permissions: {str(e)}")


# Ensure the signal is connected
post_save.connect(assign_user_permission, sender=User)
