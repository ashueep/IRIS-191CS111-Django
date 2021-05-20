from django.contrib import admin
from .models import Club, Items, ItemRequest, RequestStatus
# Register your models here.

admin.site.register(Club)
admin.site.register(Items)
admin.site.register(ItemRequest)
admin.site.register(RequestStatus)