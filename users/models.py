from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    custom user model for scalability
    making email field required
    """

    email = models.EmailField(blank=False)
