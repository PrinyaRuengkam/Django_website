from django.db import models
 
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=128)
    
    def __str__(self):
        return self.category
    


class subject(models.Model):
    class_id  = models.CharField(max_length=10)
    class_name = models.CharField(max_length=128)
    class_credit = models.IntegerField()
    class_year = models.IntegerField()
    semester = models.IntegerField() 
    teacher = models.CharField(max_length=255) 
    
    class_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    on_register = models.BooleanField(default=False)

    def __str__(self):
        return self.class_name
        