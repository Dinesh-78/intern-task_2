from django.contrib import admin
from .models import Profile,User,blog,hcategory
# Register your models here.
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(blog)
admin.site.register(hcategory)

