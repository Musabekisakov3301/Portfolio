from atexit import register
from multiprocessing.util import register_after_fork
from django.contrib import admin
from . import models 

admin.site.register(models.Portfolio)
admin.site.register(models.Contact)
admin.site.register(models.Animation)
admin.site.register(models.PageText)
admin.site.register(models.Welcome)
admin.site.register(models.Summary)
admin.site.register(models.Skils)
admin.site.register(models.Photo)
