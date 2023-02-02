from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, default="...")
    in_list = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # finished = models.DateTimeField(default=True)

    def __str__(self) -> str:
        return self.name

    def done_undone(self):
        self.done = not self.done
        self.save()
