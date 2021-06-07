from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Issuer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.user.username

class Issue(models.Model):
    issue_type = models.CharField(max_length=200)
    issue_detail = models.CharField(max_length=500)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE, related_name='issuers')

    def __str__(self) :
        return str(self.issue_type) + " issue for " + str(self.issuer)
    
# Will execute when a user is created
def post_user_created_signal(sender, instance, created, **kwargs):
    # Instance is basicaly the string rep of the new object created
    # created is True is its a new entry or False if its an update
    if created:
        Issuer.objects.create(user=instance)  # Create a new Issuer when a new User is created ie signup
     

# When User model saved call the post_user_created_signal method 
post_save.connect(post_user_created_signal, sender=User)
