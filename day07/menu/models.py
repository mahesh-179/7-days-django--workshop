from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVariety(models.Model):
    CHAI_TYPE = [
        ('MT', 'MASALA TEA'),
        ('LT', 'LEMON TEA'),
        ('NT', 'NORMAL TEA'),
        ('BT', 'BLACK TEA'),
    ]

    image = models.ImageField(upload_to='chais/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE)

    def __str__(self):
        return self.name
    
class ChaiReview(models.Model):
    chai=models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comments = models.TextField()
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVariety,related_name='store')


    def _str_(self):
        return self.name
    
#one to one
chai =  models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
certificate_number=models.CharField(max_length=10)
issued_date=models.DateTimeField(default=timezone.now)
validate=models.DateTimeField()



