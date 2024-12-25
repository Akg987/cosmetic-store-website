from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class cosmetics(models.Model):
    CATEGORY_CHOICES = [
        ('SKINCARE', 'Skincare'),
        ('MAKEUP', 'Makeup'),
        ('FRAGRANCE', 'Fragrance'),
        ('HAIRCARE', 'Haircare'),
        ('BODYCARE', 'Bodycare'),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    caption = models.TextField(max_length=500,null=False, blank=False)
    price = models.FloatField(null=False,blank=False)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='SKINCARE')
    image = models.ImageField(upload_to='files/cover')


class ask(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title= models.CharField(null=False,max_length=300)
    caption=models.CharField(max_length=2000,null=False)
    Created=models.DateTimeField()
    product = models.ForeignKey(cosmetics, on_delete=models.CASCADE)
    class Meta:
        verbose_name="Review"
        verbose_name_plural="Reviews"

class CommentAsk(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ask=models.ForeignKey(ask, on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    text=models.CharField(max_length=2000,null=False)
    Created=models.DateTimeField()
    class Meta:
        verbose_name="answer"
        verbose_name_plural="answers"
