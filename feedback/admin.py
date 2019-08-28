from django.contrib import admin
from .models import FeedBack


# Register your models here.

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'description', 'active')
    list_filter = ['active']


admin.site.register(FeedBack, FeedBackAdmin)
