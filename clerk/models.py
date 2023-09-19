from django.db import models
# from investor.models import User

# Create your models here.
class clerk(models.Model):
    # user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    hospital_id=models.CharField(max_length=100)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.hospital_id