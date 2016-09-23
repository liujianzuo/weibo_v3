from django.contrib import admin

# Register your models here.


from dao import models

admin.site.register(models.Tags)
admin.site.register(models.UserProfile)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Topic)
admin.site.register(models.Weibo)
