from django.contrib import admin

# Register your models here.
from catalog.models import *

from django.shortcuts import render

# admin.site.register(Language)
# #admin.site.register(Book)
# # admin.site.register(Author)
# admin.site.register(Genre)
# #admin.site.register(BookInstance)

# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance
#
# #Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#
# # Register the admin class with associated model
# admin.site.register(Author, AuthorAdmin)
#
# # Register the Admin classes for Book using the decorator
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]
#
# # Register the Admin classes for BookInstance using the decorator
# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back')
#         }),
#     )

# @admin.register(GroupVideo)
# class GroupVideoAdmin(admin.ModelAdmin):
#     pass






class ProcessorVideoInline(admin.TabularInline):
    model = ProcessorVideo

@admin.register(CustomVideoGroup)
class CustomVideoGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(ProcessorVideo)
class ProcessorVideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'keywords',
        'watched_as_ad',
        'watched_as_video',
        'category',
        'channel',
    )
    list_filter = (['category'])
    actions = ['add_to_group']

    def add_to_group(self, request, queryset):
        return render(request,
                      'addtogroup_intermediate.html',
                      context={})
    add_to_group.short_description = 'Add selected videos to a custom video group'
