from django.contrib import admin

from . import models
# Register your models here.
class CaptchaAdmin(admin.ModelAdmin):
    list_display = ('token', 'url', 'created', 'modified')
admin.site.register(models.Captcha, CaptchaAdmin)