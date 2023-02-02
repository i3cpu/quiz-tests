from django.contrib import admin
from tests.models import TestModel, TestModelCategories

# Register your models here.

admin.site.register(TestModel)
admin.site.register(TestModelCategories)
