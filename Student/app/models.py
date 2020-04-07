from django.db import models
from django.utils.html import mark_safe

class StudentModel(models.Model):
    Class_CHOICES = (
        ('9am', '9am'),
        ('11am', '11am')
    )

    name = models.CharField(max_length=60)
    cno = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    timeing = models.CharField(max_length=6, choices=Class_CHOICES, default='9am')
    photo1 = models.ImageField(upload_to='student/')
    photo2 = models.ImageField(upload_to='studnet/')
    t_date = models.DateField(auto_now_add=True)

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.photo1))

    image_tag.short_description = 'Image'


