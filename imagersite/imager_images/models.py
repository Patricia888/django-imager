from django.db import models

# Create your models here.

# create Photo

# title, description, date_uploaded, date_modified, and date_published fields. You should also have a published field which takes one of several possible values: (‘private’, ‘shared’, ‘public’)

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
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


# create Album

# title and description. It should also contain a date_created, date_modified, and date_published as well as a published field containing the same options described for Photos. 

