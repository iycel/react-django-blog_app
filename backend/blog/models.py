from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    CATEGORIES = {
        ('world', 'WORLD'),
        ('environmnet', 'ENVIRONMENT'),
        ('technology', 'TECHNOLOGY'),
        ('design', 'DESIGN'),
        ('culture', 'CULTURE'),
        ('business', 'BUSINESS'),
        ('politics', 'POLITICS'),
        ('opinion', 'OPINION'),
        ('science', 'SCIENCE'),
        ('health', 'HEALTH'),
        ('style', 'STYLE'),
        ('travel', 'TRAVEL'),
    }
    category = models.CharField(max_length=50, choices=CATEGORIES, default='WORLD')
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')


