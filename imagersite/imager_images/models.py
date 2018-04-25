from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Albums(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    cover = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=7,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        return '{}'.format(self.name)


class Photo(models.Model):
    product = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='photos')
    image = ImageField(upload_to='images')
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=7,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        return '{}'.format(self.title)
