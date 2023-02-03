from django.test import TestCase
from todo.models import Task
from django.contrib.auth.models import User

# Create your tests here.
class ModelTest(TestCase):
    test_user = User.objects.create(username="username", password="password")

    def testTaskModel(self):
        task = Task.objects.create(
            name="task_name",
            description="Base description",
            author=self.test_user,
        )
        self.assertEqual(str(task), "task_name")
        self.assertTrue(isinstance(task, Task))
