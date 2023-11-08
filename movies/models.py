from django.db import models
from djangomovies.users.models import User
from django.utils.text import slugify



# Create your models here.
class TimestampedModel(models.Model):
    """
    An abstract base class model that provides automatic timestamp fields for created and modified dates/times.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Movie(TimestampedModel):
    '''
    A class to help create instances of a movie object
    '''
    title = models.CharField(max_length=140)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to="posters")
    director = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=140)
    
    class Meta:
        ordering = ['-created_by']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
