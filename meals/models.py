from django.db import models
from django.utils.text import slugify

# Create your models here.

# The Meals class is a model that has a name, description, serve, price, cooktime, and images, and returns name
class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    serve = models.IntegerField()
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cooktime = models.IntegerField()
    images = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)

    def save(self , *args , **kwargs):
        """
        If the slug field is empty, then populate it with the slugified version of the name field
        """
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Meals , self).save(*args , **kwargs)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name

# The Category class is a model that has a name field with a max length of 30 characters
class Category(models.Model):
    name = models.CharField(max_length=30)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
