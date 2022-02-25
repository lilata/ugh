from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Page)
admin.site.register(models.NavLink)
admin.site.register(models.ProfileTag)