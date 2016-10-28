from django.contrib import admin

# Register your models here.
from .models import Publication, Previous_Engagements

admin.site.register(Publication)

admin.site.register(Previous_Engagements)