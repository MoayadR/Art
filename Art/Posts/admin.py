from django.contrib import admin
from .models import Tag , Comment , Post , Reported , UserHistoryTags

# Register your models here.
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Reported)
admin.site.register(UserHistoryTags)