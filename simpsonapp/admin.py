from django.contrib import admin

# Register your models here.
from simpsonapp.models import Character, Project, Client, Contact

admin.site.register(Character)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Contact)
