from django.contrib import admin

# Register your models here.
from .models import Survey, Question

admin.site.register(Survey)
admin.site.register(Question)