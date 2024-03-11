from django.contrib import admin
from .models import CarList,ShowRoomList,Reviews

# Register your models here.
admin.site.register(CarList)
admin.site.register(ShowRoomList)
admin.site.register(Reviews)