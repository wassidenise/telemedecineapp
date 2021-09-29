from django.contrib import admin
from .models import Post
from .models import patients

admin.site.register(Post)
admin.site.register(patients)