from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_technician = models.BooleanField(default=False)
    is_issuer = models.BooleanField(default=False)

class Issuer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anydesk_id = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self) :
        return self.user.username

class Issue(models.Model):
    
    
    # Choice Fields
    HIGH = 'HIG'
    MEDIUM = 'MED'
    LOW = 'LOW'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    ]
    PENDING = 'Pending'
    ASSIGNED = 'Assigned'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ASSIGNED, 'Assigned'),
        (COMPLETED, 'Completed')
    ]

    # Model Fields
    issue_type = models.CharField(max_length=200)
    issue_detail = models.CharField(max_length=500)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE, related_name='issuers')
    priority = models.CharField(
        max_length=3,
        choices= PRIORITY_CHOICES,
        default=MEDIUM
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    location = models.CharField(default="None", blank=True, max_length=30)
    date_added = models.DateTimeField(auto_now_add=True, max_length=30)
    technician = models.ForeignKey("Technician", null=True, blank=True, on_delete=models.CASCADE)
    anydesk_id = models.CharField(blank=True, max_length=100, null=True)
    screenshot = models.ImageField(null=True, blank=True)


    def __str__(self) :
        return str(self.issue_type) + " issue for " + str(self.issuer)
    
# Will execute when a user is created
def post_user_created_signal(sender, instance, created, **kwargs):
    # Instance is basicaly the string rep of the new object created
    # created is True is its a new entry or False if its an update
    if created and not instance.is_technician and not instance.is_superuser:
        Issuer.objects.create(user=instance)  # Create a new Issuer when a new User is created ie signup
        print('User being creared is not tech')
    if created and instance.is_technician:
        print(instance)
        Technician.objects.create(user=instance) 

# When User model saved call the post_user_created_signal method 
post_save.connect(post_user_created_signal, sender=User)


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) :
        return self.user.username    


# Will execute when a technician is deleted 
# basically we need to delete the user model for this technician as well 
def post_technician_deleted_signal(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()
    

# When a technician is deleted call the post_technician_deleted_signal method 
post_delete.connect(post_technician_deleted_signal, sender=Technician)


