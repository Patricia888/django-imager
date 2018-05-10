from django.forms import ModelForm
from .models import Albums, Photo


# class ProductForm(ModelForm):
#     # meta class
#     class Meta:
#         model = Product
#         fields = ['cover', 'name', 'description', 'price', 'published']

#     def __init__(self, *args, **kwargs):
#         # remove anything that is not preexisting in the Meta model
#         # above fields has no username, so must remove username
#         username = kwargs.pop('username')
#         super().__init__(*args, **kwargs)
#         # giving this field the ability to select a cover for a product
#         self.fields['cover'].queryset = Photo.objects.filter(product__user__username=username)
