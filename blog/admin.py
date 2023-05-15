from django.contrib import admin
from .models import Post, User, Tag, Category, Comment

from admin_auto_filters.filters import AutocompleteFilter
from import_export.admin import ExportActionMixin

from import_export.admin import ImportExportModelAdmin



# Register your models here.


# admin.site.register(User)
# admin.site.register(Tag)
# admin.site.register(Category)
# admin.site.register(Comment)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name'] 
admin.site.register(Category, CategoryAdmin)


class TagAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['tag'] 
admin.site.register(Tag, TagAdmin)

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ['author', 'category', 'tag', 'published_date',]
    list_display =('title' , 'thumbnail_image', 'author')
    search_fields = ['title', 'name']
    filter_horizontal = ['tag']
    autocomplete_fields = ['category',]

admin.site.register(Post, PostAdmin)


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['username'] 
admin.site.register(User, UserAdmin)


class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ['post', 'email',]
    search_fields = ['username',] 
    # autocomplete_fields = ('post',)
admin.site.register(Comment, CommentAdmin)








# # Register your models here.
# class BookAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('title', 'description', 'author', 'year')
# admin.site.register(Book, BookAdmin)


    
# class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#         ...

# admin.site.register(Blog, BlogAdmin)  

  