from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    # type = models.CharField(max_length=250)
    # address = models.CharField(max_length=250)
    short_description = models.TextField()
    long_description = models.TextField()

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])