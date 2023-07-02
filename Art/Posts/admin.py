from django.contrib import admin
from .models import Tag , Comment , Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post)