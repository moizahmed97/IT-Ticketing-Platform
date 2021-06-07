from django.contrib import admin
from issues.models import User,Issue,Issuer, Technician

# Register your models here.
admin.site.register(User)
admin.site.register(Issue)
admin.site.register(Issuer)
admin.site.register(Technician)