from django.contrib import admin
from . models import user
# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','phone','address','email','password')