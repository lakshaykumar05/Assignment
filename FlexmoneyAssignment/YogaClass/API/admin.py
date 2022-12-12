from django.contrib import admin
from API.models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','age','batchType','paymentStatus')

admin.site.register(User, UserAdmin)

# Register your models here.
