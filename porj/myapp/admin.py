from django.contrib import admin
from myapp.models import Books, category, product

admin.site.register(Books)

admin.site.register(category)

admin.site.register(product)


# Register your models here.
