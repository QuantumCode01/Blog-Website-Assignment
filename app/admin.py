from django.contrib import admin
from .models import Post
from django.db import models
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=('id','title','content','publicationdate','name','image')
    formfield_overrides = {
    models.TextField: {'widget': admin.widgets.AdminTextareaWidget},
}
