from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student, Profile


# Jab bhi new Student create hoga,
# automatically uska Profile create ho jayega.
@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):

    # created=True sirf tab hota hai jab Student
    # pehli baar database mein create ho raha ho.
    if created:

        Profile.objects.create(
            student=instance
        )