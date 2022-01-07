from django.contrib import admin
from .models import Person

# Register your models here.
class ApproveAdmin(admin.ModelAdmin):
    list_display = ('name','address','accuracy')



admin.site.register(Person,ApproveAdmin)