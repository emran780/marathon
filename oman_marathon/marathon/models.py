from django.db import models
from django.contrib.auth.models import User

class Run(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"

class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other runner fields as needed
    runs = models.ManyToManyField(Run, through='RunRegistration')

    def __str__(self):
        return self.user.username

class RunRegistration(models.Model):
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE)
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.runner.user.username} - {self.run.name} - {self.registration_date}"

