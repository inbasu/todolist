from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, default="...")
    in_list = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.name

    def done_undone(self):
        self.done = not self.done
        self.save()

    class Meta:
        ordering = ["-id"]
