from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type')
    search_fields = ('description',)

admin.site.register(Request, RequestAdmin)
