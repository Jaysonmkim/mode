from django.contrib import admin
from .models import Students
from .models import Teachers
from .models import Parents
from .models import host

# Register your models here.
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Parents)
admin.site.register(host)