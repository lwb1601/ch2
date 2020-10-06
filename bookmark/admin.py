from django.contrib import admin
from bookmark.models import BookmarkSet, Bookmark
# Register your models here.

class BookmarkInline(admin.TabularInline):
    model = Bookmark
    extra = 4

class BookmarkAdmin(admin.ModelAdmin):
    inlines = [BookmarkInline]

admin.site.register(BookmarkSet, BookmarkAdmin)
admin.site.register(Bookmark)